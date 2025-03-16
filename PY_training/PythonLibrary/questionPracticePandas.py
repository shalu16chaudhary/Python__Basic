import pandas as pd
import numpy as np
#1 Create a DataFrame from a dictionary and display the first 5 rows.

# df = pd.DataFrame({
#     'name' :['Shalu','Amit','sumit','Manju','Kisanveer','Krishna',"Bhoopsingh"],
#     'age':[21 ,22,24,44,50,40,50],
#     'id':[1,2,3,4,5,6,7],
# })

# print(df.head())




#2 Load a CSV file into a DataFrame and display basic info.
# data = pd.read_csv("info.csv")
# df = pd.DataFrame(data)
# print(df)


 
#3 Filter students who scored more than 80 marks
data = {
    'Name': ['Aman', 'Priya', 'Rahul', 'Sneha', 'Vikram'],
    'Age': [21, 22, 20, 23, 21],
    'Marks': [85, 90, 78, 88, 95]
}
df = pd.DataFrame(data)
filtered_sts = df[df['Marks']>80]
print(filtered_sts)

#4. Find the average age of students.
avg_age = df['Age'].mean()
print(avg_age)

#5. Count the number of students in each age group.
age_count = df['Age'].value_counts()
print(age_count)


#Given a dataset of employee salaries, find the employee with the highest salary.

data = {
    'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Salary': [55000, 72000, 67000, 85000, 90000]
}

df = pd.DataFrame(data)
highest_salary = df.loc[df['Salary'].idxmax()]
print(highest_salary)
# employee_index = df['Employee'[highest_salary]]
# print(employes)


#7. Add a new column "Tax (10%)" that calculates 10% tax on salary.
df['tax 10%'] = df['Salary']/10  # (salary*10)/100
print(df)


#8. Group data by "Department" and find the average salary per department.
data = {
    'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Department': ['HR', 'IT', 'IT', 'Finance', 'Finance'],
    'Salary': [55000, 72000, 67000, 85000, 90000]
}
df = pd.DataFrame(data)

avg_salary = df.groupby('Department')['Salary'].mean()
print(avg_salary)

#9. Find all employees whose names start with "A".
a_name_epl = df[df['Employee'].str.startswith('A')]
print(a_name_epl)

#10. Replace all "IT" department values with "Tech".
df['Department'] = df['Department'].replace('IT','Tech')
print(df)


#11. Given a dataset of sales data, find the month with the highest total sales.
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
    'Sales': [12000, 18000, 15000, 22000, 20000]
}
df = pd.DataFrame(data)
highest_total_score = df.loc[df['Sales'].idxmax()]
print(highest_total_score)


#14. Find the percentage change in sales month-over-month.
df['per_cng'] = df['Sales'].pct_change()*100
print(df)

# #12. Convert a date column to Pandas datetime format and extract the year.
# data = {
#     'Name': ['Alice', 'Bob', 'Charlie'],
#     'Join_Date': ['2020-05-15', '2019-08-21', '2021-02-10']
# }
# df = pd.DataFrame(data)
# df['Join_Date'] = pd.to_datetime(df['Join_Date'])
# df['year'] = df['Join_Date'].dt.year
# print(df)

# #13. Find the moving average of a stock price over 3 days.
# data = {
#     'Day': [1, 2, 3, 4, 5, 6, 7],
#     'Stock_Price': [100, 102, 101, 105, 110, 108, 115]
# }
# df = pd.DataFrame(data)

# df['3-day-MA']= df['Stock_Price'].rolling(window=3).mean()
# print(df)


#15. Find the correlation between two numerical columns (e.g., Sales and Profit).
data = {
    'Sales': [10000, 15000, 20000, 20000, 30000],
    'Profit': [2000, 3000, 4000, 5000, 6000]
}
df = pd.DataFrame(data)
correlation = df.corr()
print(correlation)

#16. Remove duplicate rows from a DataFrame.
df.drop_duplicates()
print(df)

#17. Find the number of missing values in each column.
