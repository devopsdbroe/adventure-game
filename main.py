from player import Player
from cards import AttackCard, DefenseCard
from enemies import Goblin, Ogre
from combat import combat_round

def setup_player():
    # TODO: Add interactive setup
    deck = [AttackCard("Strike", 1, 6), DefenseCard("Defend", 1, 5)]
    return Player(health=100, deck=deck, relics=[])

def setup_enemies():
    # Simple setup for enemy demonstration
    return [Goblin(30), Ogre(50)]

def main():
    print("Welcome to Adventure Game!")
    player = setup_player()
    enemies = setup_enemies()

    # Game loop
    for enemy in enemies:
        print(f"\nA wild {enemy.name} appears!")
        while enemy.is_alive() and player.is_alive():
            combat_round(player, enemy)
            if not enemy.is_alive():
                print(f"{enemy.name} has been defeated!")
            if not player.is_alive():
                print("You have been defeated. Game over.")
                break

    if player.is_alive():
        print("Congratulations! You defeated all the enemies.")

if __name__ == "__main__":
    main()