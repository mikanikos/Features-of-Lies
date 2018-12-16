
import pickle
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import string
import random
import seaborn as sn
from sklearn.model_selection import *
from sklearn.preprocessing import *
from sklearn.linear_model import *
from sklearn.ensemble import *
from sklearn.metrics import *
from sklearn.externals import *
from sklearn.naive_bayes import *
from sklearn.svm import *
from sklearn.utils import shuffle
from textblob.classifiers import NaiveBayesClassifier
from dateutil.parser import parse
import datetime as dt
pd.options.mode.chained_assignment = None  # default='warn'
from nltk.corpus import stopwords
from nltk import *
from textblob import TextBlob, Word

from cleaningtool import *


def load_data(path):
    columns = ["ID", "label", "statement", "subject", "speaker", "job", "state", "party", "barely_true_cts",
        "false_cts", "half_true_cts", "mostly_true_cts", "pants_on_fire_cts", "context"]
    
    data = pd.read_table(path, header=None)
    data.columns = columns
    return data


def convert_label(data):
    mapping = {'true': 3, 'mostly-true': 2, 'half-true': 1, 'barely-true': 0, 'false': -1, 'pants-fire': -2}
    return data.label.map(mapping)


def save_data(df, feat, path):
    df[feat].to_csv(path, header=False, index=False, sep=" ")
    subprocess.call(["sed -i 's/\"//g' " + path], shell=True)


def plot_length_statement_distr(data):
    # Plot the distribution of the length of the tweets

    lengths = data.apply(lambda x: len(x.split()))
    plt.hist(lengths, log=True)
    plt.xlabel('Length of statement')
    plt.ylabel('Number of statements')
    plt.show()
    
    
def plot_label_distribution(data):
    return sn.countplot(x='label', data=data, palette='hls')


def plot_freq_word(data):

    all_words = []
    for t in data.values:
        for w in t.split():
            if len(w) > 3:
                all_words.append(w)

    all_words_df = pd.Series(all_words)
    words_count = pd.DataFrame(all_words_df.groupby(all_words_df.values).count().sort_values(ascending=False)).reset_index()
    words_count.columns = ["word", "count"]
    words_count.head(20).plot.bar(x="word", y="count")
    
    
def clean_data(hd_df, feat):

    hd_df[feat] = hd_df[feat].apply(lambda x: " ".join(x.lower() for x in x.split()))

    # Removing tags
    hd_df[feat] = hd_df[feat].str.replace('<.*?>','')

    # Removing possible mentions or urls (don't know if it's necessary but might be) 
    hd_df[feat] = hd_df[feat].str.replace('@\w+','')
    hd_df[feat] = hd_df[feat].str.replace('http.?://[^\s]+[\s]?','')

    # Removing punctuation and symbols
    hd_df[feat] = hd_df[feat].str.replace('[^\w\s]', '')
    hd_df[feat] = hd_df[feat].apply(lambda x: " ".join(x for x in x.split() if x not in string.punctuation))

    # Removing non alphabetical character
    hd_df[feat] = hd_df[feat].apply(lambda x: " ".join(x for x in x.split() if x.isalpha()))

    # Removing characters non longer than 1
    hd_df[feat] = hd_df[feat].apply(lambda x: " ".join(x for x in x.split() if len(x) > 1))

    # Removing stopwords
    sw = stopwords.words('english')
    hd_df[feat] = hd_df[feat].apply(lambda x: " ".join(x for x in x.split() if x not in sw))

    # Removing digits
    hd_df[feat] = hd_df[feat].apply(lambda x: " ".join(x for x in x.split() if not x.isdigit()))

    # Removing words that appear less than 5
    word_freq = pd.Series(' '.join(hd_df[feat]).split()).value_counts()
    less_freq = word_freq[word_freq < 5]
    hd_df[feat] = hd_df[feat].apply(lambda x: " ".join(x for x in x.split() if x not in less_freq))

    # Removing multiple spaces
    hd_df[feat] = hd_df[feat].apply(lambda x: x.strip())
    hd_df[feat] = hd_df[feat].str.replace(' +',' ')

    # Lemmatization (better than stemmatization imho)
    hd_df[feat] = hd_df[feat].apply(lambda x: " ".join([Word(w).lemmatize() for w in x.split()]))

    # Removing blank lines
    #hd_df.drop(hd_df[hd_df[feat] == ""].index, inplace=True)
    
    # Removing possible duplicates
    #hd_df[feat].drop_duplicates(inplace=True)

    return hd_df


def convertToTupleList(df):
    list_tuple = [tuple(x) for x in df.values]
    #random.shuffle(list_tuple)
    return list_tuple


def train_NLTK_NB(labeled_list_tr):
    all_words = set(word.lower() for passage in labeled_list_tr for word in word_tokenize(passage[0]))
    train_set = [({word: (word in word_tokenize(x[0])) for word in all_words}, x[1]) for x in labeled_list_tr]
    classifier = NaiveBayesClassifier.train(train_set)
    return classifier


def test_NLTK_NB(labeled_list_te, classifier):
    all_words = set(word.lower() for passage in labeled_list_te for word in word_tokenize(passage[0]))
    test_set = [({word: (word in word_tokenize(x[0])) for word in all_words}, x[1]) for x in labeled_list_te]
    print("Accuracy: ", classify.accuracy(classifier, test_set))
    return test_set


def getFeatures(fileName):
    # Loading embeddings created before
    embeddings = np.load("data/embeddings.npy")
    feat_repr = []
    with open('data/vocab.pkl', 'rb') as f:
        vocab = pickle.load(f)
        with open(fileName) as file:
            for line in file:
                tokens = [vocab.get(t, -1) for t in line.strip().split()]
                #tokens = [t for t in tokens if t >= 0]
                embed_sum = np.zeros(embeddings.shape[1])
                for t in tokens:
                    embed_sum = np.sum([embed_sum, embeddings[t]], axis=0)
                feat_repr.append(embed_sum/len(tokens))
    return feat_repr


def train_RF(train_data, train_labels, test_data, test_labels):
    rforest = RandomForestClassifier(n_estimators=100)
    rforest.fit(train_data, train_labels)
    y_pred = rforest.predict(test_data)
    print("Accuracy: ", accuracy_score(test_labels, y_pred))
    return y_pred


def train_LR(train_data, train_labels, test_data, test_labels):
    logistic = LogisticRegression(solver="lbfgs", multi_class='auto')
    logistic.fit(train_data, train_labels)
    y_pred = logistic.predict(test_data)
    print("Accuracy: ", accuracy_score(test_labels, y_pred))
    return y_pred


def train_SVM(train_data, train_labels, test_data, test_labels):
    svm_class = LinearSVC()
    svm_class.fit(train_data, train_labels)
    y_pred = svm_class.predict(test_data)
    print("Accuracy: ", accuracy_score(test_labels, y_pred))
    return y_pred


def preprocess_data(data):
    
    data = clean_df(data)
    
    # Manually cleaning state field
    data['state'] = data['state'].apply(lambda x: "Washington" if x == "Washington, D.C." or x == "Washington, D.C. " or x == "Washington state" or x == "Washington DC" or x == "Washington D.C." else x)
    data['state'] = data['state'].apply(lambda x: "Wisconsin" if x == "Wisconsin " else x)
    data['state'] = data['state'].apply(lambda x: "Ohio" if x == "ohio" else x)
    data['state'] = data['state'].apply(lambda x: "New York" if x == "New York " else x)
    data['state'] = data['state'].apply(lambda x: "Illinois" if x == "Illinois " else x)
    data['state'] = data['state'].apply(lambda x: "Georgia" if x == "Georgia " else x)
    data['state'] = data['state'].apply(lambda x: "Florida" if x == "Florida " else x)
    data['state'] = data['state'].apply(lambda x: "Colorado" if x == "Colorado " else x)
    data['state'] = data['state'].apply(lambda x: "Massachusetts" if x == "Massachusetts " else x)
    data['state'] = data['state'].apply(lambda x: "Pennsylvania" if x == "PA - Pennsylvania" else x)
    data['state'] = data['state'].apply(lambda x: "Tennessee" if x == "Tennesse" else x)
    data['state'] = data['state'].apply(lambda x: "Virginia" if x == "Virgiia" or x == "Virgina" or x == "Virginia " or x == "Virginia director, Coalition to Stop Gun Violence" else x)
    
    # Cleaning context field
    data['context'] = data['context'].apply(lambda x: "a speech" if x == "a speech." or x == "in a speech" else x)
    data['context'] = data['context'].apply(lambda x: "a television interview" if x == "a TV interview" or x == "a TV interview." else x)
    data['context'] = data['context'].apply(lambda x: "a debate" if x == "a debate." else x)
    data['context'] = data['context'].apply(lambda x: "a radio interview" if x == "a radio interview." else x)
    data['context'] = data['context'].apply(lambda x: "an interview" if x == "an interview." else x)
    data['context'] = data['context'].apply(lambda x: "a television commercial" if x == "a TV commercial" else x)
    data['context'] = data['context'].apply(lambda x: "a television ad" if x == "a TV ad." or x == "a TV ad" else x)
    data['context'] = data['context'].apply(lambda x: "a press release" if x == "a press release." else x)
    data['context'] = data['context'].apply(lambda x: "a news release" if x == "a news release." else x)
    
    # Cleaning job field
    data['job'] = data['job'].apply(lambda x: "Governor" if x == "governor" else x)
    data['job'] = data['job'].apply(lambda x: "U.S. Senator" if x == "U.S. senator" else x)
    data['job'] = data['job'].apply(lambda x: "U.S. Representative" if x == "U.S. representative" or x == "U.S. House of Representatives" else x)
    data['job'] = data['job'].apply(lambda x: "State Representative" if x == "State representative" or x == "state representative" else x)
    data['job'] = data['job'].apply(lambda x: "State Senator" if x == "State senator" else x)
    data['job'] = data['job'].apply(lambda x: "State Senator" if x == "State senator" or x == "state senator" else x)
    data['job'] = data['job'].apply(lambda x: "State Senator" if x == "State senator" or x == "state senator" else x)
    
    return data
