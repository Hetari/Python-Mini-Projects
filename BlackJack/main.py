import random
from os import system


def random_card():
    card = random.choice(cards)
    return card


def score(item):
    score = sum(item)
    if 11 in item and score > 21:
        score -= 10
    return score


def win(player, dealer):
    score(player)
    score(dealer)

    if score(dealer) > score(player) or score(player) > 21:
        print("You loos!")
    elif score(dealer) < score(player) or score(dealer) >= 21:
        print("You win!")
    elif score(dealer) == score(player) and score(player) <= 21:
        print("Tie!")

    print(f"Player cards: {player}, dealer cards: {dealer}")
    print(f"Player points: {score(player)}, dealer points: {score(dealer)}")


game = True
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

while (game):
    start = input("Do you want to play a game of BlackJack (yes/no): ")
    if start[0].lower() != 'y':
        print("Goodbye, see u later!")
        break
    system('cls')

    player_cards = [random_card(), random_card()]
    dealer_cards = [random_card(), random_card()]
    print(f"Your cards are {(player_cards)
                            }, current score: {score(player_cards)}")
    print(f"Dealer's first card is: {dealer_cards[0]}")

    another_card = input("Do you want a another card? Type 'no' to pass: ")
    if score(dealer_cards) != 0 and score(dealer_cards) < 17:
        dealer_cards.append(random_card())
    if another_card[0] == 'y':
        player_cards.append(random_card())
        print(f"Your cards are {(player_cards)
                                }, current score: {score(player_cards)}")
        print(f"Dealer's first card is: {dealer_cards[0]}")
        win(player_cards, dealer_cards)
    else:
        win(player_cards, dealer_cards)
