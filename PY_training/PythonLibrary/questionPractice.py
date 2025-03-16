import numpy as np
import random

# arr = np.arange(10,50) #create a NumPy array of integers from 10 to 50
# print(arr)
# arr = np.arange(0,9).reshape(3,3)  #create a 3x3 NumPy array with values ranging from 0 to 8
# print(arr)
# arr = np.ones((3,3))  #create a NumPy array of shape (3,3) with all elements as 1
# print(arr)
# arr = np.random.rand(5)   #generate a NumPy array of 5 random numbers between 0 and 1?
# print(arr)

# arr = np.random.randint(1,101 , size = 10) # generate a NumPy array of 10 random integers between 1 and 100?
# print(arr)       

# arr= np.arange(1,10)  #find the maximum and minimum value in a NumPy array
# arr = np.array([1,2,3,4,5,6,7,8,9])
# print(np.max(arr))
# print(np.min(arr))
# print(np.mean(arr))  #find the mean and standard deviation of a NumPy array
# print(np.median(arr))
# print(np.std(arr))

# arr =np.eye(4)#create an identity matrix of size 4x4
# print(arr)

# arr = np.array([1,2,3,4,5,6,7,8,9,10])   #extract all even numbers from a NumPy array?
# even = []
# for i in arr:
#     if i%2 ==0:
#         even.append(i)

# print(even)    # Output: [2, 4, 6, 8, 10]




# arr = np.array([1,2,3,4,5,6,7,8,9,10])   #replace all odd numbers in a NumPy array with -1
# list =[]
# for i in arr:
#     if i % 2 ==1:
#         i = -1
#     list.append(i)
    
# print(list)
        
# arr = np.array([1,2,3,4,5,6,7,8,9,10])#replace all even numbers in an array with 0
# evenzero = []
# for i in arr:
#     if i % 2 ==0:
#         i = 0
#     evenzero.append(i)
# print(evenzero)

# arr = np.random.randint(1,51,size=(3,3))#create a NumPy array of shape (3,3) filled with random integers between 1 and 50
# print(arr)
# print(np.sum(arr))

#find the column-wise sum of a 3x3 NumPy array
arr = np.array([[1,2,3],[4,5,6,],[7,8,9]])
print(np.sum(arr,axis = 0))

arr = np.array([[1,2,3],[4,5,6,],[7,8,9]])  #find the row-wise sum of a 3x3 NumPy array
print(np.sum(arr,axis =1))

arr = np.array([[7,5,3],[4,8,7,],[7,2,1]]) #sort a NumPy array in ascending and descending order
print(np.sort(arr))

arr = np.array([[7,5,3],[4,8,7,],[7,2,1]])
print(np.sort(arr)[::-1])

arr = np.array([4,67,35,8,66,9,56,43,4,2])    #find the index of the maximum and minimum value in a NumPy array?
print(np.max(arr))
print(np.min(arr))

arr = np.array([4,67,35,8,1,9,5,43,4,2])#create a boolean mask for all numbers greater than 5 in a NumPy array
mask = []
for n in arr:
    if n >5:
        mask.append(n)
print(mask)
#find the top 3 scores
scores = np.array([45, 78, 88, 56, 90, 67, 99, 82, 76, 95])
top3 = np.sort(scores)[-3:]
print(top3)

#Given a dataset of monthly sales, find the month with the highest sales
sales = np.array([1200, 3400, 2300, 5000, 6700, 5400, 7600, 8200, 4500, 3800, 6100, 7300])
months = np.array(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])

max_sale_index = np.argmax(sales)
best_month = months[max_sale_index]
print(f"best month {best_month} with highest sales {sales[max_sale_index]}")

# dataset of temperatures, find how many days had temperatures above average
temps = np.array([32, 35, 30, 28, 40, 45, 38, 42, 37, 39, 41, 43, 36, 29, 33])
average = np.mean(temps)
abv_avg = np.sum(temps > average)
print(abv_avg)

print(average)
temp = []

for n in temps:
    if n > average:
        temp.append(n)

print(temp)
#Given a dataset of product prices, replace outliers with the median price
prices = np.array([100, 120, 130, 110, 125, 900, 115, 105, 140, 950, 135])

#dataset of student scores in multiple subjects, find the student with the highest total score.
students = np.array(["Aman", "Priya", "Rahul", "Sneha", "Vikram"])
scores = np.array([
    [85, 90, 78],  # Aman
    [88, 76, 95],  # Priya
    [92, 89, 85],  # Rahul
    [79, 84, 80],  # Sneha
    [91, 87, 88],  # Vikram
])

total_score = np.sum(scores,axis=1)
top_student_index = np.argmax(total_score)
top_student = students[top_student_index]
print(f"{top_student} is the top student with {total_score[top_student_index]} score")



#dataset of daily electricity consumption, find the moving average for the past 3 days
consumption = np.array([150, 160, 170, 180, 190, 200, 210, 220, 230, 240])


#Given a dataset of employee salaries, find the median salary for employees earning above ₹50,000.
salaries = np.array([45000, 52000, 60000, 70000, 48000, 75000, 82000, 67000, 90000])
for n in salaries:
    if n > 50000:
        median_salary = np.median(n)
print(median_salary)


highest_salary = salaries[salaries >50000]
median_salaries = np.median(highest_salary)
print(f"{median_salaries} is the meadian salary of emplyee greater than 5k")


# a dataset of daily stock prices, find the days when the stock price increased from the previous day.
stock_prices = np.array([100, 102, 98, 105, 110, 108, 115, 120, 118, 122])

increase_days = np.where(stock_prices[1:] > stock_prices[:-1])[0] + 1  # Find indices of increase
print(f"Days when stock increased: {increase_days}")


#Given a dataset of house prices, calculate the percentage increase/decrease in price compared
# to the previous month.
house_prices = np.array([50000, 52000, 51000, 53000, 55000, 54000, 56000])

percentage_change = np.diff(house_prices) / house_prices[:-1] * 100
print(percentage_change)


