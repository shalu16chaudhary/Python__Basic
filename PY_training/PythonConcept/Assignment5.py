# # 1. Sort a list of tuples by the first element in each tuple.
# # Sample List: [(5, 1), (2, 4), (3, 3), (1, 2)]
# # Expected Output:
# # [(1, 2), (2, 4), (3, 3), (5, 1)]
# # Explanation: The tuples are sorted by the first element. The sorted list is: [(1, 2), (2, 4), (3, 3), (5, 1)].

# list = [(5, 1), (2, 4), (3, 3), (1, 2)]
# list.sort()
# print(list)

# def sortTuple(tuples):
#     def get_first_element(t):
#         return t[0]
#     return sorted(tuples,key = get_first_element)

# print(sortTuple)











# # 2. Sort a list of tuples by the sum of the elements in each tuple.
# # Sample List: [(1, 2), (2, 3), (3, 1), (4, 2)]
# # Expected Output:
# # [(1, 2), (3, 1), (4, 2), (2, 3)]
# # Explanation: The tuples are sorted based on the sum of their elements. Sum of elements in the tuples:
# # (1, 2) → 3
# # (2, 3) → 5
# # (3, 1) → 4
# # (4, 2) → 6
# # The sorted list by sum of elements: [(1, 2), (3, 1), (4, 2), (2, 3)].

# list = [(1, 2), (2, 3), (3, 1), (4, 2)]
# def add(n):
#  return sum(n)
# def sorted_list(tuples):
#  return sorted(tuples ,key = add)
# print(sorted_list(list))











# # 3. Sort a list of tuples in reverse order based on the first element in each tuple.
# # Sample List: [(3, 4), (1, 2), (5, 1), (2, 3)]
# # Expected Output:
# # python
# # Copy
# # [(5, 1), (3, 4), (2, 3), (1, 2)]
# # Explanation: The tuples are sorted by the first element in reverse order: 5 > 3 > 2 > 1.

# list = [(3, 4), (1, 2), (5, 1), (2, 3)]
# list.sort()
# list.reverse()
# print(list)











# # 4. Group tuples by the first element in each tuple and sort the groups by the last element.
# # Sample List: [(2, 5), (1, 2), (2, 3), (1, 1), (2, 4)]
# # Expected Output: [(1, 1), (1, 2), (2, 3), (2, 4), (2, 5)]
# # Explanation: First, the list is grouped by the first element (1 and 2), and then each group is sorted by the second element. The final result is [(1, 1), (1, 2), (2, 3), (2, 4), (2, 5)].

# list = [(2, 5), (1, 2), (2, 3), (1, 1), (2, 4)]
# def last(n):
#     return n[-1]
# def sorted_list(tuple):
#     return sorted(tuple , key = last)
# print(sorted_list(list))













# # 5. Sort a list of tuples by the length of each tuple.
# # Sample List: [(1, 2), (1, 2, 3), (4,), (2,)]
# # Expected Output:[(4,), (2,), (1, 2), (1, 2, 3)]
# # Explanation: The tuples are sorted by their length: [(4,), (2,), (1, 2), (1, 2, 3)].

# list = [(1, 2), (1, 2, 3), (4,), (2,)]

# def sorted_list(tuple):
#     return sorted(tuple,key = len)
# print(sorted_list(list))

# # trial code skip
# # n = len(list)
# # print(n)
















# # 6. Sort a list of tuples by the first element, and in case of a tie, by the second element.
# # Sample List: [(1, 3), (1, 2), (2, 4), (2, 3)]
# # Expected Output:
# # python
# # Copy
# # [(1, 2), (1, 3), (2, 3), (2, 4)]
# # Explanation: The tuples are first sorted by the first element. If two tuples 
# # have the same first element, they are then sorted by the second element. 
# # The result is: [(1, 2), (1, 3), (2, 3), (2, 4)].

# list = [(1, 2), (1, 3), (2, 3), (2, 4)]
# list.sort()
# print(list) # sort by the first element 

# def last(n): #sort using the second element
#     return n[-1]
# def sorted_list(tuples):    
#     return sorted(tuples , key = last)
# print(sorted_list(list))

















# # 7. Find the tuple with the maximum sum of elements from a list of tuples.
# # Sample List: [(1, 2), (3, 1), (5, 2), (4, 3)]
# # Expected Output:# (5, 2)
# # Explanation: The sum of the elements in the tuples:
# # (1, 2) → 3
# # (3, 1) → 4
# # (5, 2) → 7
# # (4, 3) → 7
# # The tuple with the maximum sum is (5, 2) or (4, 3) (since both have the same sum of 7).
# #  In case of a tie, the tuple that appears first is chosen.

# list = [(1, 2), (3, 1), (5, 2), (4, 3)]

# tuples = [sum(i) for i in list]
# tuple_sum = list(map(sum , list))
# result = list(tuples)
# print(tuple_sum)










# # 8. Find the tuple with the minimum first element in a list of tuples.
# # Sample List: [(4, 5), (2, 3), (1, 6), (3, 2)]
# # Expected Output:(1, 6)
# # Explanation: The tuple with the minimum first element is (1, 6).


# tuples_list = [(4, 5), (2, 3), (1, 6), (3, 2)]
# min_tuple = tuples_list[0]
# for tup in tuples_list:
#     if tup[0] < min_tuple[0]:
#         min_tuple = tup
# print(min_tuple)













# # 9. Sort a list of tuples by the second element, but if two second elements are equal, sort by the first element.
# # Sample List: [(3, 5), (1, 4), (2, 4), (4, 5)]
# # Expected Output:[(1, 4), (2, 4), (3, 5), (4, 5)]
# # Explanation: The tuples are first sorted by the second element, and if the second elements are equal, they are sorted by the first element.


# tuples_list = [(3, 5), (1, 4), (2, 4), (4, 5)]
# n = len(tuples_list)
# for i in range(n):
#     for j in range(0, n - i - 1):
#         # Pehle second element ko compare karenge
#         if tuples_list[j][1] > tuples_list[j + 1][1]:
#             tuples_list[j], tuples_list[j + 1] = tuples_list[j + 1], tuples_list[j]
#         # Agar second element same hai, toh first element se compare karenge
#         elif tuples_list[j][1] == tuples_list[j + 1][1] and tuples_list[j][0] > tuples_list[j + 1][0]:
#             tuples_list[j], tuples_list[j + 1] = tuples_list[j + 1], tuples_list[j]
# print(tuples_list)














# # 10. Create a new list of tuples where each tuple contains the sum of the elements from the original list of tuples. Sort it in increasing order of the sum.
# # Sample List: [(1, 3), (2, 1), (4, 2), (3, 1)]
# # Expected Output:[(2, 1), (3, 1), (1, 3), (4, 2)]
# # Explanation: First, calculate the sum of elements in each tuple:

# # (1, 3) → 4
# # (2, 1) → 3
# # (4, 2) → 6
# # (3, 1) → 4
# # After sorting by sum: [(2, 1), (3, 1), (1, 3), (4, 2)].

# tuples_list = [(1, 3), (2, 1), (4, 2), (3, 1)]
# def tuple_sum(tup):
#     return tup[0] + tup[1]
# # Implementing Bubble Sort based on sum of elements
# n = len(tuples_list)

# for i in range(n):
#     for j in range(0, n - i - 1):
#         if tuple_sum(tuples_list[j]) > tuple_sum(tuples_list[j + 1]):
#             tuples_list[j], tuples_list[j + 1] = tuples_list[j + 1], tuples_list[j]
# print(tuples_list)
















# # -List Questions:
# # Merge Sorted Lists: Given two sorted lists, write a Python function to merge them into a single 
# # sorted list without using the sorted() function.

# def merge_sorted_lists(list1, list2):
#     merged = []
#     i, j = 0, 0

#     while i < len(list1) and j < len(list2):
#         if list1[i] < list2[j]:
#             merged.append(list1[i])
#             i += 1
#         else:
#             merged.append(list2[j])
#             j += 1

#     merged.extend(list1[i:])
#     merged.extend(list2[j:])
    
#     return merged


# print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))  # [1, 2, 3, 4, 5, 6]







# # -Rotate List: Write a Python function that rotates a list to the right by k positions.
# #  (For example, [1, 2, 3, 4, 5] rotated by 2 positions becomes [4, 5, 1, 2, 3]).

# def rotate_list(nums, k):
#     if not nums or k % len(nums) == 0:
#         return nums
#     k = k % len(nums)
#     return nums[-k:] + nums[:-k]


# print(rotate_list([1, 2, 3, 4, 5], 2))  # [4, 5, 1, 2, 3]






# # -Find the Longest Increasing Subsequence: Given a list of integers, write a Python function that 
# # returns the longest increasing subsequence.

# from bisect import bisect_left
# def longest_increasing_subsequence(nums):
#     if not nums:
#         return []
    
#     subseq = []
    
#     for num in nums:
#         pos = bisect_left(subseq, num)
#         if pos == len(subseq):
#             subseq.append(num)
#         else:
#             subseq[pos] = num
    
#     return subseq


# print(longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18]))  # [2, 3, 7, 18]






# # -Group Anagrams: Write a function that takes a list of strings and groups them into anagrams 
# # (i.e., strings that are anagrams of each other).

# from collections import defaultdict
# def group_anagrams(words):
#     anagram_dict = defaultdict(list)
    
#     for word in words:
#         sorted_word = ''.join(sorted(word))
#         anagram_dict[sorted_word].append(word)
    
#     return list(anagram_dict.values())


# print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# # [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]






# # -Nested List Flattening: Write a Python program that flattens a nested list of lists into a 
# # single list (e.g., [[1, 2], [3, [4, 5]], 6] becomes [1, 2, 3, 4, 5, 6]).


# def flatten_list(nested_list):
#     flattened = []
    
#     def flatten(sublist):
#         for item in sublist:
#             if isinstance(item, list):
#                 flatten(item)
#             else:
#                 flattened.append(item)
    
#     flatten(nested_list)
#     return flattened


# print(flatten_list([[1, 2], [3, [4, 5]], 6]))  # [1, 2, 3, 4, 5, 6]



















# # Tuple Questions:
# # -Tuple Comparison: Write a function that compares two tuples element by element and returns True
# #  if all elements are equal, otherwise False.

# def compare_tuples(tuple1, tuple2):
#     return tuple1 == tuple2

# # Example
# print(compare_tuples((1, 2, 3), (1, 2, 3)))  # True
# print(compare_tuples((1, 2, 3), (1, 2, 4)))  # False






# # -Find the Second Largest Element: Write a Python function that returns the second largest element 
# # in a tuple without converting it to a list.

# def second_largest(tup):
#     if len(tup) < 2:
#         return None  # Not enough elements
    
#     first, second = float('-inf'), float('-inf')
    
#     for num in tup:
#         if num > first:
#             second = first
#             first = num
#         elif first > num > second:
#             second = num
    
#     return second if second != float('-inf') else None

# print(second_largest((10, 20, 4, 45, 99)))  # 45
# print(second_largest((5, 5, 5)))  # None







# # -Tuple to Dictionary: Write a function that takes a list of tuples where each tuple contains two 
# # elements (key, value), and converts them into a dictionary.

# def tuples_to_dict(tuples_list):
#     return dict(tuples_list)


# print(tuples_to_dict([('a', 1), ('b', 2), ('c', 3)]))
# # {'a': 1, 'b': 2, 'c': 3}









# # -Count Occurrences in Tuple: Given a tuple of elements, write a Python function that counts the
# #  frequency of each element using a dictionary and returns it.

# def count_occurrences(tup):
#     freq_dict = {}
#     for item in tup:
#         freq_dict[item] = freq_dict.get(item, 0) + 1
#     return freq_dict

# # Example
# print(count_occurrences((1, 2, 2, 3, 3, 3, 4, 4, 4, 4)))
# # {1: 1, 2: 2, 3: 3, 4: 4}























# # Set Questions:
# # -Find Symmetric Difference: Write a Python function that takes two sets and returns their 
# # symmetric difference (elements that are in one set or the other, but not both).

# def symmetric_difference(set1, set2):
#     return set1 ^ set2  # Equivalent to (set1 - set2) | (set2 - set1)

# # Example
# print(symmetric_difference({1, 2, 3}, {3, 4, 5}))  # {1, 2, 4, 5}









# # -Set Operations on Multiple Sets: Given multiple sets, write a Python program to find
# #  the union, intersection, and difference for all the sets.

# def multiple_set_operations(*sets):
#     union_result = set.union(*sets)
#     intersection_result = set.intersection(*sets)
#     difference_result = set.difference(*sets)  # Difference with respect to first set

#     return {
#         "Union": union_result,
#         "Intersection": intersection_result,
#         "Difference": difference_result
#     }


# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}
# set3 = {4, 5, 6, 7}
# print(multiple_set_operations(set1, set2, set3))
# # {'Union': {1, 2, 3, 4, 5, 6, 7}, 'Intersection': {4}, 'Difference': {1, 2}}










# # -Check for Subset and Superset: Write a Python function that takes two sets and checks if one 
# # is a subset or superset of the other.

# def check_subset_superset(set1, set2):
#     return {
#         "set1 ⊆ set2": set1.issubset(set2),
#         "set1 ⊇ set2": set1.issuperset(set2),
#         "set2 ⊆ set1": set2.issubset(set1),
#         "set2 ⊇ set1": set2.issuperset(set1)
#     }

# print(check_subset_superset({1, 2}, {1, 2, 3}))  
# # {'set1 ⊆ set2': True, 'set1 ⊇ set2': False, 'set2 ⊆ set1': False, 'set2 ⊇ set1': True}







# # -Set of Frozensets: Create a set that contains frozensets. Perform set operations (e.g., union,
# #  intersection) on it.

# def frozenset_operations():
#     s1 = frozenset({1, 2, 3})
#     s2 = frozenset({3, 4, 5})
#     s3 = frozenset({5, 6, 7})

#     set_of_frozensets = {s1, s2, s3}
    
#     # Performing operations (example union using normal sets)
#     union_result = set().union(*set_of_frozensets)
#     intersection_result = set.intersection(*set_of_frozensets)
    
#     return {
#         "Set of Frozensets": set_of_frozensets,
#         "Union": union_result,
#         "Intersection": intersection_result
#     }

# # Example
# print(frozenset_operations())
# {'Set of Frozensets': {frozenset({1, 2, 3}), frozenset({3, 4, 5}), frozenset({5, 6, 7})}, 
#  'Union': {1, 2, 3, 4, 5, 6, 7}, 'Intersection': set()}


















# # Mixed Questions (List, Tuple, Set):
# # -Remove Elements from List and Set: Given a list and a set, write a function that removes
# #  the elements from the list that exist in the set, without modifying the original set.

# def remove_elements(lst, s):
#     return [item for item in lst if item not in s]


# print(remove_elements([1, 2, 3, 4, 5], {2, 4}))  # [1, 3, 5]





# # -Find the Intersection of a List of Tuples: Given a list of tuples (each tuple has two elements), 
# # write a Python function to find the intersection of the first elements of all the tuples and 
# # return the result as a set.

# def tuple_list_intersection(tuples):
#     if not tuples:
#         return set()
    
#     first_elements = [t[0] for t in tuples]
#     return set(first_elements)
# # 
# # Example
# print(tuple_list_intersection([(1, 'a'), (1, 'b'), (2, 'c'), (2, 'd'), (3, 'e')]))
# # {1, 2, 3}








# # -Merge List of Sets: Write a function that takes a list of sets and merges them into one set,
# #  removing any duplicate elements.

# def merge_sets(set_list):
#     return set().union(*set_list)

# # Example
# print(merge_sets([{1, 2, 3}, {3, 4, 5}, {5, 6, 7}]))  # {1, 2, 3, 4, 5, 6, 7}












# # -List and Tuple Frequency: Given a list and a tuple, write a Python program to count how many 
# # times the elements from the tuple appear in the list.

# from collections import Counter

# def count_tuple_elements_in_list(lst, tup):
#     counter = Counter(lst)
#     return {item: counter[item] for item in tup}

# # Example
# print(count_tuple_elements_in_list([1, 2, 3, 2, 4, 1, 2, 3], (2, 3, 5)))  
# # {2: 3, 3: 2, 5: 0}
