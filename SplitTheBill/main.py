print("Welcome to the tip calculator")

bill = eval(input("Total bill? "))
tip = eval(input("Percent of the tip? "))
people = eval(input("The amount of people how will split the bill? "))

total_bill = (bill * (1 + tip / 100))  / people

print(f"Each person should pay: {round(total_bill, 2)}$")