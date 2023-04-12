import pandas as pd

# Create a dictionary of data
data = {'Name': ['John', 'Jane', 'Bob', 'Alice', 'Anna', 'Jerry'],
        'Age': [25, 30, 27, 40, 60, 62]}

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)

def check_age_func(x, var1, var2):
    '''
        This function to check age of a person and categorize this person 
        into one of three types - Young, Middle, Old
    '''
    if x[var1] < 30:
        x[var2] = 'Young'
    elif 30 <= x[var1] <= 60:
        x[var2] = 'Middle'
    else:
        x[var2] = 'Old'

    return x


# Display the DataFrame
df1 = df.apply(lambda x: check_age_func(x, 'Age', 'Category'), axis=1)
print('New dataframe adding Category column: \n', df1)