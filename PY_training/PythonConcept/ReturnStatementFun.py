# In Python, return is used in a function to exit the function and send a result or value back to the caller. When the return statement is executed, the function terminates,
#  and the value (if provided) is returned to the code that called the function.
def add_numbers(a, b):
    result = a + b
    return result  # Returning the sum of a and b

sum_value = add_numbers(3, 5)  # Function call
print(sum_value)  # This will print 8


# Key Points:
# Exits the function: Once return is executed, the function stops running further code.
# Returns a value: The value or expression after return gets sent back to the caller.
# Optional: You can use return with or without a value. If no value is provided, 
# None is returned by default.
def greet(name):
    print(f"Hello, {name}!")
    # No return statement here, so it returns None by default.

greet("Alice")


# 1. Returning Multiple Values:
# You can return multiple values from a function by separating them with commas. 
# Python will return these as a tuple.

def get_coordinates():
    latitude = 40.7128
    longitude = -74.0060
    return latitude, longitude  # Returning multiple values

coords = get_coordinates()  # This will return a tuple
print(coords)  # Output: (40.7128, -74.0060)


#In this case, the function returns two values (latitude and longitude), and they are automatically packed into a tuple.

# 2. Returning No Value (Implicit None)
# If a function doesn't include a return statement, or if the return is used without a value, 
# Python will return None by default.

def print_message(message):
    print(message)
    # No return statement, so None is returned by default

result = print_message("Hello!")
print(result)  # Output: None

# Even though we print the message inside the function, there is no explicit return, so None is returned.

# 3. Returning Expressions
# You can return the result of an expression directly.

def square(x):
    return x ** 2  # Returning the square of x directly

result = square(4)
print(result)  # Output: 16


# Instead of storing the result in a variable and returning it, we directly return the result of the expression x ** 2.

# 4. Returning from a Conditional Block
# You can use return within conditional statements to return different values depending on the conditions.

def check_positive(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

result = check_positive(10)
print(result)  # Output: Positive

# Here, the function checks if a number is positive, negative, or zero and returns the corresponding string.

# 5. Returning Early (Exiting the Function Early)
# You can use return at the beginning of a function to exit early under certain conditions. This can be useful for validation or handling special cases.