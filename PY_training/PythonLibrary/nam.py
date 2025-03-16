import numpy as np
# arr =np.array(([1,2,3],[2,3,4]))
# print(arr)

# arr =np.array([1,2,3])
# print(arr)

# arr = np.array([[10,20,30],[40,50,60],[70,80,90],[100,101,102]])
# a = np.arange(24)
# print(a)
# a.ndim
# print(arr)

# print(type(arr))
# print(arr.shape)
# print(arr.size)
# print(arr.ndim)

# b = a.reshape(2,4,3)
# print(b)
# print(b.ndim)


# a1 = np.array([[1,2,3],[4,5,6]],dtype='int')
# b1 = np.array([1,3,5])
# c1 = np.zeros((3,4)) #row ,col
# d1 = np.full((3,3),4,dtype='int')
# e1 = np.random.random((2,2))
# f = np.linspace(0,5,9)
# h = np.arange(0,30,2)
# print(a1)
# print(b1)
# print(c1)
# print(d1)
# print(e1)
# print(f)
# print(h)

# arr = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
# print(arr.shape)

# # slicing
# temp = arr[:3,::3] # before coma work for row after coma 
# print("\n",temp)

# temp = arr[1:3:1,1:2:2]
# print("\n",temp)

# temp = arr[1:3:1,::3]
# print("\n",temp)

# temp = arr[::1,::2]
# print("\n",temp)

# temp = arr[1:4:2,::1]
# print("\n",temp)

# temp = arr[1:2:1,::2]
# print("\n",temp)

# temp = arr[2:4:1,::2]
# print("\n",temp)

# temp = arr[1:2:1,::2]
# print("\n",temp)



# arr = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
# temp = arr[[0,1,2,3],[3,2,1,0]]

# print(temp)
# temp = arr[[1,3,2,1],[2,1,2,0]]
# print(temp)

# cond = arr>5
# temp = arr[cond]
# print("element greater than 5\n",temp)

# print("add element",arr+1)
# print("subtract element",arr-1)
# print("multiplication element",arr*1)
# print("multiplication element",arr**2)
# print("devide element",arr/9)

# a = np.array([[1,2,3],[3,4,5],[9,6,0]])
# a*=2
# print("doubled 1 value to every element ",a)

# # transpose
# a = np.array([[1,2,3],[3,4,5],[9,6,0]])
# print("original array\n",a)
# # print("transpose of array ",a.T)

# print("largest element",a.max())
# print("row wise max element ",a.max(axis=1))
# print("col wise max element ",a.min(axis=0))
# print("sum of all element",a.sum())
# print("cumulative sum along each row \n",a.cumsum(axis=1)) 


