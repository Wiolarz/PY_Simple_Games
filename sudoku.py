"""
Sudoku alpha is a simple version, with random solver
"""

import random

def draw_board(board):
    for j, row in enumerate(board):
        if j % 3 == 0:
            print("----------------------")
        for i, value in enumerate(row):
            if i % 3 == 0 and i != 0:
                print("|", end=" ")
            print(value, end=" ")
        print()
    print("----------------------")

def generate_random_board():
    board = []
    for row in range(9):
        values = [i + 1 for i in range(9)]
        random.shuffle(values)
        board.append(values)
    # draw_board(board)
    return board

def checking_full_board(board):
    numbers = [x for x in range(1, 10)]
    # horizontal
    for row in board:
        copy_row = row.copy()
        copy_row.sort()
        if copy_row != numbers:
            return False

    # vertical
    columns = [[] for _ in range(len(board[0]))]
    for row in board:
        for index, value in enumerate(row):
            columns[index].append(value)
    for column in columns:
        column.sort()
        if column != numbers:
            return False

    return True

if __name__ == '__main__':
    for _ in range(10000000):
        board = generate_random_board()
        score = checking_full_board(board)
        if score:
            break
    draw_board(board)
    print(score)
