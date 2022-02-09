from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split as tts
from sklearn.feature_extraction.text import CountVectorizer

from sklearn.neighbors import KNeighborsClassifier as knc
from sklearn.tree import DecisionTreeClassifier as dtc
from sklearn.naive_bayes import CategoricalNB as cnb
from sklearn.svm import SVC as svc
from sklearn.ensemble import RandomForestClassifier as rfc
from sklearn.ensemble import VotingClassifier as vcl

#c_romance = pd.read_csv('Clean_Romance.csv').drop('Unnamed: 0', axis='columns')
c_love= pd.read_csv('Clean_Love.csv').drop('Unnamed: 0', axis='columns')
c_wisdom = pd.read_csv('Clean_Wisdom.csv').drop('Unnamed: 0', axis='columns')
#c_truth = pd.read_csv('Clean_Truth.csv').drop('Unnamed: 0', axis='columns')
c_god = pd.read_csv('Clean_God.csv').drop('Unnamed: 0', axis='columns')
#c_faith = pd.read_csv('Clean_Faith.csv').drop('Unnamed: 0', axis='columns')
c_humor = pd.read_csv('Clean_Humor.csv').drop('Unnamed: 0', axis='columns')
#c_writing = pd.read_csv('Clean_Writing.csv').drop('Unnamed: 0', axis='columns')
c_death = pd.read_csv('Clean_Death.csv').drop('Unnamed: 0', axis='columns')
#c_time = pd.read_csv('Clean_Time.csv').drop('Unnamed: 0', axis='columns')
c_knowledge = pd.read_csv('Clean_Knowledge.csv').drop('Unnamed: 0', axis='columns')
#c_science = pd.read_csv('Clean_Science.csv').drop('Unnamed: 0', axis='columns')

TYPE = 'Type'

# =============================================================================
# Categorize for this model
# =============================================================================
#c_romance[TYPE] = 'Love'
c_love[TYPE] = 'Love'

c_wisdom[TYPE] = 'Wisdom'
#c_truth[TYPE] = 'Wisdom'

c_god[TYPE] = 'Religion'
#c_faith[TYPE] = 'Religion'

c_humor[TYPE] = 'Wit'
#c_writing[TYPE] = 'Wit'

c_death[TYPE] = 'Death'
#c_time[TYPE] = 'Death'

c_knowledge[TYPE] = 'Knowledge'
#c_science[TYPE] = 'Knowledge'

# =============================================================================
# Making the master DF for this application
# =============================================================================
master_clean = pd.concat([c_love, c_wisdom, c_god, c_humor, c_death, c_knowledge],ignore_index=True).drop(['Genre', 'Category'], axis='columns')


# =============================================================================
# Beginning the Machine Learning
# =============================================================================
# =============================================================================
# Preparing the data
# =============================================================================
thing = CountVectorizer()
thing.fit_transform(master_clean.Quote)
vectorized = CountVectorizer().fit_transform(master_clean.Quote)
train_x, test_x, train_y, test_y = tts(vectorized, master_clean.Type, test_size=0.30, random_state=42)


# =============================================================================
# knearest nighbor classifier. Tried playing around with nneighbors, seems about optimal between 15-20. At best still about ~45%
# =============================================================================
model_knc = knc(n_neighbors = 15).fit(train_x.toarray(), train_y)
score_knc = model_knc.score(test_x.toarray(), test_y)


# =============================================================================
# Decision tree classifier, hoping for better results than knearest. 
# And indeed off the bat got 57%. Not great, but I can make an ensemble if I get decent results everywhere
# Tried adjusting hyperparameter splitter to random, not as good as best
# =============================================================================
model_dtc = dtc().fit(train_x, train_y)
score_dtc = model_dtc.score(test_x, test_y)


# =============================================================================
# Going to try Naive Bayes, tried playing with test_size with 2 other models, seems to run optimal at 30%
# Can't get score method to work, see note
# =============================================================================
#model_cnb = cnb().fit(train_x.toarray(), train_y)

#Unable to get a score prediction from cnb, IndexError: index 1 is out of bounds for axis 1 with size 1
#score_cnb = model_cnb.score(test_x.toarray(), test_y)

# =============================================================================
# Will try SVC, hoping for better success 
# Best so far, off the bat with 62.5% Accuracy, however, model is quite slow
# =============================================================================
model_svc = svc().fit(train_x, train_y)
score_svc = model_svc.score(test_x, test_y)


# =============================================================================
# Now to try random forest, last model before making an ensemble
# And lo, best model out the gate with 66.23%. 
# =============================================================================
model_rfc = rfc().fit(train_x, train_y)
score_rfc = model_rfc.score(test_x, test_y)


# =============================================================================
# Ensemble, I'm going to assume that naive bayes is average, which would mean roughly 56% accuracy. Will use that as float for weight
# Decided to abandon cnb for now, something quite costly in voncerting to array, perhaps will re-instate if able to obtain score
# =============================================================================
model_hard_vcl = vcl(estimators=[
    #('knc', knc(n_neighbors=20)),
    ('dtc', dtc()),
    #('cnb', cnb()),
    ('svc', svc()),
    ('rfc', rfc()),
    ],
    voting = 'hard').fit(train_x, train_y)

score_hard_vote = model_hard_vcl.score(test_x, test_y)

"""
model_soft_vcl = vcl(estimators=[
    #('knc', knc(n_neighbors=20)),
    ('dtc', dtc()),
    #('cnb', cnb()),
    ('svc', svc()),
    ('rfc', rfc()),
    ],
    voting = 'soft').fit(train_x, train_y)
score_soft_vote = model_soft_vcl.score(test_x, test_y)
"""
# =============================================================================
# Soft gives model, but no score, since probability=false, will have to investigate
# Attempted the runs while including knc, but knc is relatively bad, at 43% accuray, and I ended up with 65.45% for hard vote, less than solo rfc
# Will drop knc from the ensemble, use the other 3 models which range from ~57-67. 
# After seeing if this results better, will see if changing train test split from 0.30 will affect
# =============================================================================


# =============================================================================
# Dropped KNC, gave about a +1.5% performance, will play with test_size before dropping next worst predictor i.e. Naive Bayes
# =============================================================================

the_quote = 'Abandon hope, all yee who enter here'
to_be_predicted = thing.transform([the_quote])

rfc_pred = model_rfc.predict(to_be_predicted)
vot_pred = model_hard_vcl.predict(to_be_predicted)

print(f'rfc predcition: {rfc_pred}, \nvoting prediction: {vot_pred}')












