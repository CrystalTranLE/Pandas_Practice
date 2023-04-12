'''
date, revenue
2022-01-01, 1000
2022-01-02, 1200
2022-01-03, 800
2022-01-04, 1500
2022-01-05, 1300
2022-01-06, 1400
2022-01-07, 1100
2022-01-08, 900
2022-01-09, 1000
2022-01-10, 1200
2022-01-11, 1400
2022-01-12, 1600
2022-01-13, 1800
2022-01-14, 1500
2022-01-15, 1200
'''
import pandas as pd 
import numpy as np

df = pd.DataFrame({
    'date': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05', '2022-01-06', '2022-01-07', 
             '2022-01-08', '2022-01-09', '2022-01-10', '2022-01-11', '2022-01-12', '2022-01-13', '2022-01-14', '2022-01-15'],
    'revenue': [1000, 1200, 800, 1500, 1300, 1400, 1100, 900, 1000, 1200, 1400, 1600, 1800, 1500, 1200]
})

#Calculate mean revenue
mean_revenue = np.mean(df['revenue'])
print('The mean of daily revenue: ', mean_revenue)

#Calculate median revenue
median_revenue = np.median(df['revenue'])
print('The median of daily revenue: ', median_revenue)

#Calculate standard deviation
std_revenue = np.std(df['revenue'])
print('The standard deviation of daily revenue: ', std_revenue)