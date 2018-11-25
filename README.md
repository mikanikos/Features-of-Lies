# Features of Lies

Our analysis is focused on the Liar dataset, a dataset with over 10000
statements with labels indicating their truthfulness.

We have explored the dataset in Exploration.ipynb, doing an analysis of the
statements based on their feature, trying to get some insight into possible
correlations with the truth classification and to better understand the
dataset.

# Results

While performing this analysis, we have realized that there is not enough data
to achieve the level of generality we hoped for in the original proposal.
Therefore, our focus has shifted towards a feature analysis of the lies, as
well as the design of classifiers for statements from politifacts.

Note that the feature analysis we performed might not generalize, since the
dataset is relatively small. However, the original publishers of the dataset
have obtained promising results by training various machine learning models,
which is also our goal.

# Augmentation

We have collected more data about the statements using the politifacts API.
As mentioned above, we plan to use this API to do generalize our analysis from
the Liar dataset to other political statements. To this end, we have followed
our inital plan to perform feature augmentation based on sentiment analysis. We
have experimented with two approaches: the python nltk library and google
cloud. From our analysis, the former does not seem to produce very reliable
metrics as is, but has a Bayes classifier that we plan to train on this
dataset. On the other hand, the latter has consistently provided accurate
metrics in our experiments and we plan to use it to augment the dataset.

These experiments can be found in SentimentAnalysis.ipynb.

# Future plans

In the following weeks, we will use the insight we gained in the dataset to
train machine learning models in order to analyse the statements from
politifacts. We plan to use their API to analyse political statements and do
an analysis on them. This is related to our intial goal, of finding
the trustworthiness of various media sources, but limited in scope to political
statements and their source.
