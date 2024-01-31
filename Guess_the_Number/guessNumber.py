import random 
from art import logo
from functions import lives_given
from functions import check_answer
import sys
import os

sys.path.append(os.path.dirname(os.path.realpath(__file__)))

game = True
lives = 0
DIFFICULTY_LEVEL = ['easy','hard']

while game == True:
    print(logo)
    random_number = random.randint(1,100)
    print("Welcome to the Number guessing game!")
    print("Im thinking of a number between 1 and 100.")
    dificulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    while dificulty not in DIFFICULTY_LEVEL:
        print("Please choose a valid option.")
        dificulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    lives = lives_given(dificulty)
    print(f"You have {lives} attempts to guess the number.")

    while True:
        guessed_number = int(input("Make a guess: "))
        while guessed_number <1 or guessed_number >100:
            print("Invalid entry, please type a number between 1 and 100")
            guessed_number = int(input("Make a guess: "))

        lives = check_answer(guessed_number, random_number,lives)     
        if  lives <=0 or  guessed_number==random_number:
            break
    last_choice = input("Would you like to play again (y/n)? ")
    last_choice = last_choice.lower()
    if  last_choice == 'n':
        print("Thank you for playing!")
        game = False
    else:
        os.system('cls')