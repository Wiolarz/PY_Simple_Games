"""

"""

import random

import matplotlib.pyplot as plt

class Power:

    def __init__(self, sides=1, number=1, bonus_value=0):

        self.sides = sides
        self.number = number

        values = None
        histogram = None

        expected_value = None
        total_different_results = None

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


    def generate_results(self):
        resultList, repeats = self.added(self.sides, self.number)
        self.values = set(resultList)
        # values = norep(resultList)
        self.histogram = self.repnumb(resultList, self.values)
        self.expected_value, self.total_different_results = self.expectedValue(self.histogram)

        # print('Result list: ', resultList)
        '''print('values: ', self.values)
        print('histogram: ', self.histogram)
        plt.bar(range(len(self.histogram)), list(self.histogram.values()), align='center')
        plt.xticks(range(len(self.histogram)), list(self.histogram.keys()))
        plt.show()
        print('expectedValue: ', self.expected_value, self.total_different_results)
        print("\n\n\n")'''


def show_powers_data():
    parameters = []
    number_of_powers = 5
    for i in range(1, number_of_powers + 1):
        parameters.append([i, i, i])


    powers_list = [Power(parameters[i][0], parameters[i][1], parameters[i][2]) for i in range(number_of_powers)]
    for power in powers_list:
        power.generate_results()

    for power in powers_list:
        print('values: ', power.values)
        print('histogram: ', power.histogram)
        plt.bar(range(len(power.histogram)), list(power.histogram.values()), align='center')
        plt.xticks(range(len(power.histogram)), list(power.histogram.keys()))
        plt.show()
        print('expectedValue: ', power.expected_value, power.total_different_results)
        print("\n\n\n")


def classic_dice_rolls():
    tesy = Power(8, 2)
    tesy.generate_results() # 20, 10 8, 4-4-4-4, 6-6-6
    # tesy.print_results(3, 3)
    # tesy.print_results(120, 15)



if __name__ == '__main__':
    print("start")


    show_powers_data()
    #classic_dice_rolls()

    print("End")



# 3 times in 15 tries 120 number


'''
3D6
18 = 9.333%
11 = 12,5
'''


