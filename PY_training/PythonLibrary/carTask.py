import numpy as np
import pandas as pd

car1 = pd.read_csv("cars1.csv")
car2= pd.read_csv("cars2.csv")
# print(car1)
# print(car2)

df = pd.DataFrame(car1)
# x = car1.drop(['Unnamed: 9','Unnamed: 10','Unnamed: 11','Unnamed: 12'],axis='columns')
# print(x)

# rowdelete = car1.drop([0,1,2,3],axis=0)
# print(rowdelete)
# y = car1.rename(columns={'mpg':'target'})
# print(y)

# print(car1.loc[:,:"car"])
# df = df.filter(items=['mpg', 'cylinder','displacement','horsepower'])
# print(df)

# columns_list = list(car1.columns)
# start_index = columns_list.index('mpg')
# end_index = columns_list.index('car')
# car1 = car1[columns_list[start_index:end_index+1]]

# print(cars1.shape)
# print(cars2.shape)



# y = pd.concat([car1,car2],axis = 1,join='inner')
# print(y)










#..........................................fictious Name quastion...............................


data_1 = {
        'subject_id': ['1', '2', '3', '4', '5'],
        'first_name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'], 
        'last_name': ['Anderson', 'Ackerman', 'Ali', 'Aoni', 'Atiches']}

data_2 = {
        'subject_id': ['4', '5', '6', '7', '8'],
        'first_name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'], 
        'last_name': ['Bonder', 'Black', 'Balwner', 'Brice', 'Btisan']}

data_3 = {
        'subject_id': ['1', '2', '3', '4', '5', '7', '8', '9', '10', '11'],
        'test_id': [51, 15, 15, 61, 16, 14, 15, 1, 61, 16]}

df1 = pd.DataFrame(data_1,index=[101,102,103,104,105])
df2 = pd.DataFrame(data_2,index=[106,107,108,109,110])
df3 = pd.DataFrame(data_3,index=[111,112,113,114,115,116,117,118,119,120])

y = pd.concat([df1,df2],axis=1,join='outer')
print(y)

#join two data frame along row
df_combined = pd.concat([df1, df2], ignore_index=False)
print(df_combined)


#join two fdtaframe along column
# Join along columns (axis=1)
df_column_joined = pd.concat([df1, df2], axis=1)
print(df_column_joined)


# print data 3
print(df3)


# merge all the data and data 3
# Merge all dataframes on 'Subject_ID' using outer join (to keep all data)
df_merged = df1.merge(df2, on="subject_id", how="outer").merge(df3, on="subject_id", how="outer")

print(df_merged)



# merge the that has same subject id



df_common = df1.merge(df2, on="subject_id", how="inner")
print(df_common)



# same data merge



# Merge only matching values from both DataFrames
df_matched = df1.merge(df2, on="subject_id", how="inner")

print(df_matched)
