# general library connection
import sys
sys.dont_write_bytecode = True
from main import skel

# generate number between 1 and 10
randomnumber = skel.randNum(1, 10)

# ask user for input
userguess = skel.requestUserInput("I'm thinking of a number between 1 and 10. What is it?\n")

# game logic
if userguess == str(randomnumber):
    print("You guessed correctly!")
else:
    print(f"You lost! The number was {str(randomnumber)}.")
