class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connected_locations = {}

    def connect(self, other, via):
        self.connected_locations[via] = other

    def __str__(self):
        return self.name + " - " + self.description