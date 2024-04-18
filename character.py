class Character:
    def __init__(self, name, strength=0, agility=0, intelligence=0):
        self.name = name
        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence

    def __str__(self):
        return (f"Name: {self.name}\n"
                f"Strength: {self.strength}\n"
                f"Agility: {self.agility}\n"
                f"Intelligence: {self.intelligence}"
                )