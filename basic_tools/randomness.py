# first test will provide a graph of a probability of results from 2d6
import random


class old:
    def oneone(self, sides):
        resultList = []
        x = 0
        for i in range(sides):
            resultList.append(i + 1)
            x += 1
        return resultList, x


    def adloop(self, table, sides):
        table2 = []
        for i in range(sides):
            for j in table:
                table2.append(i + j + 1)
        return table2


    def added(self, sides=6, num=2):
        # table of all possible results, and number of them
        table1 = []
        x = sides ** num
        for i in range(sides):
            table1.append(i + 1)
        for i in range(num - 1):
            table1 = self.adloop(table1, sides)
        return table1, x


    def norep(self, resultList):
        # create list off all possible answers without repetition
        values = []
        for i in resultList:
            if i not in values:
                values.append(i)
        return values


    def repnumb(self, resultList, values):
        # count number of repetition
        # x = 0
        histogram = {}
        for j in resultList:
            if j in histogram:
                histogram[j] += 1
            else:
                histogram[j] = 1

        # for i in values:
        #    for j in resultList:
        #        if i == j:
        #            x += 1
        #    histogram.append([i, x])
        #    x = 0
        return histogram


    def expectedValue(self, histogram):
        # count expected value
        x = 0
        nr = 0
        for i in histogram:
            x += i * histogram[i]
            nr += histogram[i]
        x = x / nr
        return x, nr


    def print_results(self, sides, number):
        resultList, repeats = self.added(sides, number)
        values = set(resultList)
        # values = norep(resultList)
        histogram = self.repnumb(resultList, values)
        x, y = self.expectedValue(histogram)

        # print('Result list: ', resultList)
        print('values: ', values)
        print('histogram: ', histogram)
        print('expectedValue: ', x, y)
        print("\n\n\n")


class experiments:

    # first test, improving success ratio
    '''
    the idea is to count on average how many repeats there have to be to achieve success
    for example: D6 has to on average repeat 6 times to achieve 6
    '''

    def __init__(self):
        self.attempts = 10000

    def additive(self, chance):
        # test with no changes
        base_success_ratio = 0
        for _ in range(self.attempts):
            if self.roll(chance):
                base_success_ratio += 1



        #increment = 100 // chance
        increment = chance
        success = 0
        rng = chance

        for _ in range(self.attempts):
            if self.roll(rng):
                rng = chance
                success += 1
            else:
                rng += increment
                if rng > 100:
                    rng = 100

        print((base_success_ratio / self.attempts) * 100, end="   ")
        print((success / self.attempts) * 100)

    def roll(self, chance):
        # first approach is to just take in % chance, check how many times it has to be multiplied to get 100%
        # and add it to the chance
        if random.randint(1, 100) <= chance:
            return True
        else:
            return False

    ''' hearthstone tournament test
    which choice has a higher chance of winning:
    1: 1/3 + 1/3 only if both occur there is a win

    2: 1/5  + 1/4 if a isnlge one occurs there is a win
    '''

    def hs_quick_test(self):
        score_one = 0
        for i in range(self.attempts):
            if random.randint(1, 3) == 1:
                if random.randint(1, 3) == 1:
                    score_one += 1
        score_two = 0
        for i in range(self.attempts):
            if random.randint(1, 5) == 1:
                score_two += 1
            else:
                if random.randint(1, 4) == 1:
                    score_two += 1
        print(score_one)
        print(score_two)



class Fajt:
    '''
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

    '''

    '''
    IDEAS:
    effects affecting only some player, or per player. Before they are all added up to the side score
    
    Only x value is added but there is a multiplier
    
    for each dice gets a basic +1 to score
    
    +1 on odd/even scores
    '''


    '''
    Code structure:
    general_tests at the beginning call for player creation which generates:
        every type of units composition we want to test
    Then For each Units we run General_effects_tests which returns scores for that unit 
    
    '''
    # attempts
    def __init__(self, number_of_attempts):
        self.attempts = number_of_attempts



    def roll(self, size, effects):
        result = random.randint(1, size)

        for effect in effects:
            result = effect.use(result, size)   #(result, size)
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
        tier_one =\
            [
                {"attacker": [[4, 6, 8]], "defender": [[4, 6, 8]]},
                {"attacker": [[4, 4, 10]], "defender": [[4, 6, 8]]}
            ]

        tier_two =\
            [
                {"attacker": [[6, 12, 12, 12]], "defender": [[6, 12, 12, 12]]},
                {"attacker": [[20, 20, 4]], "defender": [[6, 12, 12, 12]]}
            ]
        tier_three =\
            [
                {"attacker": [[4, 6, 8]], "defender": [[4, 6, 8]]},
                {"attacker": [[4, 4, 10]], "defender": [[4, 6, 8]]}
            ]


        tier_actual_game =\
        [
            {"attacker": [[6, 10, 12]], "defender": [6, 6, 6, 10]},
            {"attacker": [[6, 6], [6, 6, 6, 6], [6, 6, 6, 6], [6, 6, 6, 6]], "defender": [[6, 6], [6, 10], [6, 6, 6], [6, 6, 6]]},
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


class known_rpg:
    class dnd:

        def advantage(self, size):
            a = result = random.randint(1, size)
            b = result = random.randint(1, size)
            if a > b:
                return a
            return b

        def data_test(self):
            attempts = 100000
            score = 0
            for _ in range(attempts):
                score += self.advantage(20)
            print(score / attempts)

    class ugis:
        def basic(self, dices):
            # its a random system from ugis rpg
            # it rolls maximum of 5 at a time while adding bigger number of dices as auto success
            # dice is D6, 2,4,6 = success while 6 is additional roll
            success = 0
            if dices > 5:
                success = dices - 5
                dices = 5
            while dices > 0:
                dices -= 1
                roll = random.randint(1, 6)
                if roll in [2, 4]:
                    success += 1
                elif roll == 6:
                    success += 1
                    dices += 1
            return success

        def data(self, reapets):
            x = 0
            for i in range(reapets):
                x += self.basic(1)
            return x / reapets

        def new_basic(self, dices):
            success = 0
            if dices > 5:
                success = dices - 5
                dices = 5
            for i in range(dices):
                roll = random.randint(1, 6)
                if roll > 2:
                    success += 1
            return success

        def new_data(self, reapets):
            x = 0
            for i in range(reapets):
                x += self.new_basic(1)
            return x / reapets

    class arcane_ugly:
        def character_generation(self):
            '''
            4 abilities: Strength, Dexterity, Intelligence, Weird
            for each we roll 3d6, and we take the lowest score
            statistical results:
            42% 1
            28& 2
            17% 3
            8.8% 4
            3.2% 5
            0.4% 6
            '''
            abilities = []
            for _ in range(4):
                rolls = [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)]
                abilities.append(min(rolls))
            return abilities

        def data_character_generation(self):
            test_range = 3000

            points = 0
            for _ in range(test_range):
                score = self.character_generation()
                for value in score:
                    points += value
            print(points / (4 * test_range))

        def advanced_data_character_generation(self):
            test_range = 25000

            point = 0

            values = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

            for _ in range(test_range):
                score = self.character_generation()
                for value in score:
                    values[value] += 1
            print(test_range)
            print(values)



def fate_test_less_dices():
    attempts = 10000
    for challenge in range(-4, 5):
        print(challenge, end=" ")
        fate_score = 0
        my_theory_score = 0
        for i in range(attempts):

            # fate
            score = 0
            for dice in range(4):
                score += random.choice([-1, 0, 1])
            if score >= challenge:
                fate_score += 1

            # my theory

            score = 0
            for dice in range(2):
                score += random.choice([-2, -1, 0, 0, 1, 2])
            if score >= challenge:
                my_theory_score += 1

        print("{:2.2%}".format(fate_score / attempts), end=" ||  ")
        print("{:2.2%}".format(my_theory_score / attempts))
        print()

if __name__ == '__main__':
    print("start")
    #print(help(Fajt))
    #tesy = old()
    #tesy.print_results(8, 2) # 20, 10 8, 4-4-4-4, 6-6-6

    #print("\n")
    #tesy.print_results(120, 15)

    # tester = known_rpg.dnd()
    # tester.data_test()


    #tester = experiments()
    #tester.hs_quick_test()
    fate_test_less_dices()

    '''tester = experiments()

    for i in range(10, 90, 10):
        tester.additive(i)'''

    '''tester = Fajt(10000)  # 0

    tester.general_tests()
'''
# 3 times in 15 tryes 120 number


'''
3D6
18 = 9.333%
11 = 12,5
'''
