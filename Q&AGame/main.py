import random
from os import system
from game_data import data
import art


# get a random integer in the range of list
def rand_one():
    rand = random.randint(0, len(data) - 1)
    return rand


# Know if the user get the answer correctly
def higher_lower(letter, list):
    '''Check if the user get the answer correctly'''
    # This my idea to know if the user entered A or B 😅
    if list[position_A]['follower_count'] > list[position_B]['follower_count']:
        return letter.upper() == 'A'
    else:
        return letter.upper() == 'B'


score = 0
print(art.logo)

position_A = rand_one()
while (True):
    position_B = rand_one()
    print(f"Compare A: {data[position_A]['name']}, a {
          data[position_A]['description']}, from {data[position_A]['country']}")

    print(art.vs)

    print(f"Compare A: {data[position_B]['name']}, a {
          data[position_B]['description']}, from {data[position_B]['country']}")

    followers = input("Who has more followers? 'A' or 'B': ")
    if higher_lower(followers, data) != True:
        system('cls')
        print(art.logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        break
    else:
        position_A = position_B
        system('cls')
        score += 1
        print(art.logo)
        print(f"You're right! Current score: {score}")
