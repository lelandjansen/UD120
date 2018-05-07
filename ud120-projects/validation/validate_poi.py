#!/usr/bin/python


"""
    Starter code for the validation mini-project.
    The first step toward building your POI identifier!

    Start by loading/formatting the data

    After that, it's not our code anymore--it's yours!
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### first element is our labels, any added elements are predictor
### features. Keep this the same for the mini-project, but you'll
### have a different feature list when you do the final project.
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### it's all yours from here forward!  
from sklearn.cross_validation import train_test_split
features_train, features_test, labels_train, labels_test = \
        train_test_split(features, labels, test_size=0.30, random_state=42)
from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier()
clf.fit(features_train, labels_train)
print "Accuracy: %f" % clf.score(features_test, labels_test)
print "POI in test: %d" % sum(clf.predict(features_test))
print "People in test set: %d" % len(labels_test)
print "Accuracy if no POIs: %f" % clf.score(features_test,
                                            [0] * len(features_test))
import numpy as np
print "True positives: %d" % sum(np.logical_and(clf.predict(features_test),
                                                labels_test))
from sklearn import metrics
print "Precision: %f" % metrics.precision_score(labels_test,
                                                clf.predict(features_test))
print "Recall: %f" % metrics.recall_score(labels_test,
                                          clf.predict(features_test))
true_positives = sum(np.logical_and(
    [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]))
print "True positives: %d" % true_positives
true_negatives = sum(np.logical_and(
    np.logical_not([0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1]),
    np.logical_not([0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0])))
print "True negatives: %d" % true_negatives
false_positives = sum(np.logical_and(
    [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1],
    np.logical_not([0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0])))
print "False positives: %d" % false_positives
false_negatives = sum(np.logical_and(
    np.logical_not([0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1]),
    [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]))
print "False negatives: %d" % false_negatives
print "Precision: %f" % (float(true_positives) /float(true_positives + false_positives))
print "Recall: %f" % (float(true_positives) /float(true_positives + false_negatives))
