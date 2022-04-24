"""
Testing different types of matchmaking systems, like a group stage or tournament ladder
"""

import random

class Tournament:
    class Player:
        def __init__(self):
            self.wins = 0
            self.defeats = 0
        def __repr__(self):
            return "P[" + str(self.wins) + ":" + str(self.defeats) + "] "



    def return_wins(self, player):
        return player.wins


    def test_basic_groups(self):
        for num_of_testers in range(5, 6):
            for test in range(20):
                players = []
                for player in range(num_of_testers):
                    players.append(self.Player())

                counter = 1
                for player in players:
                    for enemy in players[counter:]:
                        if random.randint(0, 1) == 0:
                            player.wins += 1
                            enemy.defeats += 1
                        else:
                            player.defeats += 1
                            enemy.wins += 1
                    counter += 1
                players.sort(reverse=True, key=self.return_wins)
                for player in players:
                    print(player)
                print("\n\n\n")



class Battlegrounds:
    class Player:
        def __init__(self):
            self.games = 0
            self.rank = 0

        def update_rank(self, value):
            self.rank += value
            if self.rank < 0:
                self.rank = 0

        def __repr__(self):
            return "P[" + str(self.games) + ":" + str(self.rank) + "] "

    def match(self, players):
        random.shuffle(players)
        value = 4
        for player in players:
            player.update_rank(value)
            player.games += 1
            value -= 1
            if value == 0:
                value -= 1

    def basic_test(self):
        population = [self.Player() for x in range(200)]

        for tour in range(10000):

            current_match = (random.choices(population, k=8))
            #print(current_match)
            self.match(current_match)
        def return_rank(player):
            return player.rank

        population.sort(key=return_rank)
        print(population)
if __name__ == '__main__':
    pass
    game = Battlegrounds()
    game.basic_test()
