import time
import colorama
from colorama import Fore
colorama.init(autoreset=True)


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


def forest2():
    """
    Follow the path after encountering a friendly creature.
    """
    print("The creature has to leave.")
    time.sleep(2)
    print("he point you in the right direction")
    time.sleep(2)
    print("your path splits in two")
    choice = make_choice([Fore.CYAN + "Left", Fore.CYAN + "Right"])

    if choice == 1:
        print("You reach a lake!")
        time.sleep(2)
        return True
    else:
        print("The road fades. you are lost")
        time.sleep(2)
        return False


def lake():
    """
    Reach a lake and make decisions.
    """
    print("You've reached a lake")
    time.sleep(2)
    print("You see a boat")
    choice = make_choice(
        [Fore.CYAN + "Go around", Fore.CYAN + "Take the boat"])

    if choice == 1:
        print("You encounter a wolf")
        time.sleep(2)
        print("It chase you away. GAME OVER!")
        return False
    else:
        print("You find two oars and row across the lake")
        return True


def forest3():
    """
    Navigate through a dense forest with limited visibility.
    """
    print("You leave the boat and enters a forest!")
    time.sleep(2)
    print("The forest is dense. you can hardly see.")
    time.sleep(2)
    choice = make_choice([Fore.CYAN + "Keep going", Fore.CYAN + "Turn back"])

    if choice == 1:
        print("You Keep going forward")
        time.sleep(2)
        print("You see something ahead")
        return True
    else:
        print("You turnd back!")
        time.sleep(2)
        print("A wolf followed you around the lake.")
        time.sleep(2)
        print("It chase you away. GAME OVER!")
        return False


def desert():
    """
    Journey through a vast desert with choices on how to proceed.
    """
    print("You arrive in a vast desert.")
    time.sleep(2)
    choice = make_choice(
        [Fore.CYAN + "Walk through the desert", Fore.CYAN + "Find an oasis"])

    if choice == 1:
        print("You walk through the desert and get dehydrated.")
        time.sleep(2)
        print("Game over! You collapse from exhaustion.")
        return False
    else:
        print("You find an oasis and replenish your water supply.")
        time.sleep(2)
        return True


def desert2():
    """
    Continue the desert journey with decisions on resting or continuing.
    """
    print("Your water supply is full")
    time.sleep(2)
    choice = make_choice(
        [Fore.CYAN + "Sit down and rest for a bit", Fore.CYAN + "keep going"])

    if choice == 1:
        print("You fell asleep")
        time.sleep(2)
        night()
    else:
        print("You continue your jurney")
        return True


def night():
    """
    Experience nightfall and make decisions on waiting or going north.
    """
    print("You fell asleep. Its now night")
    time.sleep(2)
    print("You've forgot where you came from")
    time.sleep(2)
    choice = make_choice(
        [Fore.CYAN + "Wait for morning", Fore.CYAN + "Go north"])

    if choice == 1:
        print("You wait until morgning and can see your foot stepps")
        time.sleep(2)
        print("You continue forward")
        return True
    else:
        print("You are lost!")
        return False


def mountain():
    """
    Face a steep mountain and decide whether to climb or go around.
    """
    print("You face a steep mountain.")
    time.sleep(2)
    choice = make_choice([Fore.CYAN + "Climb the mountain",
                          Fore.CYAN + "Go around the mountain"])

    if choice == 1:
        print("You successfully climb the mountain.")
        time.sleep(2)
        print("You reach the summit and see the treasure ahead.")
        return True
    else:
        print("You go around the mountain and encounter a group of bandits.")
        time.sleep(2)
        print("They steal your belongings.")
        return False


def main():
    """
    The main function that orchestrates the entire game, calling other functions based on player choices.
    """
    introduction()

    if forest():
        if forest2():
            if lake():
                if forest3():
                    if desert():
                        if desert2():
                            if mountain():
                                print(
                                    Fore.GREEN + "Congratulations! You reached the treasure.")
                                print(Fore.GREEN + "You have Won!")
                            else:
                                print(
                                    Fore.RED + "Game over! You did not reach the treasure.")
                        else:
                            print(
                                Fore.RED + "Game over! You did not reach the treasure.")
                    else:
                        print(Fore.RED + "Game over! You did not reach the treasure.")
                else:
                    print(Fore.RED + "Game over! You did not reach the treasure.")
            else:
                print(Fore.RED + "Game over! You did not reach the treasure.")
        else:
            print(Fore.RED + "Game over! You did not reach the treasure.")
    else:
        print(Fore.RED + "Game over! You did not reach the treasure.")


if __name__ == "__main__":
    main()