import random
import new_words
import Hangman_visual
from os import system

word_list = new_words.words
chosen_word = random.choice(word_list)

display = []
for _ in chosen_word:
    display += '_'

guess_letters = []
lives = 6

while("".join(display) != chosen_word and lives > 0):
    
    print("  ".join(display))
    guess = input("Enter a char: ").lower()

    system('cls')
    
    for index in range(len(chosen_word)):
        if guess == chosen_word[index]:
            display[index] = guess
            
    if guess in guess_letters:
        print(f"You've already guessed {guess}")
    elif guess in chosen_word and guess not in guess_letters:
        print(f"You've guessed {guess} correctly!")
    elif guess not in chosen_word and guess not in guess_letters:
        print(f"You guessed {guess}, that's not in the word. You lose a life")
        lives -= 1
    
    guess_letters.append(guess)
    
    print("\nLives:", lives,"\n")
    print(Hangman_visual.hangman[lives])

if "".join(display) == chosen_word:
    print(f"You won\nThe word was {chosen_word}")
else:
    print(Hangman_visual.hangman[lives])
    print(f"You lose\nThe correct word was {chosen_word}")