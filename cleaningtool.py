## Short utilities to clean the dataframes used in other pieces of the project.

## Imports
import numpy as np
import pandas as pd
import re

def replace(arr, term, category, inplace=True):
    ''' Replaces all instances matching an expression in an iterable with a canonical representation
    Params - arr : array-like to iterate, term : regex defining terms to replace, category : desired replacement string,
    inplace : specifies if operation is in place (true by default)
    Returns - arr
    '''
    if not inplace:
        arr = arr.copy()
    reg = re.compile(term)
    mask = np.vectorize(lambda x: True if reg.search(str(x).lower()) else False)
    arr[mask(arr)] = category
    return arr

def find(arr, term):
    ''' Finds all elements of an array matching a specific expression.
    Params - arr : array-like to iterate, term : regex defining terms to return
    Returns - subset of arr that matches the regex
    '''
    reg = re.compile(term)
    mask = np.vectorize(lambda x: True if reg.search(str(x).lower()) else False)
    return arr[mask(arr)]

def clean_df(df):
    ''' Cleans desired dataframe to have better categorization of jobs and contexts
    Params - df : dataframe to be cleaned
    Returns - copy of the dataframe with jobs and contexts features categorized in more consistent ways
    '''
    df = clean_jobs(df)   
    return df

## Function to clean the jobs field
## Cleaning was manually determined
def clean_jobs(df):
    ''' NOTE: Use clean_df instead of clean_jobs - clean_jobs is a helper for clean_df
    Cleans the jobs of a dataframe.
    Params - df : dataframe to clean
    Returns - Cleaned copy of the dataframe
    '''
    ## Initialize result df and job array
    result = df.copy()
    arr = result['job']
    
    ## Sets Candidates, Former and Foreign members aside
    ## These are replaced with their original entries later
    ## (this is so they do not get replaced when found within other criteria)
    arr = replace(arr, 'candidate', 'Candidate')
    arr = replace(arr, 'former', 'Former')
    arr = replace(arr, 'russia|china|cuba', 'Foreign')

    ## Group politicians according to their role
    arr = replace(arr, 'u.s. senator', 'Senator')
    arr = replace(arr, 'state senator', 'Senator')
    arr = replace(arr, 'senate', 'Senator')
    arr = replace(arr, 'senate majority', 'Senator')
    arr = replace(arr, 'senate minority', 'Senator')
    arr = replace(arr, 'representative', 'House Member')
    arr = replace(arr, 'house majority', 'House Member')
    arr = replace(arr, 'house minority', 'House Member')
    arr = replace(arr, 'rep.', 'House Member')
    arr = replace(arr, 'house member', 'House Member')
    arr = replace(arr, 'congressman', 'Congress Member')
    arr = replace(arr, 'congresswoman', 'Congress Member')
    arr = replace(arr, 'member of congress', 'Congress Member')
    arr = replace(arr, 'congress,', 'Congress Member')
    arr = replace(arr, 'governor of', 'Governor')
    arr = replace(arr, 'mayor', 'Mayor')
    arr = replace(arr, 'assembly', 'Assembly Member')
    arr = replace(arr, 'attorney', 'Attorney')
    
    ## Group other common jobs under canonical titles
    arr = replace(arr, 'host', 'Radio/TV host')
    arr = replace(arr, 'ceo', 'CEO')
    arr = replace(arr, 'treasur', 'Treasurer')        
    arr = replace(arr, '^actor', 'Actor')
    arr = replace(arr, 'teacher', 'Teacher')
    arr = replace(arr, 'blogg', 'Blogger')
    arr = replace(arr, 'blog\\b', 'Blog')
    
    ## Group members of the media under canonical titles
    arr = replace(arr, 'news', 'News Host/Affiliate')
    arr = replace(arr, 'anchor', 'News Host/Affiliate')
    arr = replace(arr, 'column', 'Columnist')
    
    ## Group non-descript jobs under canonical titles
    arr = replace(arr, 'business owner', 'Business Owner')
    arr = replace(arr, 'business(wo)?man', 'Businessman')
    arr = replace(arr, 'president,', 'President of Group/Association')
    arr = replace(arr, 'president of', 'President of Group/Association')
    
    ## Group groups under canonical titles
    arr = replace(arr, 'advoca', 'Advocacy Group')

    ## Restore reserved entries and create result
    arr[arr=='Former'] = df['job'][arr=='Former']
    arr[arr=='Foreign'] = df['job'][arr=='Foreign']
    result['job'] = arr
    
    return result