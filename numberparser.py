import inflect
import nltk
import re
import numpy as np
import pandas as pd

## Credit to user 'Adnan Umer' for this utility at https://stackoverflow.com/questions/493174/is-there-a-way-to-convert-number-words-to-integers.
## I could not find an importable package that has this utility so I have while preserving remaining text within a string used this implementation.
def text2int (textnum, numwords={}):
    '''Parses a text an converts word representations of numbers into their integer counterparts
    Params - textnum : text containing numbers
    Returns - string with number words replaced with their digit representations
    '''
    if not numwords:
        units = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen",
        ]

        tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

        scales = ["hundred", "thousand", "million", "billion", "trillion"]

        numwords["and"] = (1, 0)
        for idx, word in enumerate(units):  numwords[word] = (1, idx)
        for idx, word in enumerate(tens):       numwords[word] = (1, idx * 10)
        for idx, word in enumerate(scales): numwords[word] = (10 ** (idx * 3 or 2), 0)

    ordinal_words = {'first':1, 'second':2, 'third':3, 'fifth':5, 'eighth':8, 'ninth':9, 'twelfth':12}
    ordinal_endings = [('ieth', 'y'), ('th', '')]

    textnum = textnum.replace('-', ' ')

    current = result = 0
    curstring = ""
    onnumber = False
    for word in textnum.split():
        if word in ordinal_words:
            scale, increment = (1, ordinal_words[word])
            current = current * scale + increment
            if scale > 100:
                result += current
                current = 0
            onnumber = True
        else:
            for ending, replacement in ordinal_endings:
                if word.endswith(ending):
                    word = "%s%s" % (word[:-len(ending)], replacement)

            if word not in numwords:
                if onnumber:
                    curstring += repr(result + current) + " "
                curstring += word + " "
                result = current = 0
                onnumber = False
            else:
                scale, increment = numwords[word]

                current = current * scale + increment
                if scale > 100:
                    result += current
                    current = 0
                onnumber = True

    if onnumber:
        curstring += repr(result + current)

    return curstring

## Clean the format to make numbers more recognizable
## Turn actual digit representations of numbers to their word counterpart
## This is so that text2int will combine terms like '3.6 billion' into a single number
def format_clean(statement):
    '''Cleans a statement so that it is in an easily parsible format for text2int
    Params - statement : string of the statement
    Return - statement formatted for text2int parsing
    '''
    statement = re.sub("\d\d?:\d\d","", statement)
    statement = re.sub("\$","", statement)
    statement = re.sub("\%","", statement)
    statement = re.sub(",","", statement)
    statement = re.sub("\.\d+", '', statement)
    statement = re.sub("(\d+)", int2word, statement)
    statement = re.sub(",","", statement)
    return statement

## Special function for format_clean that replaces digit representations with their word form
def int2word(string):
    '''Takes a string of digit characters and converts it into a word representation
    Params - string : string containing only digit characters
    Return - the desired number as a word representation
    '''
    word = string.string[string.start(0):string.end(0)]
    n2w = inflect.engine()
    return n2w.number_to_words(int(word))

## Checks NTLK PoS parsed token for 'CN' which is cardinal parsed numbers.
def numbers_contained(tokens):
    result = []
    for token in tokens:
        if token[1]=='CD':
            number = get_num(token[0])
            if number!=0:
                result.append(number)
    return result

## Gets the number from a 'CN' parsed entry
## This is an extension of simply typecasting digit characters to int
## Covers cases such as '2nd' or '1st'
def get_num(word):
    num_names = {'one':'1', 'two':'2', 'million':'1000000', 'billion':'1000000000', 'trillion':'1000000000000'}
    word = re.sub(',', '', word)
    word = re.sub('st|nd', '', word)
    try:
        word = int(word)
    except ValueError:
        try:
            word = num_names[word]
        except KeyError:
            return 0
        return get_num(word)
    return word

## Combines a list of lists of numbers into a single list of numbers
def get_all_numbers(number_array):
    result = []
    for number_list in number_array:
        for number in number_list:
            result.append(number)
    return result

## The purpose of all of the above helpers - find the distribution of leading digits in a set of text
def leading_digits(df):
    ''' Computes the distribution of leading digits within words mentioned in a set of spoken workds
    Params - df : Dataframe with a 'statement' column to parse
    Returns - dictionary that maps leading digits to their number of occurences
    '''
    statements = df['statement']
    statements = list(map(format_clean, statements))
    statements = list(map(text2int, statements))

    parsed = list(map(lambda x: nltk.pos_tag(nltk.tokenize.word_tokenize(x)), statements))

    num_mask = list(map(lambda x: numbers_contained(x), parsed))

    nums = get_all_numbers(num_mask)
    digits = np.array(list(map(lambda x: int(str(x)[0]), nums)))
    result = {"total":len(digits)}
    for i in range(1,10):
        result[i] = len(digits[digits==i])
    return result