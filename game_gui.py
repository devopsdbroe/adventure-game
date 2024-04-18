import tkinter as tk
import character as Character

class GameGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("RPG Game")
        self.master.geometry("600x400")

        self.character = None # This will hold the Character instance

    # Character creator
    def setup_gui(self):
        # Welcome label
        label = tk.Label(self.master, text="Create your character", font=("Arial", 16))
        label.pack(pady=20)

        # Character name
        name_label = tk.Label(self.master, text="Name:", font=("Arial", 12))
        name_label.pack()
        self.name_entry = tk.Entry(self.master, font=("Arial", 12))
        self.name_entry.pack()

        # Stat entries
        self.stats = {}
        # Loop through list to show entries for each stat
        for stat in ["Strength", "Agility", "Intelligence"]:
            label = tk.Label(self.master, text=f"{stat}:", font=("Arial", 12))
            label.pack()
            entry = tk.Entry(self.master, font=("Arial", 12))
            entry.pack()
            # Set each 'stat' within stats to the value of 'entry'
            self.stats[stat] = entry

        # Button to create character
        create_button = tk.Button(self.master, text="Create Character", command=self.create_character)
        create_button.pack(pady=20)

    def create_character(self):
        name = self.name_entry.get()
        strength = int(self.stats["Strength"].get())
        agility = int(self.stats["Agility"].get())
        intelligence = int(self.stats["Intelligence"].get())

        self.character = Character(name, strength, agility, intelligence)
        print(self.character)