# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 09:38:58 2024

@author: Priyanka
"""


import pandas as pd
import numpy as  np
import scipy
from scipy import stats
import statsmodels.stats.descriptivestats as sd
import statsmodels.stats.weightstats

"""
1 sample sign test
for given dataset check wweather the scores are either equal or less than 80
H0=scores are either equal or less than 80
H1=scores are not equal and greater than 80
whenever there is single sample and data is not normal
"""
marks=pd.read_csv("C:\Data Set\hypothesis_datasets\Signtest.csv")
#Normal QQ plot
import pylab
stats.probplot(marks.Scores,dist='norm',plot=pylab)
#Data is not normal
#H0=data is normal
#H1=Data is not normal
stats.shapiro(marks.Scores)
"""
p_value is 0.024>0.005 p is high null fly
Decision:Data is not normal
Let us check the distribution of the data
"""
marks.Scores.describe()
#1 sample sign test
sd.sign_test(marks.Scores,mu0=marks.Scores.mean())
import pandas as pd
import numpy as np

###############1-Sample Z- Test################################
#importing the data
fabric=pd.read_csv("C:\Data Set\hypothesis_datasets\Fabric_data.csv")
#calculating the normality  test

print(stats.shapiro(fabric))
#0.1460
#Calculating the mean

np.mean(fabric)

#ztest
#parameters in z-test,value is mean of the data
ztest,pval=stats.ztest(fabric,x2=None,value=150)

print(float(pval))
#p-value=7.156e-06 < 0.05 so p low null go

############Mann-Whiteny Test############################
#Vehicles with and without adddicitve
#Ho:fuel addictive dose not impacty performance
#H1:fuel addictie does impact the performance

fuel=pd.read_csv("C:\Data Set\hypothesis_datasets\mann_whitney_additive.csv")
fuel

fuel.columns="Without_addictive","with_addictive"

#Normality test
#H0:data is normal

print(stats.shapiro(fuel.Without_addictive))#p high fly
print(stats.shapiro(fuel.Without_addictive))#p low null go

#withput_addictive is normal
#with addictive is not normal
#When two samples are not normal then meanwhiteney test
#non-parametric Test Case
#Mann-Whitney test

scipy.stats.mannwhitneyu(fuel.without_addictive,fuel.with_addictive)

#p value= 0.5011984109 so p high null fly
#Ho:fuel addictive does not impact the performance

############################# Paired T-Test #################################

#When two features are normal then paired T test
#A univariate test that test fi=or significant difference between mof suppilers eans 

sup=pd.read_csv("C:\Data Set\hypothesis_datasets\paired2.csv")
sup.describe()

#Ho:There is no significant difference between means of suppliers of A ar
#Ha: There is significant difference between means of suppliers of A and E
#Normality Test-#Shapiro Test

stats.shapiro(sup.SupplierA)
stats.shapiro(sup.SupplierB)

#Data are normal

import seaborn as sns
sns.boxplot(data=sup)

#Assuming ther external conditions are same for both the samples
#Paired T Test

ttest,pval=stats.ttest_rel(sup['SupplierA'],sup['SupplierB'])
print(pval) #0.0<0.5  so p no null go

######################## 2-Sample T-Test ######################################
#Load the data
prom=pd.read_excel()
prom
#Ho:InterestRateWaiver < StandardPromotion
#Ha:InteresrRateWaiver > StandardPromotion

prom.columns='InterestRateWaiver','StandardPromotion'

#Normality Test
stats.shapiro(prom.InterestRateWaiver)  #Shapiro Test
print(stats.shapiro(prom.StandardPromotion))

#Data are Normal
#Variance Test

help(scipy.stats.levene)

#H0 = Both columns have equal variances
#H1=Both Columns have Equal Varience
scipy.stats.levene(prom.InteresrRateWaiver, prom.StandardPromotion)

#p value =0.287 > 0.05 so p high null fly  => Equal variances

#2 sample T test
scipy.stats.ttest_ind(prom.InteresrRateWaiver, prom.StandardPromotion)
help(scipy.stats.ttest_ind)

#H0= equal means
#Ha= unequal means
#p-val: 0.024<0.05


#################### One-Way ANOVA ####################################

"""
A marketing organization outsources their back-office operations
 to three different suppliers. The contracts are up for renewal
 and the CMO wants to determine whether they should renew contracts 
 with all suppliers or any specific supplier. CMO want to renew the 
 contract of supplier with the least transaction time. CMO will renew
 all contracts if the performance of all suppliers is similar
"""

con_renewal=pd.read_excel("C:\Data Set\hypothesis_datasets\ContractRenewal_Data(unstacked).xlsx")
con_renewal
con_renewal.columns=" SupplierA","SupplierB","SupplierC"

#H0= all the 3 suppliers have equal mean transaction time
#H1= all the 3 suppliers have notequal mean transaction time 
#Normality twst

stats.shapiro(con_renewal.SupplierA)

#pvalue=0.89>0.005 Supplier A is normal

stats.shapiro(con_renewal.SupplierB)

stats.shapiro(con_renewal.SupplierC)
# 0.57>0.005 SupplierC is Normal

#Variance Test
help(scipy.stats.levene)

#All 3 supplier are being cheacked for Variable
scipy.stats.levene(con_renewal.SupplierA,con_renewal.SupplierB,con_renewal.SupplierC)
#the Levene test tests the null hypothesis
#that all input samples are from  populationswith equal variances
#pvalue =0.777>0.005 ,p is high null fly
#H0= All the input sample are from population with equal variances
#


#one way ANOVA
F,p=stats.f_oneway(con_renewal.SupplierA,con_renewal.SupplierB,con_renewal.SupplierC) 

#p value
p
# P High Null fly
#all the 3 suppliers have equal mean transaction time

###################### 2 Proportional Test  #####################################

import numpy as np
two_prop_test =pd.read_excel("C:\Data Set\hypothesis_datasets\JohnyTalkers.xlsx")
from statsmodels.stats.proportion import proportions_ztest

tab1=two_prop_test.Person.value_count()
tab1
tab2=two_prop_test.Drinks.value_count()
tab2


#Crosstable 

pd.crosstab(two_prop_test.Person, two_prop_test.Drinks)

count=np.array([58,152])
nobs=np.array([480,740])

stats, pval=proportions_ztest(count, nobs, alternative="two-sided")
print(pval)
#pvalue= 0.000

stats, pval=proportions_ztest(count, nobs, alternative="larger")
print(pval)
#pvalue=0.999



############################# Chi Square Test ##########################

Bahaman=pd.read_excel("C:\Data Set\hypothesis_datasets\Bahaman.xlsx")
Bahaman
count=pd.crosstab(Bahaman["Defective"], Bahaman["Country"])
count
Chisquares_results=scipy.stats.chi2_contingency(count)

Chi_square=[['Test Statistic','P-values'],[Chisquares_results[0],Chisquares_results[1]]]
Chi_square

"""
you use chi2_contigency when you want to test 
whether two or more groups have the same distribution
"""

#H0=null Hypothesis:the two groups have
#no sigificant differences
#since p=0.63>0.05 hence H0 is true

