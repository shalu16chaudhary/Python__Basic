# import queue
# import random
# import string
# from collections import deque 
# class Queue:
#     def __init__(self):
#         self.queue = deque()

#     def enqueue(self , data):
#         self.queue.append(data)

#     def dequeue(self):
#         if not self.is_empty():
#             return self.queue.popleft()
#         return "Queue is empty"
    
#     def is_empty(self):
#         return len(self.queue) ==0
    
# q = Queue()
# q.enqueue(5)
# q.enqueue(15)
# print(q.dequeue())




# def generate_password(length=12):
#     q = queue.Queue()
    
#     # Define character sets
#     characters = string.ascii_letters + string.digits + string.punctuation
    
#     # Enqueue random characters into the queue
#     for _ in range(length):
#         q.put(random.choice(characters))
    
#     # Dequeue characters to form the password
#     password = ''.join([q.get() for _ in range(length)])
#     return password

# # Generate and print a random password of 12 characters
# print("Generated Password:", generate_password(12))









# import queue
# import random
# import time
# import threading

# class BankQueueSystem:
#     def __init__(self, num_tellers):
#         self.customer_queue = queue.Queue()  # FIFO queue for customers
#         self.token_counter = 1  # Unique token number assignment
#         self.num_tellers = num_tellers  # Number of tellers
#         self.teller_status = [None] * num_tellers  # Store current customer at each teller

#     def generate_customer(self):
#         """Simulates a new customer arriving at the bank."""
#         service_type = random.choice(["Deposit", "Withdrawal"])
#         token_number = self.token_counter
#         self.token_counter += 1

#         self.customer_queue.put((token_number, service_type))  # Add customer to queue
#         print(f"Customer {token_number} (Service: {service_type}) entered the bank.")

#     def serve_customer(self, teller_id):
#         """Teller processes the next customer in queue if available."""
#         while True:
#             if not self.customer_queue.empty():
#                 token_number, service_type = self.customer_queue.get()
#                 self.teller_status[teller_id] = token_number  # Teller is busy with this customer
#                 print(f"Teller {teller_id + 1} is serving Customer {token_number} ({service_type}).")

#                 processing_time = random.randint(2, 5)  # Simulating random service time
#                 time.sleep(processing_time)

#                 print(f"Teller {teller_id + 1} finished serving Customer {token_number}.")
#                 self.teller_status[teller_id] = None  # Teller is now free

#             time.sleep(1)  # Small delay before checking the queue again

#     def start_simulation(self, total_customers):
#         """Starts the bank queue simulation."""
#         # Start teller threads
#         tellers = []
#         for i in range(self.num_tellers):
#             teller_thread = threading.Thread(target=self.serve_customer, args=(i,))
#             teller_thread.daemon = True
#             tellers.append(teller_thread)
#             teller_thread.start()

#         # Generate customers randomly
#         for _ in range(total_customers):
#             self.generate_customer()
#             time.sleep(random.randint(1, 3))  # Random arrival times

#         # Wait for tellers to finish processing remaining customers
#         while not self.customer_queue.empty():
#             time.sleep(1)

#         print("Bank is now closed. All customers have been served.")

# # Run the simulation with 3 tellers and 10 customers
# bank = BankQueueSystem(num_tellers=3)
# bank.start_simulation(total_customers=10)





# from collections import deque
# import random
# import time

# # Define the Customer class
# class Customer:
#     def _init_(self, token_number, service_type):
#         self.token_number = token_number
#         self.service_type = service_type

#     def _str_(self):
#         return f"Token {self.token_number} ({self.service_type})"

# # Define the Teller class
# class Teller:
#     def _init_(self, teller_id):
#         self.teller_id = teller_id
#         self.is_busy = False

#     def serve_customer(self, customer):
#         if not self.is_busy:
#             self.is_busy = True
#             print(f"Customer with {customer} is being served by Teller {self.teller_id}.")
#             # Simulate serving time (random between 1 to 3 seconds)
#             time.sleep(random.randint(1, 3))
#             print(f"Teller {self.teller_id} finished serving {customer}.")
#             self.is_busy = False
#             return True
#         return False

# # Define the Bank class to simulate the process
# class BankQueueSimulation:
#     def _init_(self, num_tellers):
#         self.customers_queue = deque()  # Queue for customers
#         self.tellers = [Teller(i + 1) for i in range(num_tellers)]  # Create multiple tellers
#         self.token_counter = 1  # Token counter to assign new tokens

#     def add_customer(self, service_type):
#         # Add a customer with a new token number and the service type
#         customer = Customer(self.token_counter, service_type)
#         self.customers_queue.append(customer)
#         print(f"Customer with Token {self.token_counter} arrived for {service_type}.")
#         self.token_counter += 1

#     def serve_customers(self):
#         while self.customers_queue:
#             for teller in self.tellers:
#                 if self.customers_queue:
#                     customer = self.customers_queue[0]
#                     if teller.serve_customer(customer):
#                         self.customers_queue.popleft()  # Remove customer from queue after they are served
#                         break

# # Simulating the Bank Queue
# def simulate_bank_queue():
#     bank = BankQueueSimulation(num_tellers=3)  # Bank with 3 tellers

#     # Randomly adding customers to the bank queue
#     for _ in range(10):  # Let's simulate 10 customers
#         service_type = random.choice(["Deposit", "Withdrawal"])
#         bank.add_customer(service_type)
#         time.sleep(1)  # Simulate time delay between arrivals

#     # Serve the customers
#     bank.serve_customers()

# # Run the simulation
# simulate_bank_queue()



from collections import deque
import random
import time
import queue

customer_queue = queue.Queue()
def add_customer(token):
    customer_queue.put(token)  
    print(f"Customer {token} joined the queue")

def serve_customer():
    if not customer_queue.empty():  # Check if queue is not empty
        token = customer_queue.get()  # Get the first customer
        print(f"Serving Customer {token}...")
        time.sleep(2)  # Simulate service time
        print(f"Customer {token} has been served.")
    else:
        print("No customers in queue.")

# Adding customers to the queue
add_customer(1)
add_customer(2)
add_customer(3)

# Serving customers one by one
serve_customer()
serve_customer()
serve_customer()

# # Trying to serve when the queue is empty
# serve_customer()


    