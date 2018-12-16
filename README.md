# Features of Lies

# Data Story

https://paul92.github.io/ADA_Project/

# Abstract

In the past years, we have become more and more bombarded by
information from multiple sources thanks to the rise of the Internet. The huge
amount of information we have at our fingertips and the freedom of the online
world comes unfortunately with the downside of corrupted information,
misinterpretations or plain lies. We believe that being able to tell the truth
from a lie has become a key ability. Using the Liar dataset, we plan to
identify key features of lies and measure their spread in the online world,
therefore making an analysis of the most reliable online medium, and on markers
of untruthful statements.

# Research Question

- Which statements within the dataset are most prevalent for determining truthfulness.

- Which topics contain the most lies?

- Which speakers lie the most?

- Do public figures lie more on their social media accounts than interviews or
  speeches?
  
- Are there underlying lexical features to lies? Is the vocabulary the same?

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

# A list of internal milestones up until project milestone 3

## Week 1 – Augmentation and statement processing: 

- Until this point, most of the features we have analyzed have been within the categorical features of the dataset. We will expand this by accounting for the date of statements as well as the best classification we can make for their sentiments. We have already implemented some sentiment classifers, we now wish to see how they can influence our model.

- We will also look for other relevant features to query from the json files hosted on Politifacts.


## Week 2 – Model improvement, quantify generalizability to inspire data story: 

- We want to improve our predictive model hopefully by accounting for more underlying features. We also want to see if this model is at all generalizable, so we want to take some reference some other fake news datasets and see if we can make predictions on those datasets with our model (will require a lot of cleaning to fit our model format). 

- If we find that our model is generalizable in this way, then we will analyze which features are important in our model prediction to create our data story. 

- If these results are not generalizable, we would like to isolate specific speakers, topics, or pairs of speakers to see if we can find some underlying patterns to make a convincing data story that may not be in the form of a general model. In doing this, we want to externalize from our dataset and see if our findings are applicable for other statements of this type.

## Week 3 – Data stories and visualizations

- Based upon our week 2 findings, we want to construct some good visuals and a compelling data story. We do not yet know if our data story will be about general findings or if they will require a case-study approach relating to specific speakers and/or subjects.

# Distribution of Workload

- Andrea – initial data exploration, machine learning models, querying Politifacts, analysis of headlines, preparation of presentation
- Marshall – project proposal, initial data exploration, data cleaning, analysis of numeric statements, preparation of presentation
- Paul – project proposal, word frequency analysis, sentiment analysis, polished visualization, construction of data story, preparation of presentation

# References

- The "Liar, Liar Pants on Fire" dataset used was provided by William Wang at: https://arxiv.org/abs/1705.00648

The following tools were throughout the project:
- https://python-graph-gallery.com/ - For visualization demonstrations and ideas
- http://evoq-eval.siam.org/Portals/0/Publications/SIURO/Vol1_Issue1/Testing_for_the_Benford_Property.pdf?ver=2018-03-30-130233-050 - - Paper - For testing for the Benford Property within our data, including methods of quantifying well-fittedness
- https://stackoverflow.com/questions/493174/is-there-a-way-to-convert-number-words-to-integers - Solution for converting words to numbers proposed by user 'Adhan Umer' was used as part of our routines.
