"""
Connect four is a simple 2 player board game with board of a size 7x6

"""
import random


def print_board(board):
    print("   1 2 3 4 5 6 7")
    for x, row in enumerate(board):
        print(x + 1, "[", end="")
        for value in row[:-1]:
            print(value, end="|")
        print(row[-1], "]", sep="")


def create_board():
    board = []
    for _ in range(6):
        board.append([" " for _ in range(7)])
    return board


def create_random_board():
    board = []
    values = [" ", "X", "O"]
    for _ in range(6):
        board.append([random.choice(values) for _ in range(7)])
    return board


def create_numerical_board():
    board = []
    for value in range(6):
        board.append([str(value + (index*10)) for index in range(7)])
    return board


def check_win(board):
    """
    Checks if someone won based on the entire board state
    :param board:
    :return: if there is a winner return his color. After DRAW return space. Otherwise return None
    """
    start = " "

    def check(color):
        nonlocal score
        nonlocal start
        if color == " ":
            score = 0
            start = " "
            return False

        if start != color:
            start = color
            score = 1
        elif value == start:
            score += 1
            if score == 4:
                return True
        return False

    # horizontal
    for row in board:
        start = " "
        score = 0
        for value in row:
            if check(value):
                return start
    # vertical
    columns = [[] for _ in range(len(board[0]))]
    for row in board:
        for index, value in enumerate(row):
            columns[index].append(value)
    for column in columns:
        start = " "
        score = 0
        for value in column:
            if check(value):
                return start
    # bias
    lines = []
    ranges_left = [5, 4]
    ranges = [6, 6, 5, 4]
    ranges_bot_top = [0, 0, 1, 2]
    # creating lines for bias FROM TOP to DOWN
    for x, index in enumerate([1, 2]):

        line = []
        for point in range(ranges_left[x]):
            line.append(board[index + point][0 + point])
        lines.append(line)

    for index in range(4):
        line = []
        for point in range(ranges[index]):
            x = point + index
            line.append(board[point][x])
        lines.append(line)
    # creating lines for bias FROM Down to TOP
    for x in range(2):
        line = []
        for y, point in enumerate(range(ranges_left[x], 0, -1)):
            line.append(board[point - 1][y])
        lines.append(line)

    for index in range(4):
        line = []
        for y, point in enumerate(range(5, -1 + ranges_bot_top[index], -1)):
            line.append(board[point][y + index])
        lines.append(line)

    # checking lines in bias
    for line in lines:
        for value in line:
            if check(value):
                return start

    # checking draw condition
    for row in board:
        for value in row:
            if value == " ":
                return
    return " "


def fast_check_win(board, last_move):
    """
    Checks if someone won based on thier last move
    :param board:
    :param last_move: array of 2 elements, contains axis of the last move
    :return: if there is a winner return his color. After DRAW return space. Otherwise return None
    """
    y = last_move[0]
    x = last_move[1]
    color = board[y][x]

    # checking horizontal
    # checking left side
    points = 1
    for a in range(x - 1, -1, -1):
        if board[y][a] == color:
            points += 1
        else:
            break
    # checking right side
    for a in range(x + 1, 7):
        if board[y][a] == color:
            points += 1
        else:
            break
    if points >= 4:
        print("horizontal")
        return color

    # checking vertical
    points = 1
    # checking top side
    for a in range(y - 1, -1, -1):
        if board[a][x] == color:
            points += 1
        else:
            break
    # checking bottom side
    for a in range(y + 1, 6):
        if board[a][x] == color:
            points += 1
        else:
            break
    if points >= 4:
        print("vertical")
        return color

    # checking bias
    points = 1

    # checking left top
    a = x - 1  # left
    b = y - 1  # top
    # while a > -1 and b > -1:
    for _ in range(6):
        if a < 0 or b < 0:
            break
        if board[b][a] == color:
            points += 1
        else:
            break
        b -= 1  # top
        a -= 1  # left

    # checking right down
    a = x + 1  # right
    b = y + 1  # down
    # while a < 6 and b > -1:
    for _ in range(6):
        if a > 6 or b > 5:
            break
        if board[b][a] == color:
            points += 1
        else:
            break
        b += 1  # down
        a += 1  # right

    if points >= 4:
        print("bias1")
        return color

    # checking right top
    points = 1

    a = x + 1  # right
    b = y - 1   # top
    #while a < 6 and b < 5:
    for _ in range(6):
        if a > 6 or b < 0:
            break
        if board[b][a] == color:
            points += 1
        else:
            break
        b -= 1  # top
        a += 1  # right

    # checking left down
    a = x - 1   # left
    b = y + 1  # down
    # while a > -1 and b < 6:
    for _ in range(6):
        if a < 0 or b > 5:
            break
        if board[b][a] == color:
            points += 1
        else:
            break
        b += 1  # down
        a -= 1  # left

    if points >= 4:
        print("bias2")
        return color

    # checking draw
    for x in range(7):
        if board[0][x] == " ":
            return
    return " "

def fast_check_win2(board, last_move):
    """
    Checks if someone won based on their last move
    :param board:
    :param last_move: array of 2 elements, contains axis of the last move
    :return: if there is a winner return his color. After DRAW return space. Otherwise return None
    """

    def line(xd, yd):
        a = x
        b = y
        for _ in range(3):
            a += xd
            b += yd
            if not -1 < a < 7 or not -1 < b < 6:
                return
            if board[b][a] == color:
                nonlocal points
                points += 1
            else:
                return

    y = last_move[0]
    x = last_move[1]
    color = board[y][x]

    directions = ((-1, 0), (1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1), (0, 1))
    points = 1
    for i, direction in enumerate(directions):
        if i % 2 == 0:
            points = 1
        line(*direction)
        if points >= 4:
            return color

    # checking draw
    for x in range(7):
        if board[0][x] == " ":
            return
    return " "

'''

# checking horizontal
points = 1
for i in [[-1, -1, -1], [1, 7, 1]]:
    for a in range(x + i[0], i[1], i[2]):
        if board[y][a] == color:
            points += 1
        else:
            break
if points >= 4:
    print("horizontal")
    return color

# checking vertical
points = 1

for i in [[-1, -1, -1], [1, 6, 1]]:
    for a in range(y + i[0], i[1], i[2]):
        if board[a][x] == color:
            points += 1
        else:
            break
if points >= 4:
    print("vertical")
    return color

# checking bias
points = 1
directions = [[-1, -1], [1, 1], [1, -1], [-1, 1]]
for i, direction in enumerate(directions):
    if i % 2 == 0:
        points = 1
    a = x + direction[0]
    b = y + direction[1]
    for _ in range(6):
        if not 7 > a > -1 or not 6 > b > -1:
            break
        if board[b][a] == color:
            points += 1
        else:
            break
        b += direction[0]
        a += direction[1]
    if points >= 4:
        print("bias")
        return color
'''


def place(color, board):
    # checking draw
    draw = True
    for x in range(7):
        if board[0][x] == " ":
            draw = False
    if draw:
        return

    while True:
        # input
        if random_move:
            x = random.randint(0, 6)
        elif not debug:
            x = int(input()) - 1
        else:
            global debug_value
            if debug_value == 1:
                x = 0
                debug_value = 2
            else:
                x = 1
                debug_value = 1
        if x > 6:
            x = 6
        if board[0][x] == " ":
            for row in range(5, -1, -1):
                if board[row][x] == " ":
                    if color:
                        board[row][x] = "O"
                    else:
                        board[row][x] = "X"
                    if fast_check:
                        return fast_check_win(board, [row, x])
                    if fast_check2:
                        return fast_check_win2(board, [row, x])


def game_loop(board):
    score = None
    players = True
    print_board(board)
    number_of_moves = 0
    while score is None:
        if number_of_moves > 10:
            print("test")
        score = place(players, board)
        number_of_moves += 1

        print_board(board)
        if not fast_check and not fast_check2:
            score = check_win(board)
        players = not players  # swapping players color

    if score == "O":
        print("WINS O")
    elif score == "X":
        print("WINS X")
    elif score == " ":
        print("DRAW")


random_move = True
debug = False
debug_value = 1

fast_check = False
fast_check2 = True


if __name__ == '__main__':

    print("start")


    # board = create_numerical_board()
    # board = create_random_board()
    for i in range(1):
        table = create_board()
        game_loop(table)
