#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print "Number of people", len(enron_data)
print "Number of features", len(enron_data.itervalues().next())
print "Number of POI", sum(1 for person in enron_data.values() if person['poi'])
print "Total number of POI", 37-3+1
print "Total stock of James Prentice", enron_data['PRENTICE JAMES']['total_stock_value']
print "Email count from Wesley Colwell to poi", enron_data['COLWELL WESLEY']['from_this_person_to_poi']
print "Stock options exercised by Jeffrey K Skilling", enron_data['SKILLING JEFFREY K']['exercised_stock_options']
print "Total payments"
print "  Lay", enron_data['LAY KENNETH L']['total_payments']
print "  Skilling", enron_data['SKILLING JEFFREY K']['total_payments']
print "  Fastow", enron_data['FASTOW ANDREW S']['total_payments']
print "Number with quantified salary", sum(1 for person in enron_data.values() if person['salary'] != 'NaN')
print "Number with email", sum(1 for person in enron_data.values() if person['email_address'] != 'NaN')
print "Fraction with NaN for total payments", sum(1 for person in enron_data.values() if person['total_payments'] == 'NaN')*1.0/len(enron_data)*100.0, "%"
print "Fraction of POIs with NaN for total payments", sum(1 for person in enron_data.values() if person['poi'] and person['total_payments'] == 'NaN')*1.0/sum(1 for person in enron_data.values() if person['poi'])*100.0, "%"
print "Number of people+10", len(enron_data)+10
print "Number with NaN for total payments +10", sum(1 for person in enron_data.values() if person['total_payments'] == 'NaN')+10
print "Number of POI +10", sum(1 for person in enron_data.values() if person['poi'])+10
print "Number of PIO wth NaN for total payments", 10
