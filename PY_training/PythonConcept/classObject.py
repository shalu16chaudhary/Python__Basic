# WAP to create a class with name person and store details of person ?
class person:# create class with person name
    def __init__(self,person_name,person_age,person_weight,person_height):# define constructor and class attributes.
        # binding the class attributes with self keyword:
        self.person_name=person_name
        self.person_age=person_age
        self.person_weight=person_weight
        self.person_height=person_height
        
# Create class object.
obj=person("Gaurav","29yrs","75kg","170cm")
# calling class atrributes with the help of class object
print(obj.person_name)
print(obj.person_age)
print(obj.person_weight)
print(obj.person_height)



class person:# create class with person name
    def __init__(self,person_name,person_age,person_weight,person_height):# define constructor and class attributes.
        # binding the class attributes with self keyword:
        self.person_name=person_name
        self.person_age=person_age
        self.person_weight=person_weight
        self.person_height=person_height
        
# # Create class object.
# obj=person("Gaurav","29yrs","75kg","170cm")
# # calling class atrributes with the help of class object
# print(obj.person_name)
# print(obj.person_age)
# print(obj.person_weight)
# print(obj.person_height)

# class person:# create class with person name
#     def __init__(self,person_name,person_age,person_weight,person_height):# define constructor and class attributes.
#         # binding the class attributes with self keyword:
#         self.person_name=person_name
#         self.person_age=person_age
#         self.person_weight=person_weight
#         self.person_height=person_height
        
# # Create class object.
# obj=person("Gaurav","29yrs","75kg","170cm")
# # calling class atrributes with the help of class object
# print("Name:",obj.person_name,",","Age:",obj.person_age,",","Weight:",obj.person_weight,",","Height:",obj.person_height)


# WAP to sum of two number using class and object?
# WAP to create class and store students data and caclculte the total marks and set label accordingly, using class and object in python?

# STD data:
#     roll_number
#     std_name
#     std_age
#     std_contact_number
#     number of subject
#     std_marks per subject
#     std_knowledge(average, good, excellent)
#     label set:
#     below 50 its average
#     below 70 its good
#     above 90 its excellent


# rec={}
# n=int(input("Enter number of students: "))
# i=1
# while i <=n:
#     name=input("Enter Student Name: ")
#     marks=input("Enter % of Marks of Student: ")
#     rec[name]=marks
#     i=i+1
# print("Name of Student","\t","% of marks")
# for x in rec:
#     print("\t",x,"\t\t",rec[x])

# class Student:
#     def _init_(self, name, roll_no, marks):
#         self.name = name
#         self.roll_no = roll_no
#         self.marks = marks

#     def display(self):
#         print(f"Name: {self.name}, Roll No: {self.roll_no}, Marks: {self.marks}")

# # List to store multiple students
# students_list = []

# # Taking user input
# num_students = int(input("Kitne students ka data store karna hai? "))

# for i in range(num_students):
#     print(f"\nStudent {i+1} ka data enter kare:")
#     name = input("Name: ")
#     roll_no = int(input("Roll Number: "))
#     marks = float(input("Marks: "))
    
#     # Creating Student object and adding to list
#     students_list.append(Student(name, roll_no, marks))

# # Display all students
# print("\nStudent Data:")
# for student in students_list:
#     student.display()


   
      

      

























# class add_num:
#     def __init__(self,num1,num2):
#         self.num1=num1
#         self.num2= num2
#         self.num3=num1+num2
# a = int(input("Enter num1:"))
# b = int(input("Enter num2:"))
# obj=add_num(a,b)
# print(obj.num3)




# class addnum:
#    def __init__(self,num1,num2):
#       self.num1 = num1
#       self.num2 = num2
#       self.num3 = num1+num2

# x = int(input("num1"))
# y = int(input("num2"))
# obj = addnum(x,y)
# print(obj.num3)








# class person:
#   def _init_(self,person_name,person_age,person_weight,person_height):
#     self.person_name=person_name
#     self.person_age=person_age
#     self.person_weight=person_weight
#     self.person_height=person_height

# obj = person("Vanshika","20yrs","50kg","150cm")
# print(obj.person_name)
# print(obj.person_age)
# print(obj.person_weight)
# print(obj.person_height)

# class person:
#   def own(self,person_name,person_age,person_weight,person_height):
#     self.person_name=person_name
#     self.person_age=person_age
#     self.person_weight=person_weight
#     self.person_height=person_height

# obj = person()
# obj.own("Vanshika","20yrs","50kg","150cm")
# print(obj.person_name)
# print(obj.person_age)
# print(obj.person_weight)
# print(obj.person_height)

#WAP to sum of two number using class and object?
# class number:
#   def add( self,x,y):
#     self.x=x
#     self.y=y
#     return x+y

  
# obj = number()
# a=obj.add(10,20)
# print(a)


class students:
  def data(self,roll_number,std_name,std_age,std_contact_number,number_of_sub,std_mark_per_sub,std_knowledge):
    self.roll_number=roll_number
    self.std_name=std_name
    self.std_age=std_age
    self.std_contact_number=std_contact_number
    self.number_of_sub=number_of_sub
    self.std_knowledge=std_knowledge
  def calculate_total_marks(self):
    total=0
    for i in self.std_marks:
      total+=i
    result = total/5
    return result
  def set_label(self):
    result = self.calculate_total_marks()
    if result <50:
      return "average"


roll_no= int(input("enter a roll.no. here: "))
st_name= input("enter  name here: ")
st_age= int(input("enter age here: "))
st_cont= int(input("enter contact number here: "))
st_num= int(input("enter subject number here: "))
st_mark_sub= int(input("enter marks here: "))




obj = students()
obj.data("excellent","Good","Average","bad")
obj.data(roll_no,st_name,st_age,st_cont,st_num,st_mark_sub)
print(obj.roll_number)
print(obj.std_name)
print(obj.std_age)
print(obj.std_contact_number)
print(obj.number_of_sub)
print(obj.std_mark_per_sub)
print(obj.std_knowledge)