# fs = frozenset([1,2,34,5])
# print(fs)

# fs = frozenset([1,2,34,5,1,2])
# print(fs)

# fs[0] = "python"

# fs1 = frozenset([1,2,3,4])
# fs2 = frozenset([3,4,5,6])

# # union
# print(fs1 | fs2)
# # intersecion
# print(fs1 & fs2)

# # differnce
# print(fs1 - fs2)

# # symmetric differnce
# print( fs1 ^ fs2)

# my_dict = {frozenset([1,2,3]):"Frozen set example"}
# print(my_dict[frozenset([1,2,3])])
# print(my_dict)

# from collections import namedtuple
# person  = namedtuple('person',['name', 'age'])
# p = person("john",30)
# print(p.name , p.age)

# Employee = namedtuple('Employee',['name','age' , 'department', 'salary'])
# emp1 = Employee("Rahul",30,"HR",50000)
# emp2 = Employee("satyam",28,"IT",60000)
# emp3 = Employee("Nisha",35,"finance",70000)

# print(emp1.name)
# print(emp2.department )
# print(emp3.salary)

# print(emp1._asdict())
# emp1_updated = emp1._replace(salary = 55000)
# print(emp1_updated)

# Employee = namedtuple('Employee',['name','age','department','salary'])

# defalut dict

# from collections import defaultdict
# dd = defaultdict(int)
# dd["apple"]+= 1
# print(dd["apple"])
# print(dd["banana"])
# print(dd["mango"])
# print(dd)

# # counting word occurence
# word_count = defaultdict(int)
# sentence = " apple banana apple orange banana apple mango orange"
# for word in sentence.split():
#     word_count[word] += 1

# print(dict(word_count))

# from collections import OrderedDict

# od = OrderedDict()
# od["a"] = 1
# od["b"] = 2
# od["c"] = 3
# print(od)

