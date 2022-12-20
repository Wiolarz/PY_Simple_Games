import random

def game_logic(test):
    def draw():
        nonlocal aces
        nonlocal deck
        nonlocal value
        card = deck[0]
        if card == 1:
            aces = True
        value += card
        deck.pop(0)


    deck = [x for x in range(2, 11)]
    for _ in range(2):  # cards values has a size of 52
        deck += deck
    for _ in range(12):
        deck.append(10)
    for _ in range(4):
        deck.append(1)
    random.shuffle(deck)
    # player draws 2 cards
    aces = False
    value = 0
    board_value = 0
    for card in range(2):
        draw()

    # gameplay loop
    board_ai = False
    for turn in range(2):
        if turn == 1:
            board_ai = True
        while value < 21:
            if value == 21:
                break

            if aces > 0:
                aces -= 10
                value += 10
                if value > 21:
                    value -= 10
                    break
                if value == 21:
                    break
                elif value >= 17 and board_ai:
                    pass
                elif not board_ai and random.randint(1, 2) == 1:
                    value -= 10


            if board_ai:
                if value >= 17:
                    break
                draw()
            else:
                if value >= test:
                    break
                draw()
                '''if value == 21:
                    break
                if random.randint(1, 2) == 1:
                    draw()
                else:
                    break'''

        if turn == 0:
            player_value = value
            aces = 0
        else:
            board_value = value

        value = board_value

    if player_value > 21:
        return False
    elif board_value > 21:
        return True
    return player_value >= board_value




if __name__ == '__main__':
    print("Start of the program")
    wins = 0
    attempts = 100000
    for test in range(11, 22):
        for _ in range(attempts):
            if game_logic(test):
                wins += 1
        print(test, end="  ")
        print("{:2.2%}".format(wins / attempts))
        wins = 0

