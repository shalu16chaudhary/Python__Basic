#Q1 write a python pg to reverse the string without using slicing ([::-1])
# str = "hello"
# reverse = " ".join(reversed(str))
# print(reverse)

#Q2 write the py pg to check if given string is palindrome

# arr = "madam"
# if arr == arr[::-1]:
#     print(" yes , it a palindrome")
# else:
#     print("not")
 
#Q3 to calculate factorial of given number 
"""input: 5 """
# n =5
# fact = 1
# for i in range(1 , n+1):
#     fact *= i
# print(fact)

# fact = 1 * 1  → 1
# fact = 1 * 2  → 2
# fact = 2 * 3  → 6
# fact = 6 * 4  → 24
# fact = 24 * 5 → 120


#Q4 Binary search on sorted array
"""Array = [1,3,5,7,9]  Target = 5 output: element found at 2 index"""


# def binarySearch(arr , target):
#  start , end = 0 ,len(arr)-1
#  while start <= end:
#      mid = (start+end)//2
#      if arr[mid]== target:
#          return mid
#      elif arr[mid]<target:
#          start = mid+1
#      else:
#          end = mid -1

#  return -1  

# target = int(input("enter the element to be found"))
# arr = [1,3,5,7,9] 
# result = binarySearch(arr, target)

# if result != -1:
#     print(f"Element found at index {result}")
# else:
#     print("Element not found")
   

#Q5 find the second max element

# Array = [10,20,4,45,99]
# first_largest = max(Array)
# Array.remove(first_largest)
# second_largest = max(Array)
# print(second_largest)
   
# Q6 to generate fibonacci series

# n = int(input("enter number"))
# a , b = 0 ,1
# for i in range(n):
#     print( a , end =" ")
#      a , b = b , a+b



#Q7 remove duplicate from list

# array = [ 1,2,2,3,4,4,5]
# set1 = set(array)
# list1 = list(set1)
# print(list1)


#Q8 prime number
# n = int(input("enter number"))
# if n>1:
#     for i in range(2,n):
#         if n%i ==0:
#             print("not a prime number")
#             break
#     else:
#         print("yes its is prime number")
# else:
#     print("not a prime number")

#Q9 
n = 1234
total = 0
while n>0:
    a = n%10
    total = total +a
    n = n//10
print(total)

#Q10

def findMissingNumber(arr,n):
    expected_sum = n*(n+1)//2
    actual_sum = sum(arr)
    return expected_sum - actual_sum

arr = [1,2,4,5]
n = 5  # total number count
print(findMissingNumber(arr,n))
