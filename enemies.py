class Enemy:
    def __init__(self, name, health, behavior):
        self.name = name
        self.health= health
        self.behavior = behavior

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} takes {damage} damage, remaining health {self.health}")
    
    def is_alive(self):
        return self.health > 0
    
    def perform_action(self, player):
        raise NotImplementedError("This method should be overridden by subclasses")
    
class Goblin(Enemy):
    def __init__(self, health):
        super().__init__("Goblin", health, ["attack"])

    def perform_action(self, player):
        if self.is_alive():
            damage = 10
            player.take_damage(damage)
            print(f"Goblin attacks for {damage} damage.")

class Ogre(Enemy):
    def __init__(self, health):
        super().__init__("Ogre", health, ["attack"])

    def perform_action(self, player):
        if self.is_alive():
            damage = 20
            player.take_damage(damage)
            print(f"Ogre performs a heavy attack for {damage} damage.")