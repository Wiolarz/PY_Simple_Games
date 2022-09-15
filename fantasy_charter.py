import random




def basic_cards_value_winrate():
    cards = [x for x in range(13)]
    cards_progress = dict(zip(cards,
                              [[0.0], [0.08], [0.16], [0.25], [0.33], [0.41], [0.5], [0.58], [0.66], [0.75], [0.83],
                               [0.91], [1.0]]))

    for bonus in range(1, 8):
        # print("bonus: ", bonus)
        for i in range(13):
            cop = cards.copy()
            cur_card = cop[i] + bonus
            cop.pop(i)
            wins = 0
            for card in cop:
                if card < cur_card:
                    wins += 1
                elif card == cur_card:
                    wins += 0.5
            # print(wins / 12)#print("{:2.2%}".format(wins / 12))
            new_value = wins / 12
            cards_progress[i].append(new_value)

    for i in range(13):

        value = cards_progress[i][0]
        print(i, "{:2.2%}".format(value), end="  ")
        last_value = value
        for j in cards_progress[i][1:]:
            value = j - last_value
            print("{:2.2%}".format(value), end=" ")
            last_value = j
        print()


def basic_ironsworn_like_test():
    cards_values = [x for x in range(13)]
    cards_winrate = dict(zip(cards_values, [[0, 0, 0] for _ in range(13)]))


    for i in range(13):
        cards = cards_values.copy()
        cur_card = cards[i]
        cards.pop(i)

        for j in range(12):
            for k in range(12):
                if k == j:
                    continue

                #[0] += 1
                if cards[j] <= cur_card and cards[k] <= cur_card:
                    cards_winrate[cur_card][0] += 1
                elif cards[j] <= cur_card or cards[k] <= cur_card:
                    cards_winrate[cur_card][1] += 1
                else:
                    cards_winrate[cur_card][2] += 1
    for i in range(13):

        for j in range(3):
            print(i, end=" ")
            value = cards_winrate[i][j] / 132
            print("{:2.2%}".format(value), end=" ")
        print()

def ironsworn_like_test():
    cards_values = [x for x in range(13)]
    for _ in range(2):  # cards values has a size of 52
        cards_values += cards_values
    cards_winrate = dict(zip(cards_values, [[0, 0, 0] for _ in range(13)]))

    for i in range(13):
        cards = cards_values.copy()
        cur_card = cards[i]
        cards.pop(i)

        for j in range(51):
            for k in range(51):
                if k == j:
                    continue

                # [0] += 1
                if cards[j] < cur_card and cards[k] < cur_card:
                    cards_winrate[cur_card][0] += 1
                elif cards[j] < cur_card or cards[k] < cur_card:
                    cards_winrate[cur_card][1] += 1
                else:
                    cards_winrate[cur_card][2] += 1

    for i in range(13):
        print(i, end=" ")
        for j in range(3):

            # print(cards_winrate[i][j], end=" ")
            value = cards_winrate[i][j] / 2550
            print("{:2.2%}".format(value), end=" ")
        print()



if __name__ == '__main__':
    print("start")
    #basic_cards_value_winrate()
    ironsworn_like_test()

"""
0.00%
8.33%
16.67%
25.00%
33.33%
41.67%
50.00%
58.33%
66.67%
75.00%
83.33%
91.67%
100.00%"""