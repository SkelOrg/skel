# General library connection
import sys
sys.dont_write_bytecode = True
from main import skel

# Asks the user to select from different amounts of choices
choiceamount = str(skel.requestUserInput("Type the amount of choices you want to give. Valid: 2, 3, 4, 5. "))

if choiceamount == "2":
    userinput1 = skel.requestUserInput("Give an option. ")
    userinput2 = skel.requestUserInput("Give another option. ")

    # Makes all the possible choices into an array
    player_chosen_options = [str(userinput1), str(userinput2)]

    # Gets a random item from player_chosen_options
    print(skel.randItem(player_chosen_options))
elif choiceamount == "3":
    userinput1 = skel.requestUserInput("Give an option. ")
    userinput2 = skel.requestUserInput("Give another option. ")
    userinput3 = skel.requestUserInput("Give another option. ")

    # Makes all the possible choices into an array
    player_chosen_options = [str(userinput1), str(userinput2), str(userinput3)]

    # Gets a random item from player_chosen_options
    print(skel.randItem(player_chosen_options))
elif choiceamount == "4":
    userinput1 = skel.requestUserInput("Give an option. ")
    userinput2 = skel.requestUserInput("Give another option. ")
    userinput3 = skel.requestUserInput("Give another option. ")
    userinput4 = skel.requestUserInput("Give another option. ")

    # Makes all the possible choices into an array
    player_chosen_options = [str(userinput1), str(userinput2), str(userinput3), str(userinput4)]

    # Gets a random item from player_chosen_options
    print(skel.randItem(player_chosen_options))
elif choiceamount == "5":
    userinput1 = skel.requestUserInput("Give an option. ")
    userinput2 = skel.requestUserInput("Give another option. ")
    userinput3 = skel.requestUserInput("Give another option. ")
    userinput4 = skel.requestUserInput("Give another option. ")
    userinput5 = skel.requestUserInput("Give another option. ")
    # Makes all the possible choices into an array
    player_chosen_options = [str(userinput1), str(userinput2), str(userinput3), str(userinput4), str(userinput5)]

    # Gets a random item from player_chosen_options
    print(skel.randItem(player_chosen_options))
else:
    print("That isn't a valid amount. Valid amounts: 2, 3, 4, 5.")
