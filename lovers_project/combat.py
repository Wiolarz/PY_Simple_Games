import random


class Fighter:
    def __init__(self):
        self.hp = 6

        self.dice_pool = [6, 6, 6, 6, 6, 6]
        self.moves = []

        self.keyboard_input = True

        self.generate_moves()

    def generate_moves(self):
        self.moves = []
        for dice in self.dice_pool:
            self.moves.append(random.randint(1, dice))

    def move(self):
        if len(self.moves) == 0:
            return 1

        player_input = self.input(len(self.moves))
        value = self.moves[player_input]
        self.moves.pop(player_input)
        return value

    def input(self, range=None):
        if range == None:
            range = 1
        if self.keyboard_input:
            player_input = int(input())
        else:
            player_input = 1

        if range == 0:
            print("error")
            exit()
        elif player_input > range:
            player_input = 1

        return player_input - 1
    def hurt(self, value=None):
        if value is None:
            value = 1
        self.hp -= value
        if self.hp <= 0:
            pass  # TODO maybe check for dying should be made here?


def forest_exploration(character, world_monsters):
    '''
    current exploration is just 2 fights
    :param character:
    :param world_monsters:
    '''
    for fights in range(2):
        monster = world_monsters[random.randrange(0, len(world_monsters))]
        if combat(character, monster):
            monster.update_info()
        else:
            character.hurt()
            if character.hp == 0:
                return


def combat_info(player, monster, scoreboard):
    print("monster: ", monster.name, " ", monster.info())
    print("score: ", scoreboard)
    print("attacks: ", player.moves)


def combat(player, monster):

    player_score = 0
    score_board = ""

    for round in range(3):
        combat_info(player, monster, score_board)
        monster_attack = monster.stats[round]

        player_attack = player.move()

        if player_attack >= monster_attack:
            player_score += 1
            score_board += "+"
        else:
            score_board += "-"

        if player_score == 2:
            combat_info(player, monster, score_board)
            print("you have won\n")
            return True
        elif round == 1 and player_score == 0:
            break
    combat_info(player, monster, score_board)
    print("you have lost\n")
    return False
