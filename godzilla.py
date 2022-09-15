"""
This is a simple game idea not made by me
It proposes that the godzilla is about to attack a 1 dimensional city
Players will try to kill godzilla.
There are x rounds before godzilla attacks, during those players can build a 1 level tower or
increase the level of existing tower, each level gets more costly.
Players receive points for damaging godzilla. Each tower has only 1 owner ->
player who owns the highest level of the tower


"""

class Player:
    def __init__(self):
        self.gold = 10
        self.score = 0


class Godzilla:
    def __init__(self, board):
        self.x = 0
        self.hp = 0
        self.attack = 1
        self.board = board
        self.board[0] = self

    def move(self):
        board[self.x] = None
        self.x += 1
        board[self.x] = self


    def __repr__(self):
        return "G"

class Tower:
    def __init__(self, board, x, player):
        self.board = board
        self.x = x
        self.owner = player
        self.range = 2
        self.power = 1
        self.hp = 1

    def dmg(self, value):
        self.hp -= value
        if self.hp <= 0:
            self.board[self.x] = None

    def attack(self, monster_pos):
        if self.x - monster_pos <= self.range:
            self.owner.score += self.power
            return self.power
        return 0

    def __repr__(self):
        return "T"


def godzilla_attack(board):
    monster = Godzilla(board)

    while len(board) != monster.x + 1:
        # godzilla action
        if board[monster.x + 1] is None:
            monster.move()
        else:
            board[monster.x + 1].dmg(monster.attack)

        # towers attack
        for spot in board:
            if isinstance(spot, Tower):
                monster.hp += spot.attack(monster.x)
        print_board(board)
        print(monster.hp)


def generate_board():
    board = [None]
    P1 = Player()
    for x in range(1, 19):
        board.append(Tower(board, x, P1))
    return board

def print_board(board):
    print("|", end="")
    for spot in board:
        if spot is None:
            print(" ", end="")
        else:
            print(spot, end="")
    print("|", end="")
    print()

if __name__ == '__main__':
    print("Start of the program")
    board = generate_board()
    godzilla_attack(board)
