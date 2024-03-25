# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 20:03:06 2024

@author: priyanka
"""

'''
4.) Telecall uses 4 centers around the globe to process customer order
forms. They audit a certain % of the customer order forms. Any error 
in order form renders it defective and must be reworked before 
processing. The manager wants to check whether the defective % varies 
by center. Please analyze the data at 5% significance level and help 
the manager draw appropriate inferences 
File: Customer OrderForm.csv
'''
import scipy.stats as stats
import statsmodels.api as sm
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

centers = pd.read_csv("C:/Data Set/CustomerOrderForm.csv")
centers.head(10)
#Applying Descriptive Statistics
centers.describe()

#Checking for Null Values
centers.isnull().sum()
centers[centers.isnull().any(axis=1)]

centers.info()
#Checking value counts in data
print(centers['Phillippines'].value_counts(),'\n',centers['Indonesia'].value_counts(),'\n',centers['Malta'].value_counts(),'\n',centers['India'].value_counts())

#Creating Contingency table
contingency_table = [[271,267,269,280],
                    [29,33,31,20]]
print(contingency_table)
 
#Calculating Expected Values for Observed data
stat, p, df, exp = stats.chi2_contingency(contingency_table)
print("Statistics = ",stat,"\n",'P_Value = ', p,'\n', 'degree of freedom =', df,'\n', 'Expected Values = ', exp)

#Defining Expected values and observed values
observed = np.array([271, 267, 269, 280, 29, 33, 31, 20])
expected = np.array([271.75, 271.75, 271.75, 271.75, 28.25, 28.25, 28.25, 28.25])

#Compare Evidences with Hypothesis using t-statictic
test_statistic , p_value = stats.chisquare(observed, expected, ddof = df)
print("Test Statistic = ",test_statistic,'\n', 'p_value =',p_value)

alpha = 0.05
print('Significnace=%.3f, p=%.3f' % (alpha, p_value))
if p_value <= alpha:
    print('We reject Null Hypothesis there is a significance difference between TAT of reports of the laboratories')
else:
    print('We fail to reject Null hypothesis')

