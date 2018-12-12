---
# You don't need to edit this file, it's empty on purpose.
# Edit theme's home layout instead if you wanna make some changes
# See: https://jekyllrb.com/docs/themes/#overriding-theme-defaults
layout: default
---

The advent of internet and the tremendous interconnectivity it created between
people comes with the downside of less checks for the validity of the
information. Nowdays everyone can have a website and share information, without
restrictions on the content quality.

Understanding the lying patterns in order to be able to detect lies is a very
difficult task. More research in natural language processing is needed, as well
as more psychological studies and data. In this project, we take a small step
in this direction, performing analysis of labelled political statements.

Politics is a very widely debated topic and it has a direct impact on people's
lives. Most of modern states in Europe and North America are based on
representative democracy, where vital decisions regarding the future of the
country are taken by representatives chosen thorugh vote. Trusting those people
is therefore vital, but not an easy task. There is a strong incentive of
deforming the truth or lying in the election campain to gain more votes or
during their mandate in order to keep a position of power.

Another related problem of the modern society are the fake news. Media
companies strive to create high impact news, not always reporting the truth.

In this project, we perform an analysis of the Liar dataset, a dataset of
political statements from [politifacts](http://www.politifact.com), looking
at cues for determining the truthfulness of a statement. We also experiment
with some machine learning models to get more insight into the data and
extrapolate it to new statements.

## The Liar dataset

A great challenge for deception detection is the lack of a large amount of
labelled data. We have used for our analysis the
[Liar dataset (Wang, 2017)](https://arxiv.org/abs/1705.00648).
This is, to the best of our knowledge, the one of the biggest labelled datasets
of statements labelled according to their truthfulness.

Unfortunately, while the dataset provides a lot of information regarding the
context of the statement, the reasons for which it received a certain truth
classification and 6 classes of truth, it has only about 12000 entries. The
relatively low number of entries, as well as the predominance of statements
from the US politics, does not allow for a good generalization. However, there
is enough data for an analysis of the lies in the US politics from the past
decade.


