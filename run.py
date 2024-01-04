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
    """
    checks that answer is valid
    """
    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            if 1 <= choice <= len(options):
                return choice
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")    


def forest():
    """
    Navigate through a dark forest with branching paths.
    """
    print("You enter a dark forest.")
    time.sleep(2)
    choice = make_choice([Fore.CYAN + "Follow the path",
                         Fore.CYAN + "Enter the cave"])

    if choice == 1:
        print("You follow the path and encounter a friendly creature.")
        time.sleep(2)
        print("The creature guides you to safety.")
        return True
    else:
        cave()
