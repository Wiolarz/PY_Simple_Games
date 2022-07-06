import random


def v_sauce():
    """
    https://youtu.be/s4tyO4V2im8 V-sauce video that explains this game
    :return:
    """
    pass
    deck = []
    for x in range(52):
        if x % 2 == 0:
            deck.append(1)
        else:
            deck.append(0)
    #print(deck)
    all_possible_combinations = [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 0], [1, 1, 1]]
    choices = [0, 1, 2, 3, 4, 5, 6, 7]
    for reduced_range in range(100):
        random.shuffle(choices)
        possible_combinations = [all_possible_combinations[choices[0]], all_possible_combinations[choices[1]]]

    for attempt in range(1000):
        random.shuffle(deck)
        stack = []
        i = 0
        last_three = []
        while i < 52:
            stack.append(deck[i])
            i += 1
            if len(stack) >= 3:
                last_three = [stack[-3], stack[-2], stack[-1]]
            if (last_three in possible_combinations):
                print("success ", last_three)
                break


        print(stack)


def test():
    pass

if __name__ == '__main__':
    print("start")
    test()