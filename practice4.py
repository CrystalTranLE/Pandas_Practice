import pandas as pd
import matplotlib.pyplot as plt
from statistics import mean

##Practice 4:
df = pd.DataFrame({
    'customer_id': [1001, 1002, 1001, 1003, 1002, 1001, 1004, 1001, 1002, 1005, 1006, 1007, 1001, 1002],
    'date': ['2022-01-01',  '2022-01-01',  '2022-01-03',  '2022-01-04',  '2022-01-05',  '2022-01-07',  '2022-01-08',  '2022-01-09',  
             '2022-01-10', '2022-01-11',  '2022-01-12',  '2022-01-15',  '2022-01-17',  '2022-01-18'],
    'amount': [19.99, 49.99, 29.99, 99.99, 69.99, 39.99, 199.99, 79.99, 89.99, 59.99, 149.99, 79.99, 49.99, 109.99]
})


#Format dt type of date
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')

#Calculate the purchase frequency for each customer.
count_days_purchased = df.groupby(['customer_id'])['date'].count()
print('The number of days between each customer purchase: \n', count_days_purchased)
num_days_purchased = df.groupby(['customer_id'])['date'].apply(list)
average_days_purchased = [] #average number of days between purchases of all customers
for i in range(len(num_days_purchased.keys())):
    d_i = []    
    for j, day in enumerate(num_days_purchased.values[i]):
        if j==0:
            d_i_j =0
        else:
            d_i_j = pd.Timedelta(day - num_days_purchased.values[i][j-1]).days
        d_i.append(d_i_j)
    if len(d_i)==1:
        average_time = 0
        print('The customer id = ', num_days_purchased.keys()[i], 'has not visited our store again after the first shopping ')
    else:
        average_time = sum(d_i)/(len(d_i)-1)
        print('The customer id = ', num_days_purchased.keys()[i], ' has the average number of days between purchases is ', average_time)
    average_days_purchased.append(average_time)
    
#Calculate the total and average amount of each customer
total_amount_purchased = df.groupby(['customer_id'])['amount'].sum()
average_amount_purchased = df.groupby(['customer_id'])['amount'].mean()
print('The total amount of each customer: \n', total_amount_purchased)
print('The average amount of each customer: \n', average_amount_purchased)

#Plot result
fig, (ax1, ax2) = plt.subplots(2,1, figsize=(8,16), sharex=True)
fig.suptitle('Frequency and amount of each customer shopping online')
ax1.bar(count_days_purchased.keys(), count_days_purchased.values, label='Frequency')
ax1.plot(num_days_purchased.keys(), average_days_purchased, color='r', label='Average')
ax1.legend()
ax1.set_xlabel('Customer_id')
ax1.set_ylabel('Days')

ax2.plot(num_days_purchased.keys(), total_amount_purchased.values, label='Total')
ax2.plot(num_days_purchased.keys(), average_amount_purchased.values, label='Average')
ax2.legend()
ax2.set_xlabel('Customer_id')
ax2.set_ylabel('Amount')
plt.savefig('Practice4_report.png')

# plt.show()