import pandas as pd

## Practice 1: Create a dataframe and input data into the dataframe.

# Create a dictionary with some sample data
Info_data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Dave','Eva','Kevin'],
    'Birth_Date': ['1991-12-01', '1980-01-11', '1966-01-18', '1996-10-10', '1996-10-10', '1999-11-11']
}
Occupation_data = {'Name': ['Alice', 'Bob', 'Eve', 'Eva', 'Kevin'],
'Occupation': ['Engineer', 'Doctor', 'Teacher', 'Student', 'Student']}

# Create a column named Age
Birth_date = Info_data['Birth_Date']
current_year = 2023
ls_age = []
for i in range(len(Birth_date)):
    age =  current_year - int(Birth_date[i][:4])
    ls_age.append(age)
Info_data['Age'] = ls_age

# Create a dataframe from the dictionary
Info_df = pd.DataFrame(Info_data)
Occupation_df = pd.DataFrame(Occupation_data)

# New dataframe merged from 2 above dataframes
# New_df = Info_df.merge(Occupation_df, how='outer', on='Name')
New_df = Info_df.merge(Occupation_df, how='inner', on='Name')
New_df.pop('Birth_Date')
print('New dataframe is: \n', New_df)