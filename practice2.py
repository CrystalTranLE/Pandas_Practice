import pandas as pd

##Practice 2: 
df = pd.DataFrame({'A': ['foo', 'bar', 'baz'],
                   'B': [[1, 2], [3, 4, 5], [6]]})

new_df = df.explode('B').reset_index(drop=True)
# path = 'C:/Users/admin/OneDrive/Máy tính/GLSoft_Tran/Training/Practice2_result.csv'
# new_df.to_csv(path)
# Link to download file csv: https://drive.google.com/file/d/1PjFsc9Kc-tz4afpIxG3WEW8hgQWoVOHa/view?usp=share_link