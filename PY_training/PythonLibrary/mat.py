import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# x = [1,2,3]
# y = [ 2,4,1]
# plt.plot(x,y)
# plt.xlabel("x-axis")
# plt.ylabel("y-axis")
# plt.title("my first graph")
# plt.show()         

# x = [1,2,3]
# y = [ 2,4,1]
# # z= [5,6,7]
# plt.plot(x,y,label="line 1")

# x1 = [3,5,7]
# y1 = [6,8,9]
# # z1 = [4,7,4]
# plt.plot(x1,y1,label="line 2")

# plt.xlabel("x-axis")
# plt.ylabel("y-axis")
# # plt.zlabel("z-axis")
# plt.title("plot two lines")
# plt.legend()
# plt.show()  


# x = [1,2,3,4,5,6]
# y = [ 1,2,3,4,3,6]

# plt.plot(x,y,color="green",linestyle="dashed",linewidth ="1",marker ="*",markerfacecolor="blue",markersize = 12)

# plt.ylim(1,8)
# plt.xlim(1,8)

# plt.xlabel("x-axis")
# plt.ylabel("y-axis")

# plt.title("thirdline")

# plt.show() 


# left = [1,2,3,4,5]
# height = [10,24,36,40,5]
# tick_label =["one","two","three","four","five"]

# plt.bar(left,height,tick_label=tick_label,width =0.8,color=["blue","orange"])
# plt.xlabel("x-axis")
# plt.ylabel("y-axis")
# plt.title("my bar chart")
# plt.show()

# left = [1,2,3,4,5]
# height = [86,80,90,89,98]
# tick_label =["joe","mary","alice","sam","harry"]
# plt.bar(left,height,tick_label=tick_label,width =0.8,color=["skyblue","orange"])
# plt.xlabel("x-axis")
# plt.ylabel("y-axis")
# plt.title("my bar chart")
# plt.show()

#...........

# x = [ 0,1,2,3,4,5,6,7,8]
# y = [0,10,20,30,40,50,60,70,90]

# plt.scatter(x,y)
# plt.show()

# data = pd.read_csv("gwp.csv")
# data2 = pd.read_csv("Salaries.csv")
# data3 =pd.read_csv("student_record (1).csv")

# df = pd.DataFrame(data)
# data = data.set_index("Year")
# print(data)
# data['GWP'].plot()
# # plt.scatter(df['Year'],df['GWP'])
# plt.show()


# df1 = pd.DataFrame(data2)
# plt.scatter(df['Year'],df['GWP'])
# plt.show()


# df3 = pd.DataFrame(data3)
# plt.scatter(df['Position'],df['Level'])
# plt.show()




# ages= [ 2,5,47,9,10,20,25,14,1,16,18,19,10,19,17]
# student = ['jeery','tom','mickey','mouse','bean']
# marks = [70,50,60,30,60,60,80,90,67,89,80]
# range =[0,100]
# bins= 10
# plt.hist(marks,bins ,range,color = "green",histtype="bar",rwidth=0.8)
# arr = np.random.randn(50)

# plt.xlabel("marks")
# plt.ylabel("student")
# plt.title("hist")
# plt.show()


# import random

# # Generate random data
# data = np.random.randn(1000)  # Normal distribution

# # Create histogram with color and edgecolor
# plt.hist(data, bins=30, color='skyblue', edgecolor='black')

# # Labels and Title
# plt.xlabel("Value Range")
# plt.ylabel("Frequency")
# plt.title("Histogram with Edge Color and Fill Color")

# # Show the plot
# plt.show()

# data3 =pd.read_csv("student_record.csv")
# # df3 = pd.DataFrame(data3)
# print(data3)


#.........................grapgh question..............................



import numbers as np 
import pandas as pd
import matplotlib.pyplot as plt

#1 Write a  Python program to draw a line with suitable label in the x axis, y axis and a title.

# x = [1,2,3]
# y = [1,2,3]
# plt.plot(x,y)
# plt.xlabel("x-axis")
# plt.ylabel("y-axis")
# plt.title("my first graph")
# plt.show()         









#2 Write a Python program to draw a line using given axis values with suitable label in the
#  x axis , y axis and a title.


# x = [1, 2, 3, 4, 5]
# y = [2, 4, 6, 8, 10]
# x = [1,2,3]
# y = [2,4,1]

# plt.plot(x, y)
# plt.xlabel("X Axis")
# plt.ylabel("Y Axis")
# plt.title("graph 2")
# plt.legend()

# plt.show()






#3  Write a Python program to draw a line using given axis values taken from a text file, with
#  suitable label in the x axis, y axis and a title.
# Test Data:
# test.txt
# 1 2
# 2 4
# 3 1


# x, y = [], []
# with open("PythonConcept/matdata.txt") as f:
#     data = f.readlines()
#     for i in data:
#         i = i.split()
#         x.append(int(i[0]))
#         y.append(int(i[1]))

# plt.title(' Graph')
# plt.plot(x,y)
# plt.show()




#4 Write a Python program to draw line charts of the financial data of Alphabet Inc. between 
# October 3, 2016 to October 7, 2016.
# Sample Financial data (fdata.csv):
# Date,Open,High,Low,Close
# 10-03-16,774.25,776.065002,769.5,772.559998
# 10-04-16,776.030029,778.710022,772.890015,776.429993
# 10-05-16,779.309998,782.070007,775.650024,776.469971
# 10-06-16,779,780.47998,775.539978,776.859985
# 10-07-16,779.659973,779.659973,770.75,775.080017

# df = pd.read_csv("PythonConcept/fdata.cvs")
# print(df)
# plt.plot(df.Date,df.Open,label = "Open")
# plt.plot(df.Date,df.High,label = "High")
# plt.plot(df.Date,df.Low,label = "Low")
# plt.plot(df.Date,df.Close,label = "Close")
# plt.xticks(rotation = 90)
# plt.legend()
# plt.show()




#5 Write a Python program to plot two or more lines on same plot with suitable legends of each line.

# x1 = [1,2,4]
# y1 = [2,1,4]
# plt.plot(x1,y1,color="green",linewidth ="1")

# x2 = [3,4,1]
# y2 = [2,1,3]
# plt.plot(x2,y2, color = "blue",)

# plt.xlabel("x-axis")
# plt.ylabel("y-axis")
# plt.title("plot two lines")
# plt.legend()
# plt.show() 




#6 Write a Python program to plot two or more lines with legends, different widths and colors.

# x1 = [1,2,3,]
# y1 = [2,4,1]
# plt.plot(x1,y1,color="green")

# x2 = [1,2,3]
# y2 = [2,4,3]
# plt.plot(x2,y2, color = "blue",)

# plt.xlabel("x-axis")
# plt.ylabel("y-axis")
# plt.title("plot two lines")
# plt.legend()
# plt.show() 





#7 Write a Python program to plot two or more lines with different styles.

# x1 = [1,2,3,]
# y1 = [2,4,1]
# plt.plot(x1,y1,color="green",linestyle="dashed")

# x2 = [1,2,3]
# y2 = [2,4,3]
# plt.plot(x2,y2, color = "blue",linestyle="dotted")

# plt.xlabel("x-axis")
# plt.ylabel("y-axis")
# plt.title("plot two lines")
# plt.legend()
# plt.show() 





#8 Write a Python program to display the current axis limits values and set new axis values.
# x1 = [1,2,3,4]
# y1 = [1,2,3,4]
# plt.plot(x1,y1,color="blue")



# plt.xlabel("x-axis")
# plt.ylabel("y-axis")
# plt.ylim(1,8)
# plt.xlim(1,8)

# plt.title("plot two lines")
# plt.legend()
# plt.show() 



#9 Write a Python program to plot quantities which have an x and y position.


# x1 = [ 0,1,2,3,4]
# y1 = [0,10,20,30,40]

# plt.scatter(x1,y1,color="red", marker=".")

# x2 = [1,2,3,2,5,]
# y2 = [34,67,89,23,56]
# plt.scatter(x2,y2, color = "blue",marker="*")
# plt.title("ques9")
# plt.legend()
# plt.show()







#10 Write a Python program to plot several lines with different format styles in one command using arrays.

x = [1,2,3,4,5,6]
y = [1,2,3,4,3,6]

plt.plot(x,y,color="green")

plt.ylim(1,8)
plt.xlim(1,8)

plt.xlabel("x-axis")
plt.ylabel("y-axis")

plt.title("thirdline")

plt.show() 









#11 Write a Python program to display the grid and draw line charts of the closing value of Alphabet Inc. between October 3, 2016 to October 7, 2016. Customized the grid lines with linestyle -, width .5. and color blue.
# Date,Close
# 03-10-16,772.559998
# 04-10-16,776.429993
# 05-10-16,776.469971
# 06-10-16,776.859985
# 07-10-16,775.080017















da = pd.read_csv("PythonLibrary/insurance.csv")
print(da)

da = {col:list(da[col].unique()) for col in da.select_dtypes("object")}
print(da)

class Pie_plot():
    def __init__(self,serie,title,color,explode):
        self.serie = serie
        self.title = title
        self.color = color
        self.explode = explode

def pie(self):
    pass