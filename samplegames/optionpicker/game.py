# General library connection
import sys
sys.dont_write_bytecode = True
from main import skel

# Asks the user for multiple inputs for the possible choices
userinput1 = skel.requestUserInput("Give an option.")
userinput2 = skel.requestUserInput("Give another option.")
userinput3 = skel.requestUserInput("Give another option.")
userinput4 = skel.requestUserInput("Give another option.")
userinput5 = skel.requestUserInput("Give another option.")

# Makes all the possible choices into an array
player_chosen_options = [str(userinput1), str(userinput2), str(userinput3), str(userinput4), str(userinput5)]

# Gets a random item from player_chosen_options
skel.randElement(player_chosen_options)
