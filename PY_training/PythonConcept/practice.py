
# str = "shaluchaudhary"
# reverse = " ,".join(reversed(str))
# print(reverse)


# alpha = 0
# numeric = 0
# for char in str:
#     if char.isalpha():
#         alpha += 1
#     elif char.isnumeric():
#         numeric += 1
# print(alpha)
# print(numeric)


# def vowelconst(str):
#     v_count = 0
#     c_count = 0
#     vowels = "aeiouAEIOU"
#     for ch in str:
#         if ch.isalpha():
#             if ch in vowels:
#                 v_count +=1
#             else:
#                 c_count +=1
#     return v_count , c_count

# vowels , consonants = vowelconst(str)
# print(vowels)
# print(consonants)

# a = "listen"
# b = "silent"
# def is_anagarm(s1 , s2):
#     return sorted(s1) == sorted(s2)


# print(is_anagarm(a ,b))


# lst =[ 4, 6, 7, 8,9,2 , 3]
# unique_list = list(set(lst))
# unique_list.sort(reverse = True)
# print(unique_list)
# print("second largest:" ,unique_list[1])


# l1 = [1,2,3,4]
# l2 = [3,4,5,6]
# l1 = set(l1)
# l2 = set(l2)
# print(list(l1.intersection(l2)))


# def flatten_list(l3):
#     for sublist in l3:
#         for i in sublist:
#             return i

# l3 = [ [1,2],[3,4],[5,6]]
# print(flatten_list([ [1,2],[3,4],[5,6]]))




# def set_operation(set1 ,set2):
#     return set1 | set2 , set1 & set2

# set1 = {1,2,3}
# set2 = {3,4,5}
# print(set_operation(set1,set2))


# class rect:
#     def area(self,l,b):
#         return l*b
    
# rec = rect()
# print(rec.area(2,3))


# s = "programming"
# out = "progamin"
# unique = " ,".join(dict.fromkeys(s))
# print(unique)

#trial
# list = s.split(",")
# print(list)
# set1 = list(set(s))
# print(set1)


# def first_non_repeating(s):
#     for ch in s:
#         if s.count(ch) ==1:
#             return ch
#     return None
# s = "swiss"
# print(first_non_repeating(s))




# def is_anagram(s1 , s2):
#     return sorted(s1) == sorted(s2)

# s1 = "hello"
# s2 = "lohel"
# s1 = "silent"
# s2 = "listen"
# print(is_anagram(s1 , s2))
        


# tuple = [("a",1),("b",2),("c",3),("d",4)]
# print(dict(tuple))




# class father:
#     def __init__(self,firstname,lastname ,age):
#         self.firstname = firstname
#         self.lastname = lastname
#         self.age = age
#     def sayname(self):
#         print(f"firstName: {self.firstname}, lastname: {self.lastname}")
        
#     def sayage(self):
#         print(f"age{self.age}")
# class daughter(father):
#     def sayname(self):
#          print(f"firstName: {self.firstname}, lastname: {self.lastname}")
# class son(father):
#     def sayname(self):
#          print(f"firstName: {self.firstname}, lastname: {self.lastname}")

# obj = father("abc" ,"is", 1)    
# obj2 = daughter("xyx","is",2)
# obj3 = son("pqr","is",3)
# obj.sayname()
# obj.sayage()
# obj2.sayname()
# obj2.sayage()
# obj3.sayname()
# obj3.sayage()

# calculatesum:
# #     def add(self,a,b):
# #         return a+b
# #     def add(self,a,b,c=10):
# #         return a+b+c
# # obj = calculatesum()
# # print(obj.add(10,20))