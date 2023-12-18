import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
num_letters= int(input("How many letters would you like in your password? ")) 
num_symbols = int(input(f"How many symbols would you like? "))
num_numbers = int(input(f"How many numbers would you like? "))
all_num = num_letters + num_numbers + num_symbols

password = []

for x in range(0, num_letters):
    index = random.randint(0, len(letters))
    password.append(letters[index])

for x in range(0, num_symbols):
    index = random.randint(0, len(symbols))
    password.append(symbols[index])

for x in range(0, num_numbers):
    index = random.randint(0, len(numbers))
    password.append(numbers[index])

random.shuffle(password)
print("".join(password))