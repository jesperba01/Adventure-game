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


def cave():
    """
    Explore a cave with potential dangers and choices.
    """
    print("You enter the cave and find a torch.")
    time.sleep(2)
    print("Visibility is low. You see something moving in the shadows.")
    time.sleep(2)
    print("You see a small opening.")
    time.sleep(2)
    choice = make_choice([Fore.CYAN + "Investigate the shadows",
                         Fore.CYAN + "Crawl through opening"])

    if choice == 1:
        print("You walk closer to see a big bear!")
        time.sleep(2)
        print("The bear chases you away.")
        return False
    else:
        cave2()


def cave2():
    """
    Continue the cave exploration with encounters with bandits.
    """
    print("You arrive in a bigger cave whit bandits.")
    time.sleep(2)
    print("They seem to be sleeping.")
    time.sleep(2)
    choice = make_choice(
        [Fore.CYAN + "Try to sneak past", Fore.CYAN + "Make a run for it"])

    if choice == 1:
        print("You stepped on a twig and woke them")
        time.sleep(2)
        print("They steal your belongings. GAME OVER!")
        return False
    else:
        print("You run for as fast as you can!")
        time.sleep(2)
        print("You are to slow. They catch you. GAME OVER!")
        return False