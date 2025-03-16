import pandas as pd
# Data = [1,3,4,5,6,2,9]
# a= pd.Series(Data)
# print(a)
# print(type(a))

# Data = [1,3,4,5,6,2,9]
# dict ={ "a":1,"b":3,"c":4,"d":6,"e":2,"f":9}
# a= pd.Series(dict)
# print(a)

# Data = [[1,2,3],[4,5,6],[1,2,3],[1,2]]
# snd = pd.Series(Data)
# print(snd)


# dict ={}
# for i in range(1,10):
#     dict[chr(96+i)]=i
# df = pd.Series(dict)
# print(df)    


# dataframe 
# table has row and col each col in data frame is a series of obj row consist element inside series 

# df = pd.DataFrame({
#     'country':['india','russia','belarus','ukraine'],
#     'population': [ 125.04, 143.5,45.5,9.5],
#     'square':[27297487,4848,37498327,84377]
#     }) 
# print(df)
# print(df['country'])
# print(type(df))
# print(df.columns)
# print(df.index)
# print(df['population'][0]) # acess the population of india

# df = pd.DataFrame({
#     'country':['india','russia','belarus','ukraine'],
#     'population': [ 125.04, 143.5,45.5,9.5],
#     'square':[27297487,4848,37498327,84377]
#     } ,index = ['IND','RU','BY','UA'])
# print(df)

# df.index= ['IND','RU','BY','US']   # index of name dene ke liye 
# df.index.name = 'country code'
# print(df)

# print(df.loc['IND'])  # COUNTRY KA PURA DATA
# print(df.iloc[3])
# print(df.loc[['IND','RU'],'population'])
# print(df.loc['IND':'BY',:]) # SLICING
# print(df[df.population>10][['country','square']])
# df['density'] = df['population']/ df['square']*1000
# print(df)

# df = pd.DataFrame({
#     'std_roll_no': [1,2,3,4,5,6,7,8,9,10],
#     'std_name':['sam','joe','benny','mary','alice','pop','sue','lacy','king','lucy'],
#     'std_contact':[272978487,484859687,37498327,8437859477,8247657,875876,4575,894785,4858,387857],
#     'std_address':['agra','mathura','noida','delhi','america','udaipur','jaipur','prayag','almora','nanital'],
#     'std_stream':['cse','me','ai','ml','bio','math','science','mba','btech','bpharma'],
#     }) 
# print(df)
# df.index= [11,22,33,44,55,66,77,88,99,00]   # index of name dene ke liye 
# df.index.name = 'code'
# print(df)

import pandas as pd
import numpy as np













