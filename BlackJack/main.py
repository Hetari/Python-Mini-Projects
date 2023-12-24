import random
import os


def random_card():
    card = random.choice(cards)
    return card


def score(item):
    score = sum(item)
    if 11 in item and score > 21:
        score -= 10
    return score


def game_result(player, dealer):
    score(player)
    score(dealer)

    if score(dealer) > score(player) or score(player) > 21:
        print("You lose!")
    elif score(dealer) < score(player) or score(dealer) >= 21:
        print("You win!")
    elif score(dealer) == score(player) and score(player) <= 21:
        print("Tie!")

    print(f"Player's cards: {player}, dealer's cards: {dealer}")
    print(f"Player's points: {score(player)}, dealer's points: {score(dealer)}")


game = True
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

while (game):
    start = input("Do you want to play a game of BlackJack (yes/no) [default <no>]: ") or 'no'
    if start[0].lower() != 'y':
        print("Goodbye, see u later!")
        break
    clear_screen = 'cls' if os.name == 'nt' else 'clear'
    os.system(clear_screen)

    player_cards = [random_card(), random_card()]
    dealer_cards = [random_card(), random_card()]
    print(f"Your cards are {(player_cards)}, current score: {score(player_cards)}")
    print(f"Dealer's first card is: {dealer_cards[0]}")

    
    another_card = input("Do you want a another card? (yes/no) [default <no>]: ") or 'no'
    if score(dealer_cards) != 0 and score(dealer_cards) < 17:
        dealer_cards.append(random_card())
        
    
    if another_card[0] == 'y':
        player_cards.append(random_card())
        print(f"Your cards are {(player_cards)}, current score: {score(player_cards)}")
        print(f"Dealer's first card is: {dealer_cards[0]}")
        game_result(player_cards, dealer_cards)
    else:
        game_result(player_cards, dealer_cards)
