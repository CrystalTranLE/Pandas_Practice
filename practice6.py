import random
import pandas as pd
import matplotlib.pyplot as plt

# Define the product categories, regions, and months
product_categories = ['Electronics', 'Clothing']
regions = ['North', 'South']
months = ['Jan', 'Feb', 'Mar']


# Generate sales data for each product category, region, and month
sales_data = []
for product in product_categories:
    for region in regions:
        for month in months:
            sales = random.randint(5000, 15000)  # Generate random sales amount between 5000 and 15000 dollars
            sales_data.append([product, region, month, sales])

# Convert the sales data to a pandas DataFrame
columns = ['Product_Category', 'Region', 'Month', 'Sales']
sales_df = pd.DataFrame(sales_data, columns=columns)


## Analyze sales trend
##1.We will analyze the total sales based on categories and regions 
##  to give a recommendation each region should focus on which category.


print('First analyzing: \n ')
tab = pd.crosstab(
    index=sales_df['Product_Category'],
    columns=sales_df['Region'],
    values=sales_df['Sales'],
    aggfunc='sum'
)

for region in regions:
    flag = max(tab[region])
    for i, product in enumerate(tab[region]):
        if product == flag:
            product_categories.sort()
            bigger_sale_product = product_categories[i]
    print('In the ' + region + ', the total sales of ' + bigger_sale_product + ' is highest.')
    print('We should increase the quantity of ' + bigger_sale_product + ' in the '+ region)

print('----------------------------------------------------------------')

#We can visualize the sales to see the differences
tab.plot(kind='bar', rot=0)
plt.title('Clothing and electronics sales in the regions')
plt.show()


##2. We will analyze the total sales based on months and product categories
##   to give a recommendation clothing and electronics should be sold in what month to obtain highest revenue

print('Second analyzing: \n')
tab1 = pd.crosstab(
    index=sales_df['Product_Category'],
    columns=sales_df['Month'],
    values=sales_df['Sales'],
    aggfunc='sum'
)

for month in months:
    flag = max(tab1[month])
    for i, product in enumerate(tab1[month]):
        if product == flag:
            product_categories.sort()
            bigger_sale_product = product_categories[i]
    print('In ' + month + ', the total sales of ' + bigger_sale_product + ' is highest.')
    print('We should focus on selling more ' + bigger_sale_product)

for i, index in enumerate(tab1.index):
    category_month = []
    max_sales_category = 0
    for j, month in enumerate(months):
        category_month.append(tab1[month][i])
        if tab1[months[j]][i] > max_sales_category:
            max_sales_category = tab1[months[j]][i]
            max_sales_month = months[j]
    print('In the first quarter of the year, the most ' + index + ' are in ' + max_sales_month)
    print('We should increase the quantity of ' + index + ' in ' + max_sales_month)

print('----------------------------------------------------------------')


#We can visualize the sales to see the differences
tab1.plot(kind='bar', rot=0)
plt.title('Clothing and electronics sales in the first quarter')
plt.show()