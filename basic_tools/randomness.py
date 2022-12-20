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
        def basic(self, dice):
            # its a random system from ugis rpg
            # it allows to roll maximum of 5 dice at a time, additional dice are treated as an auto success
            # dice size is an D6: 2,4,6 = success while 6 is additional roll
            success = 0
            if dice > 5:
                success = dice - 5
                dice = 5
            while dice > 0:
                dice -= 1
                roll = random.randint(1, 6)
                if roll in [2, 4]:
                    success += 1
                elif roll == 6:
                    success += 1
                    dice += 1
            return success

        def data(self, repeats):
            x = 0
            for i in range(repeats):
                x += self.basic(1)
            return x / repeats

        def new_basic(self, dice):
            success = 0
            if dice > 5:
                success = dice - 5
                dice = 5
            for i in range(dice):
                roll = random.randint(1, 6)
                if roll > 2:
                    success += 1
            return success

        def new_data(self, repeats):
            x = 0
            for i in range(repeats):
                x += self.new_basic(1)
            return x / repeats

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

    class fate:

        def test(self, difficulty):
            score = 0
            for dice in range(4):
                score += random.choice([-1, 0, 1])
            return score >= difficulty

        def test_using_resources(self, difficulty, re_rolls=2):
            """
            if player wants to use "resource" to re roll 2 dices
            :param difficulty:
            :return:
            """
            score = []
            for dice in range(4):
                score.append(random.choice([-1, 0, 1]))
            if sum(score) >= difficulty:
                return True

            for i in range(re_rolls):
                if -1 in score:
                    score.remove(-1)
                    score.append(random.choice([-1, 0, 1]))
                elif 0 in score:
                    score.remove(0)
                    score.append(random.choice([-1, 0, 1]))

                if sum(score) >= difficulty:
                    return True

            return False

    class durf:
        class hero:
            def __init__(self):
                self.STR = random.randint(1, 3)    # Strength
                self.DEX = random.randint(1, 3)    # Dexterity
                self.WILL = random.randint(1, 3)    # Willpower
                self.HD = 1     # Hit dice
                self.inventory = []
                self.max_inventory = 10 + self.STR
                self.gold = (random.randint(1, 6) + random.randint(1, 6)) * 5
                # + 2 supplies
                # + 3 * d40 random item
                self.name = ""
                self.exp = 0

            def gain_exp(self, value):
                # 1k * current HD 1k -> 2k -> 3k
                """
                At the end of each session the GM rewards
                each character XP based on the gold value of
                the non-magical treasure they brought back
                safely (1 GP = 1 XP), and 25 XP per NPC Hit Die
                of each monster they defeated or outsmarted
                """
                pass
            def spell(self):
                """
                To cast a spell the caster must have at least
                one empty inventory slot to receive Stress, one
                hand free, and must be able to speak.
                """
                roll = random.randint(1, 20)
                if roll + self.WILL > 15:
                    pass
                elif roll == 1:
                    pass


        def buffs(self, value):
            rolls = []
            for dice in range(abs(value)):
                rolls.append(random.randint(1, 6))
            return max(rolls)

        def data_test(self, stat=0, advantages=0):
            attempts = 100000
            score = 0
            for _ in range(attempts):
                roll = random.randint(1, 20)
                if advantages < 0:
                    roll -= self.buffs(advantages)
                elif advantages > 0:
                    roll += self.buffs(advantages)
                if roll + stat > 15:
                    score += 1
            print(score / attempts)

    class carder:
        """
        https://postimg.cc/yJLwV08s
        https://postimg.cc/PNpBjpsn
        https://postimg.cc/47njnnYt
        https://coffeesniffer.itch.io/carder-rpg
        https://www.reddit.com/r/RPGdesign/comments/x8w4bk/carder_rpg_v42/
        """


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

        def data_test(self):
            attempts = 10000

            for difficulty in range(-4, 5):
                score = 0
                for tests in range(attempts):
                    if self.test(difficulty):
                        score += 1

                re_rolls_scores = []
                for re_rolls in range(1, 4):
                    re_rolls_results = 0
                    for tests in range(attempts):
                        if self.test_using_resources(difficulty, re_rolls):
                            re_rolls_results += 1
                    re_rolls_scores.append(re_rolls_results)

                print("difficulty: ", difficulty, " result ", score / attempts, end="  |||  ")
                for re_roll_value in range(1, 4):
                    print("re_roll: ", re_roll_value, " result ", re_rolls_scores[re_roll_value - 1] / attempts, end="|||  ")
                print()


class lovers_project:
    def __init__(self, number_of_attempts=None):
        if number_of_attempts == None:
            number_of_attempts = 100
        self.attempts = number_of_attempts
    def distribution_of_stats(self):
        """
        Each monster rolls his die, if this die has
        :return:
        """


def classic_dice_rolls():
    tesy = old()
    tesy.print_results(8, 2) # 20, 10 8, 4-4-4-4, 6-6-6
    # tesy.print_results(3, 3)
    # tesy.print_results(120, 15)



if __name__ == '__main__':
    print("start")


    #classic_dice_rolls()

    # tester = known_rpg.dnd()
    # tester.data_test()

    tester = known_rpg.durf()
    for stat in range(0, 4):
        for buff_value in range(-4, 4):
            print(stat, " ", buff_value, end=" ")
            tester.data_test(stat, buff_value)

    #tester = experiments()
    #tester.hs_quick_test()


    '''tester = experiments()

    for i in range(10, 90, 10):
        tester.additive(i)'''


# 3 times in 15 tries 120 number


'''
3D6
18 = 9.333%
11 = 12,5
'''


