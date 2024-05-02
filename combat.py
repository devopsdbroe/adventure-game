def combat_round(player, enemy):
    print("Begin combat")
    # Player turn
    # Assumption is that player plays all cards in their hand
    for card in player.deck:
        card.play(player, enemy)
        if not enemy.is_alive():
            print(f"{enemy.name} defeated!")
            break

    # Enemy turn
    if enemy.is_alive():
        enemy.perform_action(player)
        if not player.is_alive():
            print("You died. Game over.")
            return
        

    # Reset player's defense for the next round
    player.defense = 0