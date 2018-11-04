# Features of Lies

# Abstract
Automatic detection of false claims is currently a challenging NLP/ML task for multiple reasons, including the lack of classified data and the enormous incentive differential between different contexts. It is difficult to manually generate lies, as the incentive lie is difficult to manufacture. The Liar Dataset, provided by UC Santa Barbara, offers one such set of tagged data which gathers statements from a setting where there is high incentive to lie. This data set contains samples of political statements, as well as their truth ratings using the PolitiFacts truth meter. Our goal is to not to make a general model to predict fake news, but rather to see what indicators there are underlying within a given statement that may influence its likelihood to be true. In particular, we note that there are many aspects underlying a snippet of text for which there exist sophisticated NLP solutions in analyzing – sentiment, semantic content and grammatical affirmation/negation. In addition to analyzing how truth of a claim relates to other features in the Liar Dataset, we wish to analyze how the truth of a claim relates to some of the underlying features we can find using NLP libraries such as NLTK. This kind of analysis can inform the public on which media platforms or topics of discourse most warrant skepticism of claims as well as which ones are generally more reliable. We also believe this kind of analysis can help alert individuals to identify common tactics such as denial and fear mongering.

# Research questions
•	How do truthfulness of claims relate to other recorded features, such as message context/setting, identity of speaker, political affiliation of the speaker, or political position of the speaker at the time of the statement?
•	How do truthfulness of claims relate to underlying features of the claim, such as its topic or sentiment?
•	What proportion of the dataset is composed of affirmative statements versus negative statements? Is one more likely to be false than the other?
•	For a given truth classification, are there differences in the topics that democrats discuss versus republicans? i.e., are democrat lies more likely to be about certain topics than republican lies and vice verse?


# Dataset
This analysis will use the Liar data set because it is imperative to use a data set that already has already been classified by truthfulness since all of our research questions relate to truthfulness of claims. Importantly, this data set contains close to uniform representation of statements from all areas of the truth spectrum, meaning that we are not simply analyzing lies, but also that we have examples of truthful statements as well. This is important, because for many of the features we wish to analyze, we will want to make some comparison between a feature's prominence in a lie versus its prominence overall.

The data set contains many features we are immediately interested in, such as speaker and context. Much of the initial phases of our project will involve using these features to construct new features to analyze.

For named speakers, such as politicians, we believe we can cross-reference with their Wikipedia entries in order to find out their political affiliation and their political position. This would allow us to compare political affiliations or different political positions. For contexts, we believe we can group certain contexts into categories, such as live speeches, social media statements, interviews, etc.

We also think that we can find ways use the statement itself to construct interesting features such as sentiment and topic. Currently, we plan to use NLTK for sentiment analysis, but will need to do research to find libraries or implementations that may help us categorize statements by their topic (such as birth control, immigration, healthcare, etc.)


# A list of internal milestones up until project milestone 2

Gather data – load the dataset
Group vs. individual augmentation – categorize each statement as to whether it has an identified individual source (such a politician or news anchor) or whether it has an undefined or group source (such as a viral Facebook post or Tweet)
Affiliation augmentation – cross-reference to add political affiliation/position for statements where the speaker is an individual; requires web querying and html parsing
Context grouping – find a way to categorize the contexts by useful groupings, such as TV, online, live, interview, etc.
Sentiment augmentation – label each statement by its sentiment; requires NLP libraries that can help perform this task 
Grammatical negation augmentation – label each statement by whether it is grammatically affirmative or negative; requires NLP libraries that can help perform this task, but it may be as simple as POS tagging as some tag sets may already differentiate between negated verbs
Semantic augmentation – find a way to discern the topic of discourse from a statement and label each statement by that; this will require some research as to the best method, but it might be sufficient to manually create topic categories and associate categories with key words
Initial analysis steps – Use the features we have augmented to perform queries related to our research questions
Ideas on visualization – Construct a plan as to the appropriate way to illustrate our findings

# Questions for TAs

One of our concerns is the size of the data set, which is only ~12,000 entries. Is this data set size restrictive of the kind of analysis we hope to achieve?
We do not know exactly how well this data analysis relates to social good. Should our approach be more prescriptive, as in trying to find strategies people can use to detect certain untruthful types of statements, or descriptive as in trying to find trends in data and letting the community make their own conclusions?

We have already identified NLTK as a possible tool to assist in some of these tasks. Are there other common libraries that might assist us? In particular, we do not currently have a definite plan on how to discern a topic of a statement, although we feel that this task is probably within the realm of possibility