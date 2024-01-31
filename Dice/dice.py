import random
import sys
import os

sys.path.append(os.path.dirname(os.path.realpath(__file__)))
import random
from art import die

die_number = random.randint(0,5)
print(die[die_number])