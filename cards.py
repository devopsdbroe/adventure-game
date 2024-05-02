class Card:
    def __init__(self, name, cost, card_type):
        self.name = name
        self.cost = cost # Energy cost to play card
        self.card_type = card_type # E.g., "Attack", "Defense", or "Power"

    def play(self, player, enemy):
        raise NotImplementedError("This method should be overridden by subclasses")
    
class AttackCard(Card):
    def __init__(self, name, cost, damage):
        super().__init__(name, cost, "Attack")
        self.damage = damage

    def play(self, player, enemy):
        enemy.take_damage(self.damage)
        print(f"Dealt {self.damage} damage to the enemy")

class DefenseCard(Card):
    def __init__(self, name, cost, defense):
        super().__init__(name, cost, "Defense")
        self.defense = defense

    def play(self, player, enemy):
        player.add_defense(self.defense)
        print(f"Added {self.defense} defense")
    