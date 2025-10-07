Models can be divided in two broad categories: *supervised* and *unsupervised*


### Supervised models

They can achieve different types of tasks that may be divided into *regression*, *classification* and *ranking*

#### Regression models
Regression models can be used when the output is a continuous value, such as a price or number of complaints

#### Classification models
They predict categories of classes. If there are only two possible outcomes, the task is known as "binary classification". The classificaiton tipically assigns a score to each category, and then chooses the class with the highest score.
It's also possible to define a threshold to define inclusion into a class.

#### Ranking models
Ranking problems are about ordering items, such as search results. A ranking task may be approached as a regression or classification task if the items are considered independent (pointwise approach).  
It can also learn to compare two items against each other (pairwise) and compute which ones ranks higher. Lastly, it can be trained on a whole list of items (listwise) and optimize for specific ranking metrics.


#### Building a ML model
It's an iterative process in which we can identify some steps:

* definition of the business case: what to predict (target), what data (features) can be used for that, what success metric we are targeting
* data preparation: extraction, cleaning, descriptive analysis, building labels, feature engineering (aggregation, binning, embeddings, etc... )
* modeling: splitting of the data between training/testing/validation sets, definition of baseline, model selection
* deployment: includes monitoring, pre-deploy shadowing, A/B testing, retraining 
