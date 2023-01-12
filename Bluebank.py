# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 12:01:10 2022

@author: Vyankatesh
"""

import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#method 1 to read .json data
json_file=open ('loan_data_json.json')
data = json.load(json_file)

#method 2 to read .json data
with open ('loan_data_json.json') as json_file:
    data=json.load(json_file)
    
#Transform to dataframe
loandata = pd.DataFrame(data)

#Finding unique values for the purpose column

loandata['purpose'].unique()

#Describe the data
loandata.describe()

#Describe data for the specific column
loandata['int.rate'].describe()
loandata['fico'].describe()
loandata['dti'].describe()

# using EXP to get annual income
income = np.exp(loandata['log.annual.inc'])
loandata['annualincome'] = income


# fico=250

# if fico>=300 and fico<400:
#     ficocat='Very Poor'
# elif fico>=400 and fico<600:
#     ficocat='poor'
# elif fico>=601 and fico<660:
#     ficocat='Fair'
# elif fico>=660 and fico<700:
#     ficocat='Good'
# elif fico>=700:
#     ficocat='Excellent'
# else:
#     ficocat= 'Unknown'
# print(ficocat)

#apply the above conditions of IF to a column

ficocat = []
length = len(loandata)

for x in range(0,length):
    category = loandata['fico'][x]
    try:
        if category>=300 and category<400:
            cat='Very Poor' 
        elif category>=400 and category<600:
            cat='poor'
        elif category>=601 and category<660:
            cat='Fair'
        elif category>=660 and category<700:
            cat='Good'
        elif category>=700:
            cat='Excellent'
        else:
            cat= 'Unknown'
    except:
        cat= 'Unknown'
        
    ficocat.append(cat)
    
#converting to series

ficocat = pd.Series(ficocat)

# adding this new column to loan data

loandata['fico.category']= ficocat

#While loops : how it works
# i =1
# while i <10:
#     print(i)
#     i += 1
    


# Testing Error

# ficocat = []
# length = len(loandata)

# for x in range(0,length):
#     category = 'red'
#     try:
        
#         if category>=300 and category<400:
#             cat='Very Poor' 
#         elif category>=400 and category<600:
#             cat='poor'
#         elif category>=601 and category<660:
#             cat='Fair'
#         elif category>=660 and category<700:
#             cat='Good'
#         elif category>=700:
#             cat='Excellent'
#         else:
#             cat= 'Unknown'
#     except:
#         cat='Error-unknown'
#     ficocat.append(cat)

# ficocat = pd.Series(ficocat)

# loandata['fico.category']= ficocat



# Another form of conditional statement :
#df.loc as conditional statements
# df.loc [df[columnname] condition, newcolumnname] = 'value if the condition is met'

#  for interest rates, a new column is wanted, ratre >0.12 then high, else low


loandata.loc[loandata['int.rate'] > 0.12, 'int.rate.type'] = 'High'
loandata.loc[loandata['int.rate'] <= 0.12, 'int.rate.type'] = 'Low'

# No of loans or rows by fico category 

catplot = loandata.groupby(['fico.category']).size()
catplot.plot.bar(color='green', width = 0.1)
plt.show()
    
purposecount = loandata.groupby(['purpose']).size()
purposecount.plot.bar(color='red', width = 0.3)
plt.show()                

#  Scatter plot:

ypoint = loandata['annualincome']
xpoint = loandata['dti']
plt.scatter(xpoint, ypoint, color = 'red')
plt.show()

# Writing to CSV

loandata.to_csv('loan_cleaned.csv', index = True)


































    
