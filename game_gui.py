import tkinter as tk
from character import Character
from locations import Location

class GameGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("RPG Game")
        self.master.geometry("600x400")

        self.character = None # This will hold the Character instance
        self.current_location = None
        self.location_label = tk.Label(self.master, text="", font=("Arial", 16))
        self.location_label.pack(pady=20)

    # Character creator
    def setup_character_creation(self):
        # Welcome label
        label = tk.Label(self.master, text="Python RPG", font=("Arial", 16))
        label.pack(pady=20)

        # Character name
        self.name_label = tk.Label(self.master, text="Name:", font=("Arial", 12))
        self.name_label.pack()
        self.name_entry = tk.Entry(self.master, font=("Arial", 12))
        self.name_entry.pack()

        # Stat entries
        self.stats = {}
        # Loop through list to show entries for each stat
        for stat in ["Strength", "Agility", "Intelligence"]:
            stat_label = tk.Label(self.master, text=f"{stat}:", font=("Arial", 12))
            stat_label.pack()
            stat_entry = tk.Entry(self.master, font=("Arial", 12))
            stat_entry.pack()
            # Set each 'stat' within stats to the value of 'entry'
            self.stats[stat] = (stat_label, stat_entry)

        # Button to create character
        self.create_button = tk.Button(self.master, text="Create Character", command=self.create_character)
        self.create_button.pack(pady=20)

    def create_character(self):
        name = self.name_entry.get()
        strength = int(self.stats["Strength"][1].get())
        agility = int(self.stats["Agility"][1].get())
        intelligence = int(self.stats["Intelligence"][1].get())

        # Create character
        self.character = Character(name, strength, agility, intelligence)

        self.character.inventory.add_item("Potion", 3)
        self.character.inventory.add_item("Sword", 1)

        self.transition_to_game()

    def transition_to_game(self):
        # Hide character creation UI
        self.hide_character_creation_form()

        # Setup game environment
        self.setup_game_environment()

    def hide_character_creation_form(self):
        # Hide all character creation widgets
        self.name_label.pack_forget()
        self.name_entry.pack_forget()
        self.create_button.pack_forget()

        for label, entry in self.stats.values():
            label.pack_forget()
            entry.pack_forget()

    def setup_game_environment(self):
        self.location_label = tk.Label(self.master, text="", font=("Arial", 16))
        self.location_label.pack(pady=20)
        self.setup_locations()
        self.update_location_gui()

    def setup_locations(self):
        # Create locations
        town = Location("Town", "A small peaceful town.")
        forest = Location("Forest", "A dark mysterious forest.")
        cave = Location("Cave", "A spooky cave with a hidden treasure.")

        # Connect locations
        town.connect(forest, "north")
        forest.connect(town, "south")
        forest.connect(cave, "east")
        cave.connect(forest, "west")

        # Starting location
        self.current_location = town

    def update_location_gui(self):
        self.location_label.config(text=f"Current Location: {self.current_location}")

        # Clear previous buttons
        for widget in self.master.pack_slaves():
            if isinstance(widget, tk.Button) and widget.cget("text").startswith("Go"):
                widget.destroy()
        
        # Create movement buttons
        for direction, location in self.current_location.connected_locations.items():
            button = tk.Button(self.master, text=f"Go {direction} to {location.name}", command=lambda loc=location: self.move(loc))
            
            button.pack()

    def move(self, location):
        # Set location to argument provided
        self.current_location = location
        self.update_location_gui()