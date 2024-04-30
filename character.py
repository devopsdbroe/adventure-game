class Character:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.currency = 0
        self.quests = {}

    def add_item(self, item):
        self.inventory.append(item)

    def update_currency(self, amount):
        self.currency += amount

    def add_quest(self, npc_name, quest):
        self.quests[npc_name] = quest

    def __str__(self):
        return f"{self.name}, Health: {self.health}, Mana: {self.mana}, Inventory: {", ".join(str(item) for item in self.inventory)}"