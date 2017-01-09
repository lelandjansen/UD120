#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
data_dict.pop("TOTAL", 0)
data = featureFormat(data_dict, features)


### your code below


salary_bonus = []
for point in data:
    salary = point[0]
    bonus = point[1]
    # if 5000000 < bonus and 1000000 < salary:
    #     print salary, bonus
    # salary_bonus.append((salary, bonus))
    matplotlib.pyplot.scatter( salary, bonus )

# salary_bonus.sort(key=lambda tup: tup[1])
# print salary_bonus

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()