# Q1 Write a Python program to find those numbers which are divisible by 7 and multiples of 5, 
# between 1500 and 2700 (both included).

# list=[]
# for i in range(1500,2701):
#     if i % 7==0 and i %5==0:
#         list.append(i)
# print(list)











# Q2 Write a Python program to guess a number between 1 and 9. 
# Note : User is prompted to enter a guess. If the user guesses wrong then the prompt 
# appears again until the guess is correct, on successful guess, user will get a "Well guessed!" 
# message, and the program will exit. 

# import random
# randomNo= random.randint(1,9)
# def guessAgain():
#    guess = int(input("enter the number between 1 to 9"))
# # guess = (input("enter the number between 1 to 9"))

# while True:
#   guess = int(input("enter the number between 1 to 9"))
#   if guess == randomNo:
#    print("well guessed!")
#    break
#   else:
#     print("Wrong guess , guess Again")
#     if guess!= randomNo:
#      print("guess Again")  
#     guessAgain()













# Q3 Write a Python program that prints each item and its corresponding type from the following 
# list.Sample List : datalist = [1452, 11.23, 1+2j, True, 'gauravwebsite', (0, -1), [5, 12], {"class":'V', 
# "section":'A'}] 

# datalist = [1452, 11.23, 1+2j, True, 'gauravwebsite', (0, -1), [5, 12], {"class":'V', 
# "section":'A'}] 
# for i in datalist:
#     print(f"item: {i} ,Type: {type(i)} ")












# Q4 Write a Python program that iterates the integers from 1 to 50. For multiples of three print 
# "Fizz" instead of the number and for multiples of five print "Buzz". For numbers that are 
# multiples of three and five, print "FizzBuzz". 
# Sample Output : 
# fizzbuzz 
# 1 
# 2 
# fizz 
# 4 
# buzz

# for i in range(1,51):
#     if i % 3==0:
#         print("fizz")
#         if i% 3==0 and i %5==0:
#          print("fizzbuzz")      
#     elif i % 5 == 0:
#         print("buzz")
#         if i% 3==0 and i %5==0:
#           print("fizzbuzz")             
#     else:
#         print(i)    













# Q5 Write a Python program that accepts a sequence of comma separated 4 digit binary 
# numbers as its input. The program will print the numbers that are divisible by 5 in a comma 
# separated sequence. 
# Sample Data : 0100,0011,1010,1001,1100,1001 
# Expected Output : 1010

# x = "0100,0011,1010,1001,1100,1001"
# list = x.split(",")
# print(list)
# for i in list:
#     if int(i,2)%5==0:
#         print("".join(i))


# #concept only
# # decimal_num = [int(b ,2) for b in list]
# # print(decimal_num)
# # for i in decimal_num:
# #     if i % 5==0:
# #         print(",".join(i))
# #         result = bin(i)[2:]    
# # print(result)     
# # num = ",".join(i)      
# # print(num)
        
     














# Q6 Write a Python program that accepts a string and calculates the number of digits and letters. 
# Sample Data : Python 3.2 
# Expected Output : 
# Letters 6 
# Digits 2

# x = "Python 3.2 "
# letters = 0
# digit = 0
# for char in x:
#     if char.isalpha():
#         letters+=1
#     elif char.isnumeric():
#         digit+=1
# print(letters)
# print(digit)    
















# Q7 Write a Python program to check the validity of passwords input by users. 
# Validation : 
#  At least 1 letter between [a-z] and 1 letter between [A-Z]. 
#  At least 1 number between [0-9]. 
#  At least 1 character from [$#@]. 
#  Minimum length 6 characters. 
#  Maximum 
#   
# length 16 characters. 

# import re
# def is_valid_password(password):
#     if (6 <= len(password) <= 16 and
#         re.search(r"[a-z]", password) and
#         re.search(r"[A-Z]", password) and
#         re.search(r"[0-9]", password) and
#         re.search(r"[$#@]", password)):
#         return True
#     return False

# # Taking user input
# password = input("Enter your password: ")

# if is_valid_password(password):
#     print("Valid password")
# else:
#     print("Invalid password")

















# Q8. Write a Python program to find numbers between 100 and 400 (both included) where each 
# digit of a number is an even number. The numbers obtained should be printed in a comma
# separated sequence.



# valid_num = []
# for num in range(100,401):
#     num_str = str(num)
#     if all(int(digit) % 2==0 for digit in num_str):
#         valid_num.append(num_str)
# print(",".join(valid_num))        
















# Q9. Write a Python program to calculate a dog's age in dog years. 
# Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog 
# year equals 4 human years. 
# Expected Output: 
# Input a dog's age in human years: 15                                     
# The dog's age in dog's years is 73 

# def dog_age_in_dog_years(human_years):
#     """Calculate dog's age in dog years based on human years."""
#     if human_years <= 2:
#         return human_years * 10.5
#     return 2 * 10.5 + (human_years - 2) * 4

# # Taking user input
# human_years = int(input("Input a dog's age in human years: "))

# dog_years = dog_age_in_dog_years(human_years)
# print(f"The dog's age in dog's years is {dog_years}")


















# Q10. Write a Python program to convert a month name to a number of days. 
# Expected Output: 
# List of months: January, February, March, April, May, June, July, August 
# , September, October, November, December                                 
# Input the name of Month: February                                        
# No. of days: 28/29 days

# def month_to_days(month):
#     """Convert a month name to the number of days."""
#     days_in_month = {
#         "January": "31 days", "February": "28/29 days", "March": "31 days",
#         "April": "30 days", "May": "31 days", "June": "30 days",
#         "July": "31 days", "August": "31 days", "September": "30 days",
#         "October": "31 days", "November": "30 days", "December": "31 days"
#     }
#     return days_in_month.get(month, "Invalid month")

# # Taking user input
# month = input("Input the name of Month: ")

# # Output the number of days
# print(f"No. of days: {month_to_days(month)}")
