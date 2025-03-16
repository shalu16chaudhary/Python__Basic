import pandas as pd
import numpy as np


# dict containing employee daat
# data1 = {'Name':['rahul','princi','gaurav','anuj',],
#          'Age':[27,25,26,32],
#          'Address':['nagpur','kanpur','delhi','kannuaj'],
#           'qulification':['msc','ma','mca','phd'] }

# # define dict containg employee data
# data2 = {'Name':['abhi','ayushi','vanshika','sarita',],
#          'Age':[17,14,23,24],
#          'Address':['nagpur','kanpur','delhi','aligarh'],
#           'qulification':['btech','ba','bsc','PGDM'] }

# df= pd.DataFrame(data1 ,index = [0,1,2,3])
# df1= pd.DataFrame(data2 ,index = [4,5,6,7])

# print(df,'\n\n',df1)
# frames = [df,df1]
# x = pd.concat(frames)
# print(x)
# y = pd.



# adding diff rows and then concat
# data1 = {'Name':['rahul','princi','gaurav','anuj',],
#          'Age':[27,25,26,32],
#          'Address':['nagpur','kanpur','delhi','kannuaj'],
#           'qulification':['msc','ma','mca','phd'],
#            'contactNo':[274688,9388748,287390,7975] }

# data2 = {'Name':['abhi','ayushi','vanshika','sarita',],
#          'Age':[17,14,23,24],
#          'Address':['nagpur','kanpur','delhi','aligarh'],
#           'qulification':['btech','ba','bsc','PGDM'],
#           'email':['dhuhu87','njs78','nkjf86','rihu76']
#           }

# df= pd.DataFrame(data1 ,index = [0,1,2,3])
# df1= pd.DataFrame(data2 ,index = [11,12,13,14])

# print(df,'\n\n',df1)
# frames = [df,df1]
# x = pd.concat(frames)
# print(x)

# y = pd.concat([df,df1],axis = 1,join='inner')
# print(y)
# y = pd.concat([df,df1],axis = 0,join='inner')
# print(y)
# y1 = df._append(df1)
# print(y1)

# z = pd.concat([df,df1],ignore_index=True)
# print(z)
# z = pd.concat([df,df1],ignore_index=False)
# print(z)


# data1 = {'Name':['rahul','princi','gaurav','anuj',],
#          'Age':[27,25,26,32],
#          'Address':['nagpur','kanpur','delhi','kannuaj'],
#           'qulification':['msc','ma','mca','phd'],
#            'contactNo':[274688,9388748,287390,7975] }

# data2 = {'Name':['abhi','ayushi','vanshika','sarita',],
#          'Age':[17,14,23,24],
#          'Address':['nagpur','kanpur','delhi','aligarh'],
#           'qulification':['btech','ba','bsc','PGDM'],
#           'email':['dhuhu87','njs78','nkjf86','rihu76']
#           }

# df= pd.DataFrame(data1 ,index = [0,1,2,3])
# df1= pd.DataFrame(data2 ,index = [11,12,13,14])

# frames = [df ,df1]
# z = pd.concat(frames,keys=['x','y'])
# print(z)

# data1 = {'Name':['rahul','princi','gaurav','anuj',],
#          'Age':[27,25,26,32],
#          'Address':['nagpur','kanpur','delhi','kannuaj'],
#           'qulification':['msc','ma','mca','phd'],
#            'contactNo':[274688,9388748,287390,7975] }

# df = pd.DataFrame(data1 , index=[0,1,2,3])

# s1 = pd.Series([1000,2000,3000,4000],name='Salary')
# s2 = pd.Series([101,102,103,104],name='id')


# res = pd.concat([df,s1,s2],axis=1)
# print(res)
# print(df,"\n\n",s1,s2)




# data1 = {'Name':['rahul','princi','gaurav','anuj',],
#          'Age':[27,25,26,32],
#          'Address':['nagpur','kanpur','delhi','kannuaj'],
#           'qulification':['msc','ma','mca','phd'],
#            'contactNo':[274688,9388748,287390,7975] }

# data2 = {'Name':['abhi','ayushi','vanshika','sarita',],
#          'Age':[17,14,23,24],
#          'Address':['nagpur','kanpur','delhi','aligarh'],
#           'qulification':['btech','ba','bsc','PGDM'],
#           'email':['dhuhu87','njs78','nkjf86','rihu76']
#           }
# df = pd.DataFrame(data1)
# df1 = pd.DataFrame(data2)



# merge the operation

data1 = {'key':['k0','k1','k2','k3'],
         'name': ['princi','jai','anuj','gaurav'],
         'age':[27,28,26,32]
         }

data2 = {'key':['k0','k1','k2','k3'],
         'address': ['nagpur','kanpur','allhabad','kanuaj'],
         'qulification':['btech','ba','bcom','bhons']
}

df = pd.DataFrame(data1)
df1 = pd.DataFrame(data2)

a1 = pd.merge(df,df1,on='key')
print(a1)