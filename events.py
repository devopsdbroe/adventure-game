import random

def random_event(player):
    events = ["Nothing happens", "You found a coin!", "A wild aminal attacks!"]
    result = random.choice(events)
    if result == "You found a coin!":
        player.update_currency(1)
    return result