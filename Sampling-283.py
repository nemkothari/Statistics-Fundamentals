## 3. Populations and Samples ##

question1 = 'population'
question2 = 'population'
question3 = 'sample'
question4 = 'population'
question5 = 'sample'

## 4. Sampling Error ##

import pandas as pd
wnba = pd.read_csv('wnba.csv')
wnba.head()
wnba.tail()
wnba.shape
parameter = wnba["Games Played"].max()
sample = wnba["Games Played"].sample(n=30, random_state = 1)
statistic = sample.max()

sampling_error = parameter -statistic

## 5. Simple Random Sampling ##

import pandas as pd
import matplotlib.pyplot as plt

wnba = pd.read_csv('wnba.csv')
result_mean=[]
for i in range(100):
    sample = wnba["PTS"].sample(10,random_state=i )
    result_mean.append(sample.mean())
    
plt.scatter(range(1,101), result_mean)
plt.axhline( wnba['PTS'].mean())
plt.show()
    
     
        
    
    
    


## 7. Stratified Sampling ##

wnba['Pts_per_game'] = wnba['PTS'] / wnba['Games Played']

# Stratifying the data in five strata
stratum_G = wnba[wnba.Pos == 'G']
stratum_F = wnba[wnba.Pos == 'F']
stratum_C = wnba[wnba.Pos == 'C']
stratum_GF = wnba[wnba.Pos == 'G/F']
stratum_FC = wnba[wnba.Pos == 'F/C']

points_per_position = {}
for stratum, position in [(stratum_G, 'G'), (stratum_F, 'F'), (stratum_C, 'C'),(stratum_GF, 'G/F'), (stratum_FC, 'F/C')]:
    sample = stratum['Pts_per_game'].sample(10, random_state = 0) 
    # simple random sapling on each stratum
    points_per_position[position] = sample.mean()
    
position_most_points = max(points_per_position, key = points_per_position.get)

## 8. Proportional Stratified Sampling ##

first = wnba[ wnba['Games Played'] <13]
second =  wnba[ (wnba['Games Played'] < 23 ) &  ( wnba['Games Played']  > 12 )] 
third = wnba[ wnba['Games Played'] > 22]
samp =[]
for i in range(100):
    one= first['PTS'].sample(n=1,random_state=i)
    two = second['PTS'].sample(n=2,random_state=i)
    three= third['PTS'].sample(n=7,random_state=i)
    final_sample = pd.concat([one, two, three])
    samp.append(final_sample.mean())

print(samp)
plt.scatter(range(1,101) , samp)
plt.axhline(wnba['PTS'].mean())
plt.show()
     

## 10. Cluster Sampling ##

clusters = pd.Series(wnba['Team'].unique()).sample(4, random_state = 0)
sample = pd.DataFrame()

for cluster in clusters:
    data_collected = wnba[wnba['Team'] == cluster]
    sample = sample.append(data_collected)
    
sampling_error_height = wnba['Height'].mean() - sample['Height'].mean()
sampling_error_age = wnba['Age'].mean() - sample['Age'].mean()
sampling_error_BMI = wnba['BMI'].mean() - sample['BMI'].mean()
sampling_error_points = wnba['PTS'].mean() - sample['PTS'].mean()

