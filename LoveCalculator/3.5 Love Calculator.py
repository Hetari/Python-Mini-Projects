print("Welcome to Love Calculator")
his_name, her_name = input("Enter his and her name: ").lower().split()

true = sum(his_name.count(letter) for letter in 'true') + \
    sum(her_name.count(letter) for letter in 'true')
love = sum(his_name.count(letter) for letter in 'love') + \
    sum(her_name.count(letter) for letter in 'love')

love_score = true * 10 + love

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you are Coke and Mentos")
elif 40 <= love_score <= 50:
    print(f"Your score is {love_score}, you are alright together")
else:
    print(f"Your score is {love_score}")
