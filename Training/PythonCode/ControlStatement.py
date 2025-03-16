# # wap to check no. is even
# n = int(input("enter the number"))
# if n % 2 == 0:
#     print("even")
# else:
#     print("odd")    

# # wap to check number is negative
# n = int(input("enter the number"))
# if n < 0:
#     print("negative")    
# else:
#     print("positive")    

#wap
# x = int(input("enter the number"))
# y = int(input("enter the number"))
# z = int(input("enter the number"))
# if x > y and x > z  :
#     print("x is greater and y and z are smaller")
# elif y > x and y > z:
#     print(" y is greater and x and z is smaller")
# elif z > x and z > y:
#    print("z is greater and x and y are smaller")
# elif (x and  y > z ) :
#     print(" z is smaller")
# elif ( x and z > y) :
#     print(" y is smaller ")
# elif(y and z > x) :
#     print("x is smaller")   
# else:
#     print( " all are equal")     


# # wap to check leap year

# x = int(input("enter the number"))
# if x % 400 == 0 or x % 100 == 0:
#      print("leap year")
# elif x % 4== 0 or x %100 == 0:     
#      print("leap year")
# else:
#     print("not a leap year")

# for loop
# wap to check number is even or odd from range? using loop
# n = int(input("enter the number"))
# for i in range(11):
#     print(i)
#     if i%2==0:
#         print("i is even" )
#     else:
#          print(" i is odd" )                   
# n = int(input("enter the number"))
# for i in range(1,11):
#     print( n,"x",i,"=",n*i)

# for i in range(2,21):
#     for j in range(1,11):
#      print( i,"x",j,"=",i*j)
# # print()     

# # wap to print 100 to 1
# x = 100
# while x>0:
#     print(x , end= " ")
#     x=x-1
   

# sum = 0
# x = int(input("enter the number"))
# rem = x % 10
# left = x // 10
# sum = sum + rem
# rem = left %10
# left = left //10
# sum = sum + rem
# rem = left %10
# left = left // 10
# sum = sum + rem

# print(sum)


# a = 187
# b = 0
# while (a != 0):
#     c = a%10
#     b =b + c
#     a = a //10
# print(b)    


for i in range( 1 , 20):
    if i ==15:
        pass
    # print(i)
    print(i , end = " ")
print(" outside the  loop")    