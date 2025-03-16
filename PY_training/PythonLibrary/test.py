import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random

# question 1
def is_palindrome(s):
    return s == s[::-1]


string = is_palindrome("babad")
print(string)
# if is_palindrome(s):
#     print(yes)


# df = pd.DataFrame({
#     'category':['A','B','A','B','A'],
#     'sales':[100,200,150,300,50],
#     'region':['East','West','East','West','East'],
# })
# result = complex_aggregation(df)






#question 5
# df1 = pd.DataFrame({
#     'id':[1,2,3],
#     'value':[10,20,30],
#     'region':['East','West','East'],

# })
# df2 = pd.DataFrame({
#     'id':[1,2,3],
#     'value':[100,200,300],
#     'category':['A','B','C']
# })
# # merged_df = conditional_merge(df1,df2,conditional_column = 'region')
# a1 = pd.merge(df1,df2,on='id')
# print(a1)
# a = pd.concat([df1,df2] ,axis = 0 ,join = "inner")
# # x = pd.concat(a)
# print(a)




#question 3
# a = np.array([[1,3],[0,2]])
# print(a.mean())





#question 6
# data = np.random.randn(1000)
# x = [ 0,1,2,3,4,5,6,7,8]
# y = [0,10,20,30,40,50,60,70,90]

# plt.scatter(x,y)
# plt.legend()
# plt.show()




# question 7
# arr =np.array(([1,2,3],[2,3,4]))
# print(arr)
# sns.heatmap()




# question 8
# df= pd.DataFrame(np.random.rand(100,5))
# column = ['A','B','C','D','E']
# plt.pariplot(df , column)
# plt.legend()
# plt.show()