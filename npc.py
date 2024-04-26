class NPC:
    def __init__(self, name, greeting, quest=None):
        self.name = name
        self.greeting = greeting
        self.quest = quest

    def talk(self):
        return self.greeting + " " + (self.quest['description'] if self.quest else "")