# Q1- Write a Python function to find the maximum of three numbers.

# def maxNumber(a,b,c):
#     if a>b and a>c:
#         print(a,"is greater number")
#     elif b>a and b>c:
#         print(b,"is greater number")
#     else:
#         print(c,"is greater number")    
# x = int(input("enter the first number"))
# y = int(input("enter the second number"))
# z = int(input("enter the third number"))
# maxNumber(x,y,z)    










# Q2- Write a Python function to sum all the numbers in a list.
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20

# list = [ 8, 2, 3, 0, 7]
# add = sum(list)
# print(add)

# def add(list):
#     addition =sum(list)
#     print(addition)

# list = [ 8, 2, 3, 0, 7]
# add(list)











# Q3- Write a Python function to multiply all the numbers in a list.
# Sample List : (8, 2, 3, -1, 7)
# Expected Output : -336

# def mul(list):
#     total=1
#     for i in list:
#      total = total*i
#     print(total)
# list = [8, 2, 3, -1, 7]
# mul(list)








# 4- Write a Python function that takes a list and returns a new list with 
# distinct elements from the first list.
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]

# def newList(list1):
#     newSet = set(list1)
#     uniqueList = list(newSet)
#     print(uniqueList)

# list1 = [1,2,3,3,3,3,4,5]
# newList(list1)










# 5- Write a Python program to print the even numbers from a given list.
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result : [2, 4, 6, 8]

# def EvenNum(list):
#     result=[]
#     for i in list:
#         if i%2==0:
#             result.append(i)

#     print(result)
            
# list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# EvenNum(list)














# 6- Write a Python function to check whether a number is "Perfect" or not.
# According to Wikipedia : In number theory, a perfect number is a positive integer 
# that is equal to the sum of its proper positive divisors, that is, the sum of its positive divisors
#  excluding the number itself (also known as its aliquot sum). Equivalently,
#  a perfect number is a number that is half the sum of all of its positive divisors 
# (including itself).
# Example : The first perfect number is 6, because 1, 2, and 3 are its proper positive divisors, 
# and 1 + 2 + 3 = 6. Equivalently, the number 6 is equal to half the sum of all its
#  positive divisors: ( 1 + 2 + 3 + 6 ) / 2 = 6. The next perfect number is 28 = 1 + 2 + 4 + 7 + 14. 
# This is followed by the perfect numbers 496 and 8128.


# def is_perfect_number(n):
#     if n <= 0:
#         return False
    
#     sum_of_divisors = 0
    
#     for i in range(1, n // 2 + 1):  # Proper divisors are less than n
#         if n % i == 0:
#             sum_of_divisors += i
    
#     return sum_of_divisors == n

# # Example usage
# test_numbers = [6, 28, 496, 8128, 10]
# for num in test_numbers:
#     print(f"{num} is a perfect number: {is_perfect_number(num)}")



# my trial  skip this
# def PerfectNum(num):
#     list=[]
#     for n in range(1,100):
#      if num % n ==0 and n < num:
#         list.append(n)
#         result = sum(list)
#     print(result)
#     #     if result == num:
#     #      print("perfect number")
#     # else:
#     #    print("not a perfect number")


# num = int(input("enter number"))
# PerfectNum(num)














# 7- Write a Python program that accepts a hyphen-separated sequence of words as 
# input and prints the words in a hyphen-separated sequence after sorting them alphabetically.
# Sample Items : green-red-yellow-black-white
# Expected Result : black-green-red-white-yellow

# string = "green-red-yellow-black-white"
# list = string.split("-")
# print(list)
# list.sort()
# str = "-".join(list)
# print(str)












# 8- Write a Python program that invokes a function after a specified period of time.
# Sample Output:
# Square root after specific miliseconds:
# 4.0
# 10.0
# 158.42979517754858


# import time
# import math

# def delayed_square_root(number, delay):
#     time.sleep(delay / 1000)  # Convert milliseconds to seconds
#     return math.sqrt(number)

# # Example usage
# numbers_with_delays = [(16, 1000), (100, 2000), (25098, 3000)]
# print("Square root after specific milliseconds:")
# for num, delay in numbers_with_delays:
#     print(delayed_square_root(num, delay))
