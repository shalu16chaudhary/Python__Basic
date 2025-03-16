import numpy as np
import pandas as pd

car1 = pd.read_csv("cars1.csv")
print(car1)
# car2= pd.read_csv("cars2.csv")
# print(car2)

df = pd.DataFrame(car1)
# x = car1.drop(['Unnamed: 9','Unnamed: 10','Unnamed: 11','Unnamed: 12'],axis='columns')
# print(x)

# rowdelete = car1.drop([0,1,2,3],axis=0)
# print(rowdelete)
y = car1.rename(columns={'mpg':'target'})
print(y)

print(car1.loc[:,:"car"])







