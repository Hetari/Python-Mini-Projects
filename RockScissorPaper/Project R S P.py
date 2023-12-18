import random

while True:
    choices = ["rock","paper","scissor"]
    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, scissor, paper?: ").lower()

    if player == computer:
        print("player:",player)
        print("computer:",computer)
        print("Tie!")
    elif player == "rock":
        if computer == "paper":
            print("player:",player)
            print("computer:",computer)
            print("You lose!")
        if computer == "scissor":
            print("player:",player)
            print("computer:",computer)
            print("You win!")
    elif player == "paper":
        if computer == "scissor":
            print("player:",player)
            print("computer:",computer)
            print("You lose!")
        if computer == "rock":
            print("player:",player)
            print("computer:",computer)
            print("You win!")
    elif player == "scissor":
        if computer == "rock":
            print("player:",player)
            print("computer:",computer)
            print("You lose!")
        if computer == "paper":
            print("player:",player)
            print("computer:",computer)
            print("You win!")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        break

print("Bye!")