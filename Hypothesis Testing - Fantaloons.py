# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 20:20:05 2024

@author: priyanka
"""

'''
5.) Fantaloons Sales managers commented that % of males 
versus females walking into the store differ based on day of 
the week. Analyze the data and determine whether there is 
evidence at 5 % significance level to support this hypothesis
 
File: Fantaloons.csv
'''
import scipy.stats as stats
import statsmodels.api as sm
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
Fantaloons = pd.read_csv("C:/Data Set/Fantaloons.csv")
Fantaloons.head()
Fantaloons.describe()

Weekdays_value=Fantaloons['Weekdays'].value_counts()
Weekend_value=Fantaloons['Weekend'].value_counts()
print(Weekdays_value,Weekend_value)

#we do the cross table 
tab = Fantaloons.groupby(['Weekdays', 'Weekend']).size()
count = np.array([280, 520]) #How many Male and Female
nobs = np.array([400, 400]) #Total number of Male and Female are there 

stat, pval =proportion_ztest(count, nobs,alternative='two-sided')
#Alternative The alternative hypothesis can be either two-sided or one of the one- sided tests
#smaller means that the alternative hypothesis is prop < value
#larger means prop > value.
print('{0:0.3f}'.format(pval))
# two. sided -> means checking for equal proportions of Male and Female 
# p-value < 0.05 accept alternate hypothesis i.e.
# Unequal proportions 

stat, pval =proportion_ztest(count, nobs,alternative='larger')
print('{0:0.3f}'.format(pval))