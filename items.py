class Item:
    def __init__(self, name, type, description):
        self.name = name
        self.type = type
        self.description = description

    def __str__(self):
        return f"{self.name} ({self.description})"
    
class Weapon(Item):
    def __init__(self, name, damage):
        super().__init__(name, "Weapon", f"Deals {damage} damage")
        self.damage = damage

class Potion(Item):
    def __init__(self, name, effect):
        super().__init__(name, "Potion", effect)