import os
import platform
import time
from character import Character
from items import Weapon, Potion
from locations import Location
from npc import NPC
from events import random_event

def clear_screen():
    """
    Clears the terminal screen
    """

    # Check if the OS is Windows
    if platform.system == "Windows":
        os.system("cls") # Clear command for Windows
    else:
        os.system("clear") # Clear command for Unix/Linux/Mac

def slow_print(text, delay=0.05):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

    
def main():
    clear_screen()
    slow_print("Welcome to the adventure game!")
    player_name = input("Enter your character's name: ")
    player = Character(player_name)
    town_square = Location("Town Square", "You are in the center of the town")
    forest = Location("Forest", "A dark and spooky forest")

    town_square.connect_location("north", forest)
    forest.connect_location("south", town_square)

    # Initialize items
    sword = Weapon("Sword", 10)
    healing_potion = Potion("Healing Potion", "Heals 20 HP")
    player.add_item(sword)
    player.add_item(healing_potion)

    # Initalize NPCs
    wizard = NPC("Merlin", "Welcome, travler!")
    town_square.add_npc(wizard)

    current_location = town_square

    # Main game loop
    while True:
        clear_screen
        print(f"Current Location: {current_location.name}. {current_location.description}")
        action = input("What would you like to do? (talk, move, quest, inventory, exit): ")

        if action == 'exit':
            break
        elif action == 'inventory':
            print("Your inventory:")
            for item in player.inventory:
                print(item)
            print(f"Currency: {player.currency}")
        elif action == 'talk':
            print(wizard.talk())
        elif action == 'move':
            print("Available directions:")
            for direction in current_location.connected_locations:
                print(direction)
            move_to = input("Which direction do you want to go? ")
            if move_to in current_location.connected_locations:
                current_location = current_location.connected_locations[move_to]
                slow_print(random_event(player))

if __name__ == "__main__":
    main()