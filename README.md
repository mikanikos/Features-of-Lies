# Features of Lies

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

# Research questions
- Which is the more reliable, Facebook or Twitter?

- Which are the topics that tend to have the most lies?

- What are features of lies? Is an affirmative statement more or less likely to
  be a lie? Are feelings somehow involved?

- Do public figures lie more on their social media accounts than interviews or
  speeches?


# Dataset
Our analysis will start with the Liar dataset, which we found to be an
invaluable resource for looking at patterns behind untruthful statements.
Moreover, this dataset provides a control group of statements that have been
classified as being true, allowing us to compare the features of a lie with
the ones of a truth. In total, we have about 12000 statements that we can use
to gain some insight into how people lie.

The data set contains many features we are immediately interested in, such as
speaker and context. One important part of our project will involve
applying natural language processing techniques in order to find new
features that we might be interested in, such as sentiment analysis or to
perform a classification of the statements based on their topic.

For named speakers, we believe we can cross-reference with Wikipedia to gather
more information about the person. Using this information, we might be able
to look for trends in trustworthiness of people based on their political
affiliation, origin, career or any other personal information.

We also think that we can find ways use the statement itself to construct
interesting features such as sentiment and topic. Currently, we plan to use
NLTK for sentiment analysis, but will need to do research to find libraries or
implementations that may help us categorize statements by their topic (such as
birth control, immigration, healthcare, etc.)

Last but not least, we consider using the Twitter dataset and using the
insight we gained from the Liar dataset, perfom an analysis on the truthfulness
of tweets and look for any correlation between their spread and truthfulness.



# A list of internal milestones up until project milestone 2

## Week 1 - Gather information: augment the Liar dataset

- collect information about the source and type of the statement. We need to
  aggregate the information about the context available in the dataset in
  a hierarchy so we can perform both general queries (e.g. interview), or very
  specific queries (e.g. presidential announcement speech).

- categorize each statement as to whether it has an identified individual
  source (such a politician or news anchor) or whether it has an undefined
  or group source (such as a viral Facebook post or Tweet)

- cross-reference with Wikipedia/other soruces to add personal information
  (e.g. political affiliation) for statements where the source is an individual.


## Week 2 - NLP: continue looking for data

- add sentiment information to each statement. Requires NLP libraries.

- label each statement by whether it is affirmative or negative; might require
NLP, but it may be as simple as POS tagging as some tag sets may
already differentiate between negated verbs.

- find the semantic topic of each statement. This will require some research
as to the best method, but it might be sufficient to manually create topic
categories and associate categories with key words or to find how well are they
represented in each statement.

## Week 3 - Analysis

- start using the features we have augmented to perform queries
related to our research questions

- construct a plan as to the appropriate way to illustrate our findings

# Questions for TAs

One of our concerns is the size of the data set, which is only ~12,000 entries.
Is this data set size restrictive of the kind of analysis we hope to achieve?

We do not know exactly how well this data analysis relates to social good.
Should our approach be more prescriptive, as in trying to find strategies
people can use to detect certain untruthful types of statements, or descriptive
as in trying to find trends in data and letting the community make their own
conclusions?

We have already identified NLTK as a possible tool to assist in some of these
tasks. Are there other common libraries that might assist us? In particular, we
do not currently have a definite plan on how to discern a topic of a statement,
although we feel that this task is probably within the realm of possibility

