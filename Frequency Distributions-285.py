## 1. Simplifying Data ##

import pandas as pd
wnba = pd.read_csv("wnba.csv")
pd.options.display.max_rows = 200
pd.options.display.max_columns = 50
wnba.shape
print(wnba)

## 2. Frequency Distribution Tables ##

wnba = pd.read_csv('wnba.csv')
freq_distro_pos = wnba['Pos'].value_counts()
freq_distro_height = wnba['Height'].value_counts()
print(freq_distro_height)
print(freq_distro_pos)

## 3. Sorting Frequency Distribution Tables ##

wnba = pd.read_csv('wnba.csv')

age_ascending = wnba['Age'].value_counts().sort_index()
age_descending = wnba['Age'].value_counts().sort_index( ascending=False )

print(age_ascending)

## 4. Sorting Tables for Ordinal Variables ##

def make_pts_ordinal(row):
    if row['PTS'] <= 20:
        return 'very few points'  #0
    if (20 < row['PTS'] <=  80):
        return 'few points'    #1
    if (80 < row['PTS'] <=  150):
        return 'many, but below average' #2
    if (150 < row['PTS'] <= 300):
        return 'average number of points' #3
    if (300 < row['PTS'] <=  450):
        return 'more than average'  #4
    else:
        return 'much more than average' #5
    
wnba['PTS_ordinal_scale'] = wnba.apply(make_pts_ordinal, axis = 1)

pts_ordinal_desc = wnba['PTS_ordinal_scale'].value_counts().iloc[[4,3,0,2,1,5]]

## 5. Proportions and Percentages ##

wnba = pd.read_csv('wnba.csv')

age =wnba['Age'].value_counts(normalize =True).sort_index() * 100

proportion_25 = age[25] / 100
percentage_30 = age[30]
percentage_over_30 = age.loc[30:].sum()
percentage_below_23 =  age.loc[:23].sum()

## 6. Percentiles and Percentile Ranks ##

wnba = pd.read_csv('wnba.csv')
from scipy.stats import percentileofscore

percentile_rank_half_less= percentileofscore(a = wnba['Games Played'], score = 17, kind = 'weak')
percentage_half_more=  100 -  percentileofscore(a = wnba['Games Played'], score = 17, kind = 'weak')

## 7. Finding Percentiles with pandas ##

wnba = pd.read_csv('wnba.csv')
percentiles = wnba['Age'].describe(percentiles = [.5, .75, .95])
age_upper_quartile = percentiles['75%']
age_middle_quartile = percentiles['50%']
age_95th_percentile = percentiles['95%']

question1 = True
question2 = False
question3 = True

## 8. Grouped Frequency Distribution Tables ##

wnba = pd.read_csv('wnba.csv')
grouped_freq_table = wnba['PTS'].value_counts(normalize=True, bins = 10).sort_index( ascending =False)*100


## 9. Information Loss ##

import pandas as pd

k= [1,2,3,5,10,15,20,40]

for i in k :
    print(wnba['MIN'].value_counts(bins = i).sort_index())

## 10. Readability for Grouped Frequency Tables ##

wnba = pd.read_csv('wnba.csv')
intervals = pd.interval_range(start = 0, end = 600, freq = 60)
gr_freq_table_10 = pd.Series([0 for _ in range(10)], index = intervals)
for value in wnba['PTS']:
       for interval in intervals:
           if value in interval:
               gr_freq_table_10.loc[interval] += 1
               break