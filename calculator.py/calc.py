import sys
import os
from art import logo
from functions import *
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

def calculator_funct():
    print(logo)
    calculator = True

    first_number = float(input("What's the first number?: "))
    for operator in operations:
        print(operator)
    while calculator:
        operator_function = input("Pick an operator: ")
        second_number = float(input("What's the second number?: "))
        calculation_function = operations[operator_function]
        answer = calculation_function(first_number,second_number)
        print(f"{first_number} {operator_function} {second_number} = {answer}")

        last_choice = input(f"Type 'y' to continue calculating with {answer}, type 'n' to start a new calculation or 'e' to exit:  ")
        if last_choice == 'n':
            os.system('cls')
            calculator_funct()
        elif last_choice == 'e':
            print("Thanks for using our calculator")
            calculator = False
        else:
            first_number = answer
            
calculator_funct()