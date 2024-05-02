class Player:
    def __init__(self, health, deck, relics):
        self.health = health
        self.deck = deck
        self.relics = relics
        self.defense = 0

    def is_alive(self):
        return self.health > 0

    def add_card_to_deck(self, card):
        self.deck.append(card)

    def remove_card_from_deck(self, card):
        self.deck.remove(card)

    def take_damage(self, damage):
        actual_damage = max(0, damage - self.defense)
        self.health -= actual_damage
        self.defense = max(0, self.defense - damage)
        print(f"Player takes {actual_damage} damage, remaining health {self.health}")

    def add_defense(self, defense):
        self.defense += defense
        print(f"Player defense increased to {self.defense}")

    def display_health(self):
        print(f"Health: {self.health}")