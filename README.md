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

- Which statements within the dataset are most prevalent for determining truthfulness?

- Which topics contain the most lies?

- Which speakers lie the most?

- Do public figures lie more on their social media accounts than interviews or
  speeches?
  
- Are there underlying lexical features to lies? Is the vocabulary the same?

Our analysis is focused on the Liar dataset, a dataset with over 10000
statements with labels indicating their truthfulness.

We have explored the dataset in Data_Analysis.ipynb, doing an analysis both of the meta-data and the text of the
statements based on their feature, trying to get some insight into possible
correlations with the truth classification and to better understand the
dataset. We also trained different classifiers to validate our analysis and discover more relevent aspects of the statements.  

# Results

While performing this analysis, we have realized that there is not enough data
to achieve the level of generality we hoped for in the original proposal.
Therefore, our focus has shifted towards a feature analysis of the lies, as
well as the design of classifiers for statements from politifacts.

Note that the feature analysis we performed might not generalize, since the
dataset is relatively small. However, the original publishers of the dataset
have obtained promising results by training various machine learning models,
which has also been our goal.

We have collected more data about the statements using the politifacts API.
As mentioned above, we used this API to do generalize our analysis from
the Liar dataset to other political statements. We also performed a sentiment analysis on the statements and analyzed several other aspects such as the statements that contain numbers and the words frequency distribution.

We also trained different classifiers not only for getting a good model but above all for better focusing on the most informative features of the lies in order to validate our results and get more useful insights. Therefore we used the insight we gained in the dataset to
train machine learning models in order to analyse the statements from
politifacts. This is related to our intial goal, of finding
the trustworthiness of various media sources, but limited in scope to political
statements and their source.

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
