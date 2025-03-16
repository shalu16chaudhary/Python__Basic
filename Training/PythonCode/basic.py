# a= 1
# b= 3
# print(a+b)
# a= eval(input("enter first num"))
# b= eval(input("enter second num"))
# print(a+b)

# from keyword import kwlist 
# #  extract all keyword in list
# print(len(kwlist))

# #add two complex and bool number
# a=2+1j
# b=False
# print(a+b)

# x=10
# y=10.0
# print(x is y)
# print(id(x))
# print(id(y))



# # string hanadling
# arr = "nitin"
# print(arr[0:3])
# # for arr in range:
# if arr[0:4] is arr[-1:-6]:
#         print("palindrome")
# else:
#         print("not palindrome")   




    
# x=input("enter a string")
# y=(x[::-1])
# if y==x:
#     print("yes")
# else:
#     print("no")

# a = "python"   
# print(a[0:20])
# print(a[::-1])





# a = "python is programming language and its very important to us"
# forward_output = "  ".join(a)
# print(forward_output)
# b = a[::-1]
# print("\n")
# backward_output = " ".join(b)
# print(backward_output)

# a = "python is programming language and its very important to us"

# for i in a:
#     if i =='':
#         continue
#     print(i , end=" ")
# print()
# for i in a[::-1]:
#     if i =='':
#         continue
#     print(i , end="")





# a = "python Programming"
# print(a.upper())
# print(a.lower())
# print(a.capitalize())

# x = "python is programming language"
# y ="python is programming language"

# print(x.title())
# print(x.title()[0:40:7])




# #  use of join function 
# # to convert the list item in string
# friend_list = ['joe','cherry','tom']
# friends = ','.join(friend_list)
# print(friends)





# # use of split function
# # to covert the string value into the list item
# friends = "joe,tom,cherry"
# friend_list = friends.split(',')
# print(friend_list)




# print square of number
# num= [ 1, 2, 3, 4, 5, 6, 7]
# sq = []
# for i in num:
#     sq.append(i**2)
# print(sq)  



# # map function =>it map two function 
# def square(n):
#     return n**2

# num=[1, 2, 3, 4, 5, 6, 7]    
# sq = list(map(square , num))
# print(sq)




# # filter function
# def greater_then_2(n):
#     if n>2:
#         return True
#     else:
#         return False

# num=[1, 2, 3, 4, 5, 6, 7]         
# greater_th_2 = list(filter(greater_then_2, num))
# print(greater_th_2)
 



# #  reduce function
# from functools import reduce
# # reduce list ko function mai run karwayega

# def sum(a,b):
#     return a+b

# list = reduce(sum , [1,2,3,4,5])
# print(list)



# list in python 
# => can include number , bool , string [1 , two , 12.8 , 2 , 2]

# listModification=>append(),insert(),remove(RmoveParticularNum),pop(RemoveLastNum) ,del[del by index]

# list operation  => cancatination repetition , membership

# list method => reverse(), count() index() copy() clear()
# listcomprehension=> 
# square = [ x**2 for x in range(1,6)] 
# print(square)

# conversion of other data type into list=> str , tuple , set
# s = "hello"
# list_s= list(s)

