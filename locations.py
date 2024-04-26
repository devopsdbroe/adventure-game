class Location:
    def __init__(self, name, description, npcs=None):
        self.name = name
        self.description = description
        self.npcs = []
        self.connected_locations = {}

    def add_npc(self, npc):
        self.npcs.append(npc)

    # Associate a dirrection with the location (e.g. north)
    def connect_location(self, direction, location):
        self.connected_locations[direction] = location