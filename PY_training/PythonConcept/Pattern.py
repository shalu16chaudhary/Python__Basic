# row = int(input("enter value"))
# for i in range(5,0,-1):
#     for j in range(i-1):
#         print("*",end=" ")
#     print()    

# row = int(input("enter value"))
# for i in range(row,0,-1):
#     for j in range(i-1):
#         print("*",end=" ")
#     print()    

# row = int(input("enter value"))
# for i in range(1,row+1):
#     for n in range(row-i):
#         print(end=" ")
#     for j in range(i):
#         print("*", end ="") 
#     print()       
  

# wap to create a fun to count upper case and lower case from given string
def check(s):
    uppercase = 0
    lowercase = 0
    for i in range(len(s)): 
      if s[i] >='A' and s[i]<='Z':
         uppercase+=1
      else:
         lowercase+=1
    print(uppercase)
    print(lowercase)

s = "Python is Programming Language"
check(s) 

# 2 method
s = input("enter ")
def str(s):
   upper = 0
   lower = 0
   for i in s:
      if i.isupper():
         upper+=1
      else:
         lower+=1
   return  upper, lower 
    
print(str(s))
        

      
