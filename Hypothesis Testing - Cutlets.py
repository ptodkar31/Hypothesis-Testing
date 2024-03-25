# -*- coding: utf-8 -*-
"""
Created on Thu Mar 5 18:56:43 2024

@author: priyanka
"""

import scipy.stats as stats
import statsmodels.api as sm
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
'''
We need to check whether the mean of both samples are different and
Is there any significance difference between the two samples?
Step 1
Make two Hypothesis one contradicting to other
Null Hypothesis is want we want to prove
Null Hypothesis: 
Alternative Hypthosis: 
Step 2
Decide a cut-off value
Significance 5%
alpha = 0.05
As it is a two-tailed test
alpha/2 = 0.025
Step 3
Collect evidence
'''
cutlets = pd.read_csv("C:/Data Set/Cutlets.csv")
cutlets.head(10)
cutlets.describe()
#Checking for NULL values
cutlets.isnull().sum()
#Checking for the duplicates
cutlets[cutlets.duplicated()].shape
cutlets[cutlets.duplicated()]

#Checking the data type
cutlets.info()

#Plotting the data
plt.subplots(figsize = (9,6))
plt.subplot(121)
plt.boxplot(cutlets['Unit A'])
plt.title('Unit A')
plt.subplot(122)
plt.boxplot(cutlets['Unit B'])
plt.title('Unit B')
plt.show()

plt.subplots(figsize = (9,6))
plt.subplot(121)
plt.hist(cutlets['Unit A'], bins = 15)
plt.title('Unit A')
plt.subplot(122)
plt.hist(cutlets['Unit B'], bins = 15)
plt.title('Unit B')
plt.show()

plt.figure(figsize = (8,6))
labels = ['Unit A', 'Unit B']
sns.distplot(cutlets['Unit A'], kde = True)
sns.distplot(cutlets['Unit B'],hist = True)
plt.legend(labels)

#Plotting Q-Q plot to check whether the distribution follows normal distribution or not
sm.qqplot(cutlets["Unit A"], line = 'q')
plt.title('Unit A')
sm.qqplot(cutlets["Unit B"], line = 'q')
plt.title('Unit B')
plt.show()

#Compare Evidences with Hypothesis using t-statistics
statistic , p_value = stats.ttest_ind(cutlets['Unit A'],cutlets['Unit B'], alternative = 'two-sided')
print('p_value=',p_value)

'''
Compare p_value with '
 '(Significane Level)
If p_value is 
 '
 ' we failed to reject Null Hypothesis because of lack of evidence
If p_value is = '
 ' we reject Null Hypothesis
interpreting p-value
'''
alpha = 0.025
print('Significnace=%.3f, p=%.3f' % (alpha, p_value))
if p_value <= alpha:
    print('We reject Null Hypothesis there is a significance difference between two Units A and B')
else:
    print('We fail to reject Null hypothesis')

'''
Hence, We fail to reject Null Hypothesis because of lack of evidence, there is no significant
difference between the two samples
'''

