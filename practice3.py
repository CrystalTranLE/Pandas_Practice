import pandas as pd
import matplotlib.pyplot as plt
from statistics import mean
##Practice 3:

#Put data into the dataframe
df = pd.DataFrame(
    {
    'customer_id': [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010],
    'gender': ['M', 'F', 'F', 'M', 'F', 'F', 'M', 'F', 'M', 'M'],
    'age': [25, 35, 28, 22, 45, 50, 40, 35, 30, 27],
    'city': ['London', 'New York', 'San Francisco', 'Paris', 'Boston', 'Melbourne', 'San Francisco', 'London', 'New York', 'Paris'],
    'category': ['T-Shirts', 'Jeans', 'Dresses', 'Suits', 'Tops', 'Dresses', 'Jeans', 'T-Shirts', 'Trousers', 'Tops'],
    'sub_category': ['Plain', 'Skinny', 'Maxi', 'Formal', 'Blouse', 'Party', 'Straight', 'Graphic', 'Chinos', 'T-Shirt'],
    'price': [10.99, 49.99, 99.99, 199.99, 29.99, 149.99, 79.99, 19.99, 59.99, 14.99],
    'quantity': [2, 1, 1, 1, 2, 1, 1, 3, 1, 2]
    }
)

# Question 1: Perform EDA
print('The dimension of data: ', df.shape) 
print('The data type of each column: \n', df.dtypes) 
print('Statistics of data: \n', df.describe()) 
print('Checking the missing values: \n', df.isnull().sum())


# # Question 2: Calculate the total revenue
   
df['revenue'] = df['price']*df['quantity']  
total_revenue = df['revenue'].sum()
print('The total revenue of the store: ', total_revenue)

# Question 3: The average price and quantity of clothing purchased by customers in each category.

avg_price = df.groupby(['category'])['price'].mean()
quantities = df.groupby(['category'])['quantity'].sum()
print('The average price of each category: ', avg_price)
print('The quantity of each category: ', quantities)

# Question 4: Group the dataset by the customer's age and gender and calculate the total revenue generated by each age/gender group.
# For gender group
data_gender = df.groupby(['gender'])['gender'].count()
total_revenue_gender = df.groupby(['gender'])['revenue'].sum()
print('The dataset group by the customer gender: \n', data_gender)
print('The total revenue generated by gender group: \n', total_revenue_gender)


# For age group 
data_age = df.groupby(['age'])['age'].count()
total_revenue_age = df.groupby(['age'])['revenue'].sum()
print('The dataset group by the customer age: \n', data_age)
print('The total revenue generated by age group: \n', total_revenue_age)

# Question 5,6 
total_revenue_cities =  df.groupby(['city'])['revenue'].sum()
top3_cities = total_revenue_cities.sort_values(ascending=False).head(3)
print('Top 3 cities in terms of total revenue: ')
for i, city in enumerate(top3_cities.keys()):
    print(city)


# Insights on Age factor
mean_age_cities = df.groupby(['city'])['age'].mean() #average age of each city
average_age = mean(df['age']) #average age of data
print('The average age of data is ', average_age)

for i, city in enumerate(top3_cities.keys()):
    age_top3 = mean_age_cities[city]
    print('The average age of city '+ city +' is ', age_top3)
print('We can see the average age in Paris and San Franciso is below and around the average of data.')
print('It indicates that shoppers in these two cities are mainly young people.')
print('And it is clear that young generation pay much more for shopping than elderly people')


# Insights on Price factor
mean_price_cities = df.groupby(['city'])['price'].mean() #average price of each city
average_price = mean(df['price']) #average price of data
print('The average price of data is ', average_price)
for i, city in enumerate(top3_cities.keys()):
    price_top3 = mean_price_cities[city]
    print('The average price of city '+ city +' is ', price_top3)
print('We can see the average price of cities in top 3 has totally bigger than the average price of data.')
print('It shows that a person in one of top 3 cities can pay a larger amount for 1 item than others living other cities')
print('It leads to the total revenue of top 3 cities is higher other cities.')


# Insight on percentage of Revenue factor
total_revenue = sum(df['revenue'])
sum_percentage = 0
for i, city in enumerate(top3_cities.keys()):
    percentage_top3_cities = total_revenue_cities[city]/total_revenue*100
    print(city, ' total sales represent ', percentage_top3_cities, ' percent of all cities sale')
    sum_percentage += percentage_top3_cities
print('Top 3 cities total sales accounts ', sum_percentage, ' percent of all total sales')
print('It proves that the capability of consuming clothes at Paris, San Francisco and Melbourne is over than 3 other cities')


# Recommendation
tab = pd.crosstab(
    index=df['city'],
    columns=df['category'],
    values=df['revenue'],
    aggfunc='sum'
)
print('The total revenue of each category in each city: \n', tab)
print('Each city currently only sells 1 or 2 types, we should diversify the items so that consumers have more choices.')