# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 19:08:58 2024

@author: priyanka
"""

'''
2.) A hospital wants to determine whether there is any difference 
in the average Turn Around Time (TAT) of reports of the laboratories
 on their preferred list. They collected a random sample and recorded 
 TAT for reports of 4 laboratories. TAT is defined as sample collected to report dispatch. 

Analyze the data and determine whether there is any difference in 
average TAT among the different laboratories at 5% significance level. 
File: LabTAT.csv 
'''
import scipy.stats as stats
import statsmodels.api as sm
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
labtat = pd.read_csv("C:/Data Set/LabTat.csv")
labtat.head()
labtat.describe()
#Checking for Null Values

labtat.isnull().sum()

#Checking for Duplicate Values
labtat[labtat.duplicated()].shape

labtat[labtat.duplicated()]
labtat.info()

#Plotting the data
plt.subplots(figsize = (16,9))
plt.subplot(221)
plt.boxplot(labtat['Laboratory_1'])
plt.title('Laboratory 1')
plt.subplot(222)
plt.boxplot(labtat['Laboratory_2'])
plt.title('Laboratory 2')
plt.subplot(223)
plt.boxplot(labtat['Laboratory_3'])
plt.title('Laboratory 3')
plt.subplot(224)
plt.boxplot(labtat['Laboratory_4'])
plt.title('Laboratory 4')
plt.show()

plt.subplots(figsize = (9,6))
plt.subplot(221)
plt.hist(labtat['Laboratory_1'])
plt.title('Laboratory 1')
plt.subplot(222)
plt.hist(labtat['Laboratory_2'])
plt.title('Laboratory 2')
plt.subplot(223)
plt.hist(labtat['Laboratory_3'])
plt.title('Laboratory 3')
plt.subplot(224)
plt.hist(labtat['Laboratory_4'])
plt.title('Laboratory 4')
plt.show()

plt.figure(figsize = (8,6))
labels = ['Lab 1', 'Lab 2','Lab 3', 'Lab 4']
sns.distplot(labtat['Laboratory_1'], kde = True)
sns.distplot(labtat['Laboratory_2'],hist = True)
sns.distplot(labtat['Laboratory_3'],hist = True)
sns.distplot(labtat['Laboratory_4'],hist = True)
plt.legend(labels)

#Plotting Q-Q plot to check whether the distribution follows normal distribution or not
sm.qqplot(labtat['Laboratory_1'], line = 'q')
plt.title('Laboratory 1')
sm.qqplot(labtat['Laboratory_2'], line = 'q')
plt.title('Laboratory 2')
sm.qqplot(labtat['Laboratory_3'], line = 'q')
plt.title('Laboratory 3')
sm.qqplot(labtat['Laboratory_4'], line = 'q')
plt.title('Laboratory 4')
plt.show()

#Compare Evidences with Hypothesis using t-statictic
test_statistic , p_value = stats.f_oneway(labtat.iloc[:,0],labtat.iloc[:,1],labtat.iloc[:,2],labtat.iloc[:,3])
print('p_value =',p_value)

alpha = 0.05
print('Significnace=%.3f, p=%.3f' % (alpha, p_value))
if p_value <= alpha:
    print('We reject Null Hypothesis there is a significance difference between TAT of reports of the laboratories')
else:
    print('We fail to reject Null hypothesis')

'''
Significnace=0.050, p=0.000
We reject Null Hypothesis there is a significance difference between TAT of reports of the laboratories
'''