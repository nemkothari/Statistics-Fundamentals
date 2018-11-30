## 1. Comparing Frequency Distributions ##

rookies = wnba[wnba['Exp_ordinal'] == 'Rookie']
little_xp = wnba[wnba['Exp_ordinal'] == 'Little experience']
experienced = wnba[wnba['Exp_ordinal'] == 'Experienced']
very_xp = wnba[wnba['Exp_ordinal'] == 'Very experienced']
veterans =  wnba[wnba['Exp_ordinal'] == 'Veteran']

rookie_distro = rookies['Pos'].value_counts()
little_xp_distro = little_xp['Pos'].value_counts()
experienced_distro = experienced['Pos'].value_counts()
very_xp_distro = very_xp['Pos'].value_counts()
veteran_distro = veterans['Pos'].value_counts()

## 2. Grouped Bar Plots ##

import seaborn as sns
sns.countplot(x = 'Exp_ordinal', hue = 'Pos', data = wnba,
              order = ['Rookie', 'Little experience', 'Experienced', 'Very experienced', 'Veteran'],
              hue_order = ['C', 'F', 'F/C', 'G', 'G/F']
             )

## 3. Challenge: Do Older Players Play Less? ##

import seaborn as s
sns.countplot(x='age_mean_relative' , hue ='min_mean_relative' ,data=wnba)
result = 'rejection'

## 4. Comparing Histograms ##

import matplotlib.pyplot as plt

wnba[wnba['Age'] >= 27]['MIN'].plot.hist(legend=True,histtype = 'step', label = 'Old' )
wnba[wnba['Age']<27]['MIN'].plot.hist(legend=True,histtype = 'step', label = 'Young' )
plt.axvline(497 , label='Average')
plt.legend()
plt.show()


## 5. Kernel Density Estimate Plots ##

wnba[wnba['MIN'] >=27]['MIN'].plot.kde(legend=True, label="Old")
wnba[wnba['MIN'] < 27]['MIN'].plot.kde(legend=True, label="Young")
plt.axvline(497 ,label="Average")
plt.show()

## 7. Strip Plots ##

import seaborn as sns

sns.stripplot(x= 'Pos' ,y= 'Weight', data=wnba, jitter=True)
plt.show()

## 8. Box plots ##

sns.boxplot(x='Pos' , y= 'Weight', data=wnba) 
plt.show()

## 9. Outliers ##

iqr = 29 - 22
lower_bound =  22  - 1.5*(iqr)
upper_bound =  1.5*(iqr) + 29


outliers_high  =  sum(wnba['Games Played'] > upper_bound ) 

outliers_low  =  sum(wnba['Games Played'] < lower_bound ) 

sns.boxplot(wnba['Games Played']  , whis = 4,
              orient = 'vertical', width = .15)