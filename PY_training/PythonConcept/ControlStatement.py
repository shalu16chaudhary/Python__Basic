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
# year = int(input("enter year"))
# if (year % 4 ==0 and year % 100!= 0) or (year % 400 ==0):
#     print("leap year")
# else:
#     print("not leap year")






# for loop
# wap to check number is even or odd from range? using loop
# for i in range(11):   
#     if i%2==0:
#         print( i," is even" )
#     else:
#          print( i,"  is odd" )  
         





# print table of number
# n = int(input("enter the number"))
# for i in range(1,11):
#     print(n,"x",i,"=",n*i)





# print table from 2 to 20
# for i in range(2,21):
#     for j in range(1,11):
#         print(i,"x",j,"=",i*j)
#     print()





# # wap to print 100 to 1
# x = 100
# while x>0:
#     print(x , end= " ")
#     x=x-1
   






    
# to sum the  digit of number
# n = int(input("enter the number to add"))
# sum = 0
# while n>0:
#     a = n%10
#     sum = sum +a
#     n = n//10
# print(sum)





# for i in range( 1 , 20):
#     if i ==15:
#         pass
#     # print(i)
#     print(i , end = " ")
# print(" outside the  loop")    

n = int(input("enter number"))
if n > 1:
    for i in range(2, n):
        if n%i==0:
            print("not a prime number")
            break
    else:
        print(n," a prime number")
else:
    print(n,"not a prime number")
            
              
