# Ques1- Write a Python program to create a class representing a Circle.
#  Include methods to calculate its area and perimeter.
class circle:
    def calculateArea(self,r):
        self.radius = r
        print(3.14*r*r)
    def calculatePerimeter(self,r):
        self.radius=r
        print(2*3.14*r)

obj = circle()
obj.calculateArea(7)
obj.calculatePerimeter(7)










# Ques2- Write a Python program to create a person class.Include attributes like
#  name, country and date of birth. Implement a method to determine the person's age

class person:
    def __init__(self,name ,country , dob):
        self.name= name 
        self.country = country
        self.dob = dob
    def age(self,age):
        self.age = age
        print(f"{self.name} has {self.age}")   
obj = person("shalu","India","16feb")
print(obj.name)  
print(obj.country)
print(obj.dob) 
obj.age(20)
    










# Ques3- Write a Python program to create a class that represents a shape.Include methods
#  to calculate its area and perimeter.Implement subclasses for different shapes
#  like circle, triangle, and square.

class shape:
    def area(self):
        pass
    def perimeter(self):
        pass

class circle(shape):
    def __init__(self,r):
        self.radius=r
    def area(self,r):
        print(3.14*r*r)
    def perimeter(self,r):
        print(2*3.14*r)

class triangle(shape):
    def __init__(self,a,b,c,h):
        self.side1 = a
        self.side2 = b
        self.side3 = c
        self.height = h

    def area(self,b,h):
        print((1/2)*b*h)

    def perimeter(self,a,b,c):
        print(a+b+c) 

class square(shape):
    def __init__(self,l):
        self.side = l

    def area(self,l):
        # self.length = l
        print(l*l)

    def perimeter(self,l):
        # self.length=l
        print(4*l)  
obj1 = square(4)
obj2= triangle(1,2,3,4)
obj3 = circle(7)   
obj1.area(4)
obj1.perimeter(4)
obj2.area(2,4)
obj2.perimeter(1,2,3)
obj3.area(7)
obj3.perimeter(7)















# Ques4- Write a Python program to create a class representing a shopping cart. Include 
# methods for adding and removing items, and calculating the total price.

class ShoppingCart:
    def __init__(self):
        self.items = {} 
    
    def add_item(self, item_name, price, quantity=1):
        if item_name in self.items:
            self.items[item_name]['quantity'] += quantity
        else:
            self.items[item_name] = {'price': price, 'quantity': quantity}
    
    def remove_item(self, item_name, quantity=1):
        if item_name in self.items:
            if self.items[item_name]['quantity'] > quantity:
                self.items[item_name]['quantity'] -= quantity
            else:
                del self.items[item_name]
        else:
            print("Item not found in cart.")
    
    def calculate_total(self):
        """Calculates the total price of items in the cart."""
        return sum(item['price'] * item['quantity'] for item in self.items.values())
    
    def show_cart(self):
        """Displays the items in the shopping cart."""
        if not self.items:
            print("Your cart is empty.")
        else:
            print("Shopping Cart:")
            for item, details in self.items.items():
                print(f"{item}: ${details['price']} x {details['quantity']}")
            print(f"Total: ${self.calculate_total():.2f}")

# Example usage
cart = ShoppingCart()
cart.add_item("Apple", 0.99, 3)
cart.add_item("Banana", 0.59, 2)
cart.show_cart()
cart.remove_item("Apple", 1)
cart.show_cart()
print("Total Price:", cart.calculate_total())


















# Ques6- Write a Python program to create a class representing a bank. Include methods 
# for managing customer accounts and transactions.


class Bank:
    def __init__(self):
        self.accounts = {}  # Dictionary to store customer accounts
    
    def create_account(self, account_number, name, balance=0.0):
        """Creates a new bank account."""
        if account_number in self.accounts:
            print("Account already exists.")
        else:
            self.accounts[account_number] = {'name': name, 'balance': balance}
            print(f"Account created for {name} with balance ${balance:.2f}")
    
    def deposit(self, account_number, amount):
        """Deposits money into an account."""
        if account_number in self.accounts:
            self.accounts[account_number]['balance'] += amount
            print(f"Deposited ${amount:.2f} into account {account_number}")
        else:
            print("Account not found.")
    
    def withdraw(self, account_number, amount):
        """Withdraws money from an account."""
        if account_number in self.accounts:
            if self.accounts[account_number]['balance'] >= amount:
                self.accounts[account_number]['balance'] -= amount
                print(f"Withdrew ${amount:.2f} from account {account_number}")
            else:
                print("Insufficient funds.")
        else:
            print("Account not found.")
    
    def check_balance(self, account_number):
        """Checks the balance of an account."""
        if account_number in self.accounts:
            print(f"Account {account_number} balance: ${self.accounts[account_number]['balance']:.2f}")
        else:
            print("Account not found.")
    
    def show_accounts(self):
        """Displays all customer accounts."""
        if not self.accounts:
            print("No accounts found.")
        else:
            print("Bank Accounts:")
            for acc, details in self.accounts.items():
                print(f"{acc}: {details['name']} - Balance: ${details['balance']:.2f}")

# Example usage
bank = Bank()
bank.create_account(101, "Alice", 500.0)
bank.create_account(102, "Bob", 300.0)
bank.deposit(101, 200)
bank.withdraw(102, 100)
bank.check_balance(101)
bank.show_accounts()




















# Ques7-:
# Part 1-Create a Class with instance attributes.
# Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.
# Part 2-Create a Vehicle class without any variables and methods
# Part 3-Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
# Given:
# class Vehicle:

#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage

# Part 4-Class Inheritance
# Given:
# Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of 50.
# Use the following code for your parent Vehicle class.

# class Vehicle:
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage

#     def seating_capacity(self, capacity):
#         return f"The seating capacity of a {self.name} is {capacity} passengers"

# Expected Output:

# The seating capacity of a bus is 50 passengers.

# Reference or problem solve through:
# Inheritance in Python
# Polymorphism in Python

# Part 5- Define a property that must have the same value for every class instance (object)
# Define a class attribute”color” with a default value white. I.e., Every Vehicle should be white.

# Use the following code for this exercise.

# class Vehicle:

#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage

# class Bus(Vehicle):
#     pass

# class Car(Vehicle):
#     pass

# Expected Output:

# Color: White, Vehicle name: School Volvo, Speed: 180, Mileage: 12
# Color: White, Vehicle name: Audi Q5, Speed: 240, Mileage: 18

# Part 6- Class Inheritance
# Given:
# Create a Bus child class that inherits from the Vehicle class. The default fare charge of any vehicle is seating capacity * 100. If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenance charge. So total fare for bus instance will become the final amount = total fare + 10% of the total fare.
# Note: The bus seating capacity is 50. so the final fare amount should be 5500. You need to override the fare() method of a Vehicle class in Bus class.

# Use the following code for your parent Vehicle class. We need to access the parent class from inside a method of a child class.

# class Vehicle:
#     def __init__(self, name, mileage, capacity):
#         self.name = name
#         self.mileage = mileage
#         self.capacity = capacity

#     def fare(self):
#         return self.capacity * 100

# class Bus(Vehicle):
#     pass

# School_bus = Bus("School Volvo", 12, 50)
# print("Total Bus fare is:", School_bus.fare())

# Expected Output:

# Total Bus fare is: 5500.0

# Part 7- Check type of an object
# Write a program to determine which class a given Bus object belongs to.

# Given:
# class Vehicle:
#     def __init__(self, name, mileage, capacity):
#         self.name = name
#         self.mileage = mileage
#         self.capacity = capacity

# class Bus(Vehicle):
#     pass

# School_bus = Bus("School Volvo", 12, 50)

# Part 8- Determine if School_bus is also an instance of the Vehicle class
# Given:

# class Vehicle:
#     def __init__(self, name, mileage, capacity):
#         self.name = name
#         self.mileage = mileage
#         self.capacity = capacity

# class Bus(Vehicle):
#     pass

# School_bus = Bus("School Volvo", 12, 50)








class Vehicle:
    color = "White"
    
    def __init__(self, name, max_speed, mileage, capacity=50):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.capacity = capacity
    
    def seating_capacity(self, capacity=None):
        if capacity is None:
            capacity = self.capacity
        return f"The seating capacity of a {self.name} is {capacity} passengers"
    
    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def fare(self):
        total_fare = super().fare()
        return total_fare + (0.1 * total_fare)

class Car(Vehicle):
    pass

# Part 1: Create a Class with instance attributes
vehicle1 = Vehicle("Car", 240, 18)
print(vehicle1.name, vehicle1.max_speed, vehicle1.mileage)

# Part 2: Create a Vehicle class without any variables and methods
class EmptyVehicle:
    pass

# Part 3: Create a child class Bus that inherits Vehicle
bus1 = Bus("School Volvo", 180, 12)
print(bus1.seating_capacity())

# Part 4: Class Inheritance
bus2 = Bus("City Bus", 150, 10)
print(bus2.seating_capacity())

# Part 5: Define a property that must have the same value for every class instance
car1 = Car("Audi Q5", 220, 15)
print(f"Color: {car1.color}, Vehicle name: {car1.name}, Speed: {car1.max_speed}, Mileage: {car1.mileage}")

# Part 6: Class Inheritance with fare calculation
total_fare = bus1.fare()
print(f"Total Bus fare is: {total_fare}")

# Part 7: Check type of an object
print(type(bus1))

# Part 8: Determine if School_bus is also an instance of the Vehicle class
print(isinstance(bus1, Vehicle))















