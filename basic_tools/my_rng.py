import random


class Fajt:
    """
    "fajt" is my own rpg system designed around letting players decide on rules of their next rolls
    those rule changes are called "bets" because you are basically betting on your better assessment of rng

    Rules for those declarations:
    1 They have to affect in some way this round
    2 There has to be a limit on how many active bets are

    Range of effect:
    1 one time
    2 each die
    3 each die from 1 player
    4 each die from 1 side (only affects 1 side of conflict)
    5 each die from a group (10, 20 / 4, 8 / 6, 12)




    Types of changes in bets:
    1 x * each dice
    2 x
    3 biggest dice



    Categories of bets:

    """

    """
    IDEAS:
    effects affecting only some player, or per player. Before they are all added up to the side score

    Only x value is added but there is a multiplier

    for each dice gets a basic +1 to score

    +1 on odd/even scores
    """

    """
    Code structure:
    general_tests at the beginning call for player creation which generates:
        every type of units composition we want to test
    Then For each Units we run General_effects_tests which returns scores for that unit 

    """

    # attempts
    def __init__(self, number_of_attempts):
        self.attempts = number_of_attempts

    def roll(self, size, effects):
        result = random.randint(1, size)

        for effect in effects:
            result = effect.use(result, size)  # (result, size)
        return result

    def fight(self, attacker, defender, attacker_target_bets, defender_target_bets):
        attacker_result = 0
        for unit in attacker:
            for die in unit:
                attacker_result += self.roll(die, attacker_target_bets)
        defender_result = 0
        for unit in defender:
            for die in unit:
                defender_result += self.roll(die, defender_target_bets)
        return defender_result <= attacker_result

    def test_fight(self, attacker, defender, atk_target, def_target):

        attacker_score = 0

        for _ in range(self.attempts):

            if self.fight(attacker, defender, atk_target, def_target):
                attacker_score += 1
        return attacker_score / self.attempts

    def general_effects_tests(self, attacker, defender):
        '''
        :param attacker: :param defender: sides players
        :return: biggest changes in score introduced by effects
        '''
        no_change = self.test_fight(attacker, defender, [], [])

        def_target = [[]]  # testing defender combination is unnecessary at this stage[[], ["reroll"]]
        atk_target = [[], [self.Effects("basic_reroll")], [self.Effects("dices_bonus", 2)]]
        max_change = 0

        for atk in atk_target:
            for dfn in def_target:
                tested_change = self.test_fight(attacker, defender, atk, dfn)

                difference = no_change - tested_change
                percent = (difference / no_change) * 100
                print(atk, "   ", dfn, "    ", percent)
        '''print(no_change)
        print(tested_change)
        print(difference)'''

    def player_generation(self):
        '''
        for a start we define 3 tiers of power, and create different types of dice imbalances in a range of each tier
        :return: a huge array of possible combination of players
        '''
        tier_one = \
            [
                {"attacker": [[4, 6, 8]], "defender": [[4, 6, 8]]},
                {"attacker": [[4, 4, 10]], "defender": [[4, 6, 8]]}
            ]

        tier_two = \
            [
                {"attacker": [[6, 12, 12, 12]], "defender": [[6, 12, 12, 12]]},
                {"attacker": [[20, 20, 4]], "defender": [[6, 12, 12, 12]]}
            ]
        tier_three = \
            [
                {"attacker": [[4, 6, 8]], "defender": [[4, 6, 8]]},
                {"attacker": [[4, 4, 10]], "defender": [[4, 6, 8]]}
            ]

        tier_actual_game = \
            [
                {"attacker": [[6, 10, 12]], "defender": [6, 6, 6, 10]},
                {"attacker": [[6, 6], [6, 6, 6, 6], [6, 6, 6, 6], [6, 6, 6, 6]],
                 "defender": [[6, 6], [6, 10], [6, 6, 6], [6, 6, 6]]},
                {"attacker": [[20, 20, 20, 20]], "defender": [[6, 6], [6, 10], [6, 6, 6], [6, 6, 6]]}
            ]
        return [tier_one, tier_two, tier_three]

    def general_tests(self):

        full_army = self.player_generation()

        for tier in full_army:
            print("tier: ", tier)
            for unit in tier:
                print("unit: ", unit)
                self.general_effects_tests(unit["attacker"], unit["defender"])

    class Effects:
        def __str__(self):
            return self.type

        def __repr__(self):
            return self.type

        def __init__(self, name, power_value=None):
            self.type = name
            self.power = power_value

        # rolls effects
        def use(self, one, two=None):
            if self.type == "basic_reroll":
                return self.basic_reroll(one, two)
            elif self.type == "even_score":
                return self.even_score(one)
            elif self.type == "odd_score":
                return self.odd_score(one)
            elif self.type == "max_score":
                return self.max_score(one, two)
            elif self.type == "dices_bonus":
                return self.dices_bonus(one)

        def basic_reroll(self, result, size):
            if result == 1:
                return random.randint(1, size)
            else:
                return result

        def even_score(self, result):
            if result % 2 == 0:
                return result + self.power
            else:
                return result

        def odd_score(self, result):
            if result % 2 != 0:
                return result + self.power
            else:
                return result

        def max_score(self, result, sides):
            if result == sides:
                return result * self.power
            else:
                return 0

        # player wide effects
        def dices_bonus(self, result):
            return result + self.power



def fajt_tests():
    tester = Fajt(10000)  # 0
    tester.general_tests()




if __name__ == '__main__':
    print("start")


