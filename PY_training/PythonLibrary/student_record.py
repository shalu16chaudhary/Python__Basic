import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv("PythonLibrary/student_record .csv")
# data = pd.read_csv("")
print(data)
print(data.isnull().sum())

# print(data['name'][19]

print(data[data["roll no."].isnull()])

x = (data[data["name"].isnull()])
data["name"].iloc[19] = "shalu"

print(data)
data["roll no."].iloc[19] = 15.0
print(data)

print(data.isnull().sum())
data.exam_id.iloc[19] = 23
print(data)
data.marks.iloc[19] = 100
print(data)
data.percentage.iloc[19] = "100%"
print(data)
data.result.iloc[19] = "passed"
print(data)
# data = data.drop(index = 19)
# print(data)
data["roll no."].iloc[4] = 15
print(data)
data["roll no."].iloc[13] = 13
print(data)
data["roll no."].iloc[18] = 18
print(data)
data["exam_id"].iloc[2] = 2
print(data)
data["exam_id"].iloc[3] = 3
print(data)
data["exam_id"].iloc[4] = 4
print(data)
data["exam_id"].iloc[13] = 14
print(data)
data["exam_id"].iloc[16] = 17
print(data)
data["exam_id"].iloc[17] = 18
print(data)

print(data.isnull().sum())

data["fees"].iloc[13] = "3k"
print(data)
data["fees"].iloc[14] = "3k"
print(data)
data["fees"].iloc[17] = "3k"
print(data)
data["fees"].iloc[20] = "3k"
print(data)
data["fees"].iloc[21] = "3k"
print(data)

data["marks"].iloc[2] = 80
print(data)
data["marks"].iloc[3] = 80
print(data)
data["marks"].iloc[4] = 80
print(data)
data["marks"].iloc[10] = 80
print(data)
data["marks"].iloc[13] = 80
print(data)
data["marks"].iloc[14] = 80
print(data)
data["marks"].iloc[17] = 80
print(data)
data["marks"].iloc[21] = 80
print(data)

data.percentage = data.percentage.fillna("75%")
print(data)

dict = {10:"passed" , 13:"passed", 14:"passed" , 21:"passed"}
data['result'] = data['result'].fillna(dict)
print(data)

# x = data.loc['name']
# y = data.loc['marks']
plt.bar(data["name"],data["marks"])
plt.xticks(rotation=90)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("my first graph")
plt.legend(["marks"],loc="upper right")
plt.show() 