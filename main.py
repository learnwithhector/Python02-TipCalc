print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
rate = int(input("How much tip would you like to give? 10, 12 or 15%? "))
num_diners = int(input("How many people split the bill? "))

tip = bill * (rate / 100)
total = bill + tip

print(f"Each person should pay ${total / num_diners :.2f}")
