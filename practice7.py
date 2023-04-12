import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import numpy as np


def return_num_keys(df, features):
    for i, key in enumerate(df.keys()):
        if features==key:
            k = i
    return k

# Read in the dataset
df = pd.read_csv('customer_purchases.csv')
# print(df)


#Question 1
average_amount_category = df.groupby(['Product_Category'])['Purchase_Amount'].mean()
print('The average purchase amount for each product category: \n', average_amount_category)


#Question 2
average_age_category = df.groupby(['Product_Category'])['Age'].mean()
print('the average age of customers who make purchases in each product category: \n', average_age_category)

average_income_category = df.groupby(['Product_Category'])['Income'].mean()
print('the average age of customers who make purchases in each product category: \n', average_income_category)

#Question 3 
tab = pd.crosstab(
    index=df['Gender'],
    columns=df['Product_Category'],
    values=df['Gender'],
    aggfunc='count'
)
print('The gender distribution of customers in each category: \n', tab)

#Visualize the result 
tab.plot(kind='bar', rot=0)
plt.title('The gender distribution of customers in each category')
plt.show()


# Question 4
tab1 = pd.crosstab(
    index=df['Customer ID'],
    columns=df['Product_Category'],
    values=df['Product_Category'],
    aggfunc='count'
)    
print('Checking how many times of each customer buying products: \n', tab1)

# Find the customers buying multiple time in each category automatically
ls_category = pd.unique(df['Product_Category'])
k_date = return_num_keys(df, 'Purchase_Date')
k_amount = return_num_keys(df, 'Purchase_Amount')
for product in ls_category:
    ls_id_product  = []
    for i , customer_id in enumerate(df['Customer ID']):
        if df['Product_Category'][i]==product:
            ls_id_product.append(customer_id)
    if len(set(ls_id_product)) != len(ls_id_product):
        duplicate_id = Counter(ls_id_product)
        for id in duplicate_id:
            if duplicate_id[id]>1:
                print('customer has id =', id, 'buying ' + product + ' multiple times.')
                print('Specifically, this customer bought ', duplicate_id[id], ' times.')

                # Calculate the average time and amount between purchases
                df_date_amount = df[df['Customer ID'] == id]
                sum_amount = 0
                ls_date_id = []
                for j, obj in enumerate(df_date_amount.values):
                    sum_amount += df_date_amount.values[j][k_amount]
                    if j==0:
                        time_between_days = 0               
                    else:     
                        time_between_days = df_date_amount.values[j][k_date] - df_date_amount.values[j-1][k_date]
                    ls_date_id.append(time_between_days)
                average_amount = sum_amount/len(ls_date_id)
                average_time = sum(ls_date_id)/(len(ls_date_id)-1)
                print('The average time between purchases of customer id ', id, ' is ', average_time)
                print('The average amount between purchases of customer id ', id, ' is ', average_amount)


# Question 5

# Add column Month
df['Purchase_Date'] = pd.to_datetime(df['Purchase_Date'], unit='D', origin='1900-01-01')
df['Month'] = df['Purchase_Date'].dt.month
print(df)

# The average purchase amount for each month
mean_amount_month = df.groupby(df['Month'])['Purchase_Amount'].mean()
for i in mean_amount_month.keys():
    print('The average purchase amount of month ', i, ' is ', mean_amount_month[i])

# Seasonal trends in purchasing behavior
# 1. Indicate at each month, Female or Male go shopping more
tab_amount_gender_month = pd.crosstab(
                            index=df['Month'],
                            columns=df['Gender'],
                            values=df['Purchase_Amount'],
                            aggfunc='sum'    
                            )

print('The total purchased amount of each gender in each month: \n', tab_amount_gender_month)

for i, month in enumerate(tab_amount_gender_month.index):
    bigger_amount_gender = max(tab_amount_gender_month.values[i])
    for j, gender in enumerate(tab_amount_gender_month.keys()):
        if tab_amount_gender_month.values[i][j] == bigger_amount_gender:
            print('In month ', month,', ', gender, ' go shopping more.')

# 2.State which products people have a tendency to buy in each month
tab_amount_product_month = pd.crosstab(
                            index=df['Month'],
                            columns=df['Product_Category'],
                            values=df['Purchase_Amount'],
                            aggfunc='sum'    
                            )

print('The total purchased amount of each category in each month: \n', tab_amount_product_month)

for i, month in enumerate(tab_amount_product_month.index):
    bigger_amount_product = max(tab_amount_product_month.values[i])
    for j, product in enumerate(tab_amount_product_month.keys()):
        if tab_amount_product_month.values[i][j] == bigger_amount_product:
            print('In month ', month,', people tend to buy ', product, 'more than other categories.')

    
for product in pd.unique(df['Product_Category']):   
    flag= np.nanmax(tab_amount_product_month[product])
    for k, month in enumerate(tab_amount_product_month[product].keys()):
        amount_product_month = tab_amount_product_month[product].values[k]
        if amount_product_month == flag:
            print('People buy the most ', product, ' in month ', month)