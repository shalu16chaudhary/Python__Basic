# # Inheritance
# class A:
#     def Adata(self):
#         print("Adata is a method of class A")
# class B(A):
#     def Bdata(self):
#         print("Bdata is a method of class B")
# obj = B()
# obj.Adata()
# obj.Bdata()     

# # MUltilevel Inheritance

# class A:
#     def Adata(self):
#         print("Adata is a method of class A")
# class B(A):
#     def Bdata(self):
#         print("Bdata is a method of class B")
# class C(B):
#     def Cdata(self):
#         print("Cdata is a method of class C")
# class D(C):
#     def Ddata(self):
#         print("Ddata is a method of class D")
# obj = D()
# obj.Adata()
# obj.Bdata()
# obj.Cdata()
# obj.Ddata()
# #Multiple
# class A:
#     def Adata(self):
#         print("Adata is a method of class A")
# class B:
#     def Bdata(self):
#         print("Bdata is a method of class B")
# class C(A,B):
#     def Cdata(self):
#         print("Cdata is a method of class C")
# obj = C()
# obj.Adata()
# obj.Bdata()
# obj.Cdata()

# # hierarchical Inheritance
# class A:
#     def Adata(self):
#         print("Adata is a method of class A")
# class B(A):
#     def Bdata(self):
#         print("Bdata is a method of class B")
# class C(A):
#     def Cdata(self):
#         print("Cdata is a method of class C")
# obj = C()
# obj1 = B()
# obj.Adata()
# obj1.Bdata()
# obj.Cdata()

# # Hybird Inheritance
# class A:
#     def Adata(self):
#         print("Adata is a method of class A")
# class B(A):
#     def Bdata(self):
#         print("Bdata is a method of class B")
# class C(A):
#     def Cdata(self):
#         print("Cdata is a method of class C")
# class D(B,C):
#     def Ddata(self):
#         print("Ddata is a method of class D")
# obj = D()

# obj.Adata()
# obj.Bdata()
# obj.Cdata()
# obj.Ddata()


# # Polymorphism

# class Father:
#     def __init__(self , first_name, last_name,age):
#         self.first_name= first_name
#         self.last_name=last_name
#         self.age=age
#     def say_name(self):
#         print("father name",self.first_name+" "+self.last_name)
#     def say_age(self):
#         print("age",str(self.age))
# class daughter(Father):
#     def say_name(self):
#         print("daughter name",self.first_name+" "+self.last_name)
# class son(Father):
#     def say_name(self):
#         print("son name",self.first_name+" "+self.last_name)

# obj = Father("xyz","is","1")
# obj1 =son("abe","is","2")
# obj2 = daughter("poi","is","3")
# obj.say_name()
# obj.say_age()
# obj1.say_name()
# obj1.say_age()
# obj2.say_name()
# obj2.say_age()


# overloading
# class calculatesum:
#     def add(self,a,b):
#         return a+b
#     def add(self,a,b,c):
#         return a+b+c
# obj = calculatesum()
# obj.add(10,20)

# alternate
# class calculatesum:
#     def add(self,a,b):
#         return a+b
#     def add(self,a,b,c=10):
#         return a+b+c
# obj = calculatesum()
# print(obj.add(10,20))

class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage