import sys
import os

import random
from logo import logo
from logo import stages
from words import word_list

sys.path.append(os.path.dirname(os.path.realpath(__file__)))

print(logo)
wordRandom = random.choice(word_list)
word_length = len(wordRandom)
# print(wordRandom)

endGame = False
lives = 6

display = []
lettersAlreadyChose = []
for dash in range(word_length):
    display += "_"

while not endGame:
    guess = input("Guess a letter: ").lower()

    os.system('cls')

    if guess in display:
        print(f"You have already guessed {guess}")

    for position in range(word_length):
        letter = wordRandom[position]
        if letter == guess:
            display[position] = letter

    if guess not in wordRandom:
        print(f"The letter '{guess}' is not in the word. You lose a life")
        lives -= 1

    print(f"{' '.join(display)}")

    if "_" not in display:
        endGame = True
        print("You Win")
    elif lives == 0:
        endGame = True
        print("You Lose")

    print(stages[lives])
