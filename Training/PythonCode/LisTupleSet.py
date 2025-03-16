
# wap to create a list with elements and apply list methods?
# x = [10 ,20,30,120,150,13,0.2, 1589]
# x.append(2)
# print(x)

# x.insert(0,"queue")
# print(x)

# x.sort()
# print(x)

# x.reverse()
# print(x)

# x.clear()
# print(x)

# x.remove(10)
# print(x)

# x.pop(2)
# print(x)

# x.extend([20,30,40])
# print(x)

# wap to sum all the list item
# list =[ 1,2,3,4]
# total = sum(list)
# print(total)


# wap to get a list sorted in increasing order by the last 
# element in each tuple from a given list of non emmpty tuples

# list = [(2,5),(1,2),(4,4),(2,3),(2,1)]
# def last(n):
#  return n[-1]
# def sorted_list(tuples):
#  return sorted(tuples ,key = last)
# print(sorted_list(list))

# # for i in list:
# list.sort()
# print(list)



# wap that take two list and return true if they have at least one common member

# x = [ 1,2,3,4,5]
# y = [ 6,7,8,9,1]
# set1 = set(x)
# set2 = set(y)
# if set1.intersection(set2):
#  common = set1.intersection(set2)
#  print("true")


# print(common)
# for i in x, y:
 
#  if x[i] == y[i]:
#   print("true")
#  else:
#   print("not") 


# wap a python pg to sort a given list of non empty
#  tuples in increasing order by the sum of  element in each tuples
# list =[(2,5),(1,2),(4,4),(2,3),(2,1)] 

# sum(list)
# print(total)

# list = [(2,5),(1,2),(4,4),(2,3),(2,1)]
# def add(n):
#  return sum(n)
# def sorted_list(tuples):
#  return sorted(tuples ,key = add)
# print(sorted_list(list))


# x=(1,2,5,6,8,9)

# print(x.index(2))
# print(min(x))
# print(max(x))
# print(len(x))
# print(x.count(6))
# print(sum(x))

# wap to get 4th element from the last element of a tuple
# x=(1,2,5,6,8,9)
# print(x[-4])

# wap to replace the last value of tuple in a list
# list=[(10,20,40),(40,50,60),(70,80,90)]
# def last(n):
#  return n[-1]
# # def replaced_list(tuples):
  
# # print(list(n))
# print(n[-1]=100)

# wap to remove an empty tuple(s) from list of tuple
# x = [(),(),('',),('a','b'),('a','b','c'),('d')]

x ={10,20,30,40,50,60}
y ={50,60,70,80,90,100,387}
print (x.union(y))
print(x.intersection(y))
print(x.difference(y))
print(x.add(1))

# wap to find all the unique words and count the frequency of 
# occurence from a given list of string. use python set data type

x = [" black ","green","black","red ","red","black","white","yellow", "green","white"]
set(x)
print(x)
y = {}

# # print(x.count("black"))
# print(y.union(set(x)))
print(set(x).union(y))
# wap to find the the two no. whose product is max among all pair in a given list of number 
# use python set

     
# wap to find all unique combination of 3 no from 
# a given list of number  adding up to a target number 
