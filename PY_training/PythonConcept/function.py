# def demo():
#     print("wlcome in function mode")
# demo()    

# def calculation(x ,y):
#     print(x+y)
#     print(x-y)
#     print(x*y)

#required argument 
# calculation(3,) 
   
# keyword args => when you defined the keywords of argument
# calculation(x=10 ,y=20)
# a = int(input("enter the value a"))
# b = int(input("enter the value b"))
# calculation(a ,b)



# variable length args
# def sum(*n):
#     total = 0
#     for n1 in n:
#         total = total+n1
#     print(total)
# sum(1,2,3,4,5)

# wap to print the index value

# def index(x):
x = ["A","B","C","D","E"]

for i in range(len(x)):
        # print(i,x[i])
        # print(i,"index" ,x[i])
        print(i-len(x),x[i])
        print(i , "index", x[i], x-len(x))


