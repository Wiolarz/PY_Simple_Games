"""

"""

import copy
from itertools import permutations
def slots_in_cages_finder():
    """
    :return:
    """


    def checking_slots_in_cages(cage_all_combinations, cage_possibilities):
        """
        search for values that cannot be inserted into a cage

        for loop of each cell:
            for loo of each spot:
                test_algorithm()


        :param cage_all_combinations: array<array<int>>
        :param cage_possibilities: array<array<int>>
        :return: a pair of numbers: cell index + slot value which is wrong
        TODO: return a dictionary - keys are index of slots that have a wrong number - values are what those numbers are
        """

        # TODO when checking a certain spot, rest of the cage should be sorted accordingly

        def insert_value(value, combinations_set):
            """
            replace a cage cell with a slot numbers
            no need to actually edit the cage as we move on it using for loop
            the only thing needed to be checked is combinations

            :param value:
            :return:
            """

            # Removing for a particular slot combinations that cannot match the slot choice
            to_be_removed = []
            for i, combination in enumerate(combinations_set):
                if value not in combination:
                    to_be_removed.append(i)
                else:
                    combination.remove(value)

            for correction, idx in enumerate(to_be_removed):
                combinations_set.pop(idx - correction)

            return combinations_set

        def test_variation(current_combinations, cage):
            """

            :param current_combinations:
            :return:
            """

            # check if the given combinations are solved
            if len(current_combinations) == 0:
                return False  # slot choice is wrong

            elif len(current_combinations[0]) == 0:
                return True  # current choice slot is correct

            # for loop
            for spot in cage[0]:
                new_combinations = copy.deepcopy(current_combinations)
                new_combinations = insert_value(slot, new_combinations)

                if test_variation(new_combinations, cage[1:]):
                    return True  # a correct path has been found

            return False  # a correct path hasn't been found

        # "final result loops"
        for cell_idx in range(len(cage_possibilities)):
            for slot in cage_possibilities[cell_idx]:
                current_combinations = copy.deepcopy(cage_all_combinations)  # combinations set for choosing this slot
                print(cell_idx, slot)
                current_combinations = insert_value(slot, current_combinations)
                '''

                    for inner_cell_idx in range(cell_idx + 1, len(cage_possibilities)):
                        for slot in cage_possibilities[cell_idx]:
                            # combinations set for choosing this slot
                            local_combinations = copy.deepcopy(current_combinations)
                            local_combinations = insert_value(slot, local_combinations)

                            if len(current_combinations) == 0:
                                return False  # slot choice is wrong

                            if len(current_combinations[0]) == 0:  # current choice slot is correct
                                break

                    insert_value(slot)

                    local_combination = copy.deepcopy(cage_all_combinations)
                '''

                # choose another slot

        return None  # everything is correct

    search_value = 15
    """
    12 - 4
    21 - 3
    19 - 3
    21 - 3
    12 - 4
    14 - 3
    26 - 5
    17 - 5
    10 - 3

    """


    combinations = [[1, 2, 3, 6], [1, 2, 4, 5]]
    cages = [[1, 2], [1, 2], [1, 2, 4], [1, 2, 3, 5]]

    checking_slots_in_cages(combinations, cages)

def cage_combinations():
    '''
    *********** [12, 4] ***********
{1, 2, 3, 6}
{1, 2, 4, 5}
*********** [17, 5] ***********
{1, 2, 3, 4, 7}
*********** [21, 3] ***********
{8, 9, 4}

{9, 5, 7}
{8, 6, 7}
*********** [19, 3] ***********
{2, 8, 9}

{3, 7, 9}
{4, 6, 9}
{4, 7, 8}
{5, 6, 8}
*********** [14, 3] ***********
{2, 5, 7}


*********** [26, 5] ***********

{1, 2,   6,    8, 9}
{1, 3,   5,    8, 9}



    :return:
    '''
    def combinations(search_value, cage_size):
        """
        Returns all possible combinations of numbers inside a cage

        :param search_value:
        :param cage_size:
        :return:
        """
        a = [i for i in range(1, 10)]
        all_perm = permutations(a, cage_size)
        sum_results = {}
        # print(all_perm.__sizeof__())
        for perm in all_perm:
            s = sum(perm)
            if s in sum_results.keys():
                sum_results[s].append(perm)
            else:
                sum_results[s] = [perm]

        all_possibilities = [6, 12, 7, 14, 8, 16, 9, 18, 10, 20, 11, 22, 12, 24]
        smaller = [6, 7, 8, 9, 10, 11, 12]
        larger = [12, 14, 16, 18, 20, 22, 24]

        smaller_values = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
        larger_values = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}

        occurences = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}

        correct_combination = []

        for result in sum_results:
            if result == search_value:
                for combination in sum_results[result]:
                    wrong = False
                    for value in combination:
                        pass
                        # if value in [1, 9]:
                        #    wrong = True
                        #    break
                    if not wrong:
                        correct_combination.append(combination)

        array_correct_combination = []

        for value in correct_combination:
            array_correct_combination.append(set(value))

        # REMOVING DUPLICATES

        no_duplicate = []

        for combination in array_correct_combination:
            if combination not in no_duplicate:
                no_duplicate.append(combination)



        # print(array_correct_combination[1] == array_correct_combination[2])

        # occurences

        '''if result in smaller:
                #print(i, sum_results[i])
                for combination in sum_results[result]:
                    for value in combination:
                        smaller_values[value] += 1
            if result in larger:
                #print(i, sum_results[i])
                for combination in sum_results[result]:
                    for value in combination:
                        larger_values[value] += 1
        print(smaller_values)
        print(larger_values)
        '''

        #for combination in no_duplicate:
        #    print(combination)
        return no_duplicate

    for test_set in [[12, 4], [21, 3], [19, 3], [14, 3], [26, 5], [17, 5], [10, 3]]:
        print("***********", test_set, "***********")
        # search value, cage size
        result = combinations(test_set[0], test_set[1])
        for combination in result:
            print(combination)


def skyscrapers():
    """
    Imagine that eah number represents the height of a skyscraper
    from a certain point of view viewer can see only a ceratin number of skyscrapers
    sudoku rules apply
    find all possible combinations
    :return:
    """

    ''' first attempt
    search for combinations with only 1 skyscraper visible

    '''

    all_possible_permutations = []
    view_length = 4

    new_permutation = []
    for cell in range(view_length):
        for i in range(1, 10):
            pass # new_permutation


if __name__ == '__main__':
    print("Start - sudoku/toolbox \n")

    #sudoku_helper()
    #skyscrapers()
    cage_combinations()
    print("End - sudoku/toolbox")
