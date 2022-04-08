import basic_tools.basic_cards as engine







def draft_encounter(rounds, players, enemy):
    for round in range(rounds):
        players_score = 0
        players_defense = 0

        enemy_score = 0
        enemy_defense = 0

        for player in players:
            # each player places their card into a pool
            card = player.use_card()
            if card.color in [0, 3]:
                players_score += card.value
            else:
                players_defense += card.value
        for monster in enemy:
            card = monster.use_card()
            if card.color in [0, 3]:
                enemy_score += card.value
            else:
                enemy_defense += card.value

        print("players: ", players_score, " def:", players_defense)
        print("enemy: ", enemy_score, " def:", enemy_defense)



if __name__ == '__main__':

    deck = engine.Deck_manager()

    players = []
    enemy = []
    for i in range(4):
        players.append(engine.Player(deck))

        enemy.append(engine.Player(deck))

    for i in range(4):
        players[i].draw(3)
        enemy[i].draw(3)




    draft_encounter(3, players, enemy)
