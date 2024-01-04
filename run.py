import colorama
from colorama import Fore


def introduction():
    """
    Display an introduction to the game.
    """
    print("Welcome to the Adventure Game!")
    time.sleep(2)
    print("You find yourself in a mysterious land.")
    time.sleep(2)
    print("Your goal is to reach the treasure at the end of the journey.")
    time.sleep(2)


def make_choice(options):
    """
    Allow the player to make a choice from a list of options.
    """
    print("Choose your path:")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")    
