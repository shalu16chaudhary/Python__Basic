class CarBuyingService:
    def __init__(self):
        self.car_prices = {
            "1": ("Hatchback", 535000),
            "2": ("Saloon", 495000),
            "3": ("Estate", 625000)
        }
        self.extras = {
            "1": ("Set of luxury seats", 45000),
            "2": ("Satellite navigation", 5500),
            "3": ("Parking sensors", 10000),
            "4": ("Bluetooth connectivity", 350),
            "5": ("Sound system", 1000)
        }
        self.trade_in_min = 10000
        self.trade_in_max = 100000
    
    def get_car_price(self, model_choice):
        return self.car_prices.get(model_choice, ("Invalid", 0))
    
    def get_extras_price(self, extra_choice):
        return self.extras.get(extra_choice, ("None", 0))
    
    def calculate_price(self, model_choice, extra_choice, is_existing_customer, trade_in_value):
        model, base_price = self.get_car_price(model_choice)
        extra, extras_price = self.get_extras_price(extra_choice)
        
        if base_price == 0:
            return "Invalid car model selection."
        if trade_in_value is not None and not (self.trade_in_min <= trade_in_value <= self.trade_in_max):
            return "Invalid trade-in value."
        
        total_price = base_price + extras_price
        
        if is_existing_customer:
            base_price *= 0.90
            extras_price *= 0.90
        
        if trade_in_value is None:
            total_price *= 0.95
        else:
            total_price -= trade_in_value
        
        return model, extra, round(total_price, 2)
    
    def calculate_payment(self, total_price, payment_choice):
        if payment_choice == "1":
            final_amount = total_price * 0.99
            return "Full Payment (1% cashback)", round(final_amount, 2), 0
        elif payment_choice == "2":
            monthly_payment = total_price / 48
            return "Monthly (4 years)", total_price, round(monthly_payment, 2)
        elif payment_choice == "3":
            final_amount = total_price * 1.05
            monthly_payment = final_amount / 84
            return "Monthly (7 years, 5% interest)", round(final_amount, 2), round(monthly_payment, 2)
        else:
            return "Invalid payment choice", 0, 0


# User Interaction
service = CarBuyingService()
print("WELCOME TO SNAZZY AUTOS !!!")
interest = input("Are you interested to buy a car? Type 1 for 'Yes' and 2 for 'No': ")
if interest != "1":
    print("Thank you for visiting!")
else:
    model_choice = input("\nWhich car model are you interested to buy?\n1. Hatchback Rs. 5.35 lakh\n2. Saloon Rs. 4.95 lakh\n3. Estate Rs. 6.25 lakh\nType your choice: ")
    extra_choice = input("\nWhich add-on feature are you interested in?\n1. Set of luxury seats Rs 45000\n2. Satellite navigation Rs 5500\n3. Parking sensors Rs 10000\n4. Bluetooth connectivity Rs 350\n5. Sound system Rs 1000\n6. None\nType your choice: ")
    is_existing = input("\nAre you an existing customer? Type 1 for 'Yes' (10% discount) and 2 for 'No' (5% discount): ") == "1"
    trade_in_choice = input("\nDo you have an old car for exchange? Type 1 for Yes and 2 for No: ")
    trade_in_value = None if trade_in_choice == "2" else int(input("Enter the value of old car (Rs 10,000 - Rs 1,00,000): "))
    
    model, extra, final_price = service.calculate_price(model_choice, extra_choice, is_existing, trade_in_value)
    
    print(f"\nThe model of the car is '{model}', worth Rs {service.car_prices[model_choice][1]} with add-on feature of '{extra}', worth Rs {service.extras.get(extra_choice, (None, 0))[1]}.")
    print(f"The total value of the car is Rs {final_price}.")
    
    payment_choice = input("\nPlease enter your payment option:\n1. Full Amount at 1% cashback\n2. Equal monthly payments for four years at no charge\n3. Equal monthly payments over seven years at 5% surcharge\nType your choice: ")
    payment_plan, net_amount, monthly_amount = service.calculate_payment(final_price, payment_choice)
    print(f"\nThe option of payment chosen is '{payment_plan}'. Net amount to be paid is Rs {net_amount}.")
    if monthly_amount > 0:
        print(f"Number of installments: 48 months and amount of each installment is Rs {monthly_amount}.")
    print("The amount of cashback is Rs 0.")
    print("\nThank you for your time!!!")
