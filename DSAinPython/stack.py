import collections
# class stack:
#     def __init__(self):
#         self.stack = []

#     def push(self ,data):
#         self.stack.append(data)

#     def pop(self):
#         if not self.is_empty():
#             return self.stack.pop()
#         return "stack is empty"
    
#     def peek(self):
#         if not self.is_empty():
#             return self.stack[-1]
#         return "stack is empty"
    
#     def is_empty(self):
#         return len(self.stack)==0
    
#     def size(self):
#         return len(self.stack)

# s = stack()
# s.push(10)
# s.push(20)
# s.push(60)
# s.push(90)
# s.push(100)
# print(s.peek())
# # print(s.pop())




stack = []   
stack.append(10)
stack.append(20)
stack.append(30)

print("stack after pushing element:",stack)
top = stack.pop()
print("popped item:",top)
print("stack after popping an element:",stack)
top = stack[0]
print("top element:",top)

if not stack:
    print("stack is empty.")
else:
    print("stack is not empty.")


from collections import deque
stack = deque()
stack.append(1)
stack.append(2)
print(stack.pop())   #output 2





# def isValid(s):
#     stack = []
#     for char in s:
#         if char == '(':
#             stack.append(char)
#         elif char == ')':
#             if not stack:
#                 return False
#             stack.pop()
    
#     return len(stack) == 0

# # Test cases
# print(isValid("()"))       # True
# print(isValid("(())"))     # True
# print(isValid("(()"))      # Fals
# print(isValid("())"))      # False






# def is_valid(s):
#     stack = []
#     # paren = {}
#     for char in s:
#         if char == '(':
#             stack.append(char)
#         elif char == ')':
#             if not stack:
#                 return False
#             stack.pop()

# print(is_valid("()"))  

# def isvalid(s):
#     stack = deque()
#     mapping = {")":"(","}":"{","]":"["}

#     for char in s:
#         if char in mapping:
#             top_element = stack.pop() if stack else '#'
#             if mapping[char] != top_element:
#                 return "false"
#         else:
#                 stack.append(char)
#     return "true" if not stack else "false"

# print(isvalid("({})"))
# print(isvalid("()[]{}"))
# print(isvalid("(]"))
# print(isvalid("([)]"))
# print(isvalid("{[]}"))


# def reverse_string(s):
#     stack = list(s)  # String ko list (stack) me convert karna
#     reversed_str = "".join(stack[::-1])  # List ko reverse karke wapas string banana
#     return reversed_str

# # Example usage
# print(reverse_string("hello"))  # Output: "olleh"

    
def reverse_string(s):
    stack = []
    
    # Push all characters to stack
    for char in s:
        stack.append(char)
    
    # Pop characters from stack to reverse the string
    reversed_str = ""
    while stack:
        reversed_str += stack.pop()
    
    return reversed_str

# Example usage
input_str = "hello"
print(reverse_string(input_str))  # Output: "olleh"



# reverse a string 
# stack = deque()
# stack.append("hello")
# for char in stack:
#     print(stack.pop())
#     print(stack.reverse())   



def reversed_string(s):
    stack = list(s)
    reversed_string = ",".join(stack[::-1])
    return reversed_string


print(reversed_string("hello"))