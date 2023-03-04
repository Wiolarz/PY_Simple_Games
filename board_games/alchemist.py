"""
Alchemist is a complex board game.
It's main gameplay system is about discovering properties of ingredients


TODO:
Document this project

### Elements of this project:

"ING" Ingredient - main object, there is an 8 of them, and they all have a random properties assigned
discovering which object has what properties is the objective of this project

ingredients() - test environment for object functions

ING

POTION - {int} -1 neutral red[0, 1] green[2, 3] blue[4, 5]  (first number in a color is a plus value)


Properties:
type  red* green* blue*
size and sign - 2 big +  1 small +   -2 big -   -1 small
when combining two ingredients:
a potion is created if 2 ingredients have 2 circles with same symbol and different size



"""

import random


class Ingredient:
    def __init__(self, name_id, values, paper):
        self.paper_pointer = paper
        # 2 big +  1 small +   -2 big -   -1 small
        self.properties_list = [
                                [2, 2, 2],
                                [2, 1, -1],
                                [1, -1, 2],
                                [1, -2, -1],
                                [-1, 2, 1],
                                [-1, 1, -2],
                                [-2, -1, 1],
                                [-2, -2, -2]]
        values = self.properties_list[values]


        items_names = ["talon", "feather", "frog", "flower", "plant", "root", "mushroom", "scorpion"]
        items_colors = ["yellow", "black", "brown", "blue", "green", "white", "purple", "red"]
        self.number = name_id
        self.name = items_names[name_id]
        self.color = items_colors[name_id]
        self.red = values[0]
        self.green = values[1]
        self.blue = values[2]
        self.properties = values


        self.produced_potions = {}
    def remove_variant(self, variant):
        self.properties_list.remove(variant)
        self.paper_pointer[self.number].remove(variant)


    def remove_variants(self, value):
        """
        TODO: how to handle -1

        value can be either a array, or a number
        value:: [(int)color, plus(TRUE)/minus(FALSE)]
        """
        if not isinstance(value, int):
            if value[1]:
                value = (value[0] * 2)
            else:
                value = (value[0] * 2) + 1
        if value == -1:
            return

        to_be_removed = []
        for i, item in enumerate(self.properties_list):
            if value % 2 == 1:
                if item[value // 2] > 0:
                    to_be_removed.append(item)
            else:
                if item[(value - 1) // 2] < 0:
                    to_be_removed.append(item)

        for i in to_be_removed:
            self.remove_variant(i)

    def remove_not_matching_properties(self):
        for potion in self.produced_potions:
            if potion[0] == 0:
                pass



    def create_potion(self, second_element):
        # potions are in order red[0, 1] green[2, 3] blue[4, 5]
        for i, color in enumerate(self.properties):
            if {color, second_element.properties[i]} == {1, 2}:
                potion = 0 + (i * 2)
                #self.produced_potions.add([potion, second_element])
                return potion
            elif {color, second_element.properties[i]} == {-1, -2}:
                potion = 1 + (i * 2)
                #self.produced_potions.add([potion, second_element])
                return potion
        #self.produced_potions.add([-1, second_element])
        return -1  # neutral potion

    def __str__(self):
        return self.name



def paper_generation():
    properties_list = [
        [2, 2, 2],
        [2, 1, -1],
        [1, -1, 2],
        [1, -2, -1],
        [-1, 2, 1],
        [-1, 1, -2],
        [-2, -1, 1],
        [-2, -2, -2]]

    paper = []
    for _ in range(8):
        paper.append(properties_list.copy())
    return paper





def win_state(collection):
    for item in collection:
        if len(item.properties_list) > 1:
            return False
    return True

def removing_unique(collection):
    unique = []
    rest = []
    for item in collection:
        if len(item.properties_list) == 1:
            unique.append(item.properties_list[0])
        else:
            rest.append(item)
    print()
    for value in unique:
        for item in rest:
            item.remove_variant(value)


def paper_removing_unique(paper):
    """
    If an item on X axis is alone, remove rest of the vertical elements
    :param collection:
    :return:
    """
    properties_list = [
        [2, 2, 2],
        [2, 1, -1],
        [1, -1, 2],
        [1, -2, -1],
        [-1, 2, 1],
        [-1, 1, -2],
        [-2, -1, 1],
        [-2, -2, -2]]
    for attempts in range(8):
        old_state = paper.copy()
        for row in properties_list:
            occurrences = 0
            x = 0
            for i, item in enumerate(paper):
                if row in item:
                    occurrences += 1
                    x = i

            """ Maximum occurences usefulness is 4
                                        """
            if occurrences == 1:
                paper[x] = [row]


        if paper == old_state:  # last iteration didn't change anything
            break
    print()


def paper_removing_pairs(paper):
    """
    If there are only 2 items on Y axis, search for an exactly the same looking pair
    :param collection:
    :return:
    """
    properties_list = [
        [2, 2, 2],
        [2, 1, -1],
        [1, -1, 2],
        [1, -2, -1],
        [-1, 2, 1],
        [-1, 1, -2],
        [-2, -1, 1],
        [-2, -2, -2]]
    for attempts in range(8):
        old_state = paper.copy()

        pairs = []
        for i, column in enumerate(paper):
            if len(column) == 2:
                pairs.append(column)


        occurrences = 0
        x = 0
        for i, item in enumerate(paper):
            if row in item:
                occurrences += 1
                x = i

            """ Maximum occurences usefulness is 4
                                        """
            if occurrences == 1:
                paper[x] = [row]


        if paper == old_state:  # last iteration didn't change anything
            break
    print()


def test():
    paper = [[1, 3], [2, 4], [1, 3], [2, 3, 4]]
    # vertical check
    a = []
    for column in paper:
        a.append(len(column))
    b = []
    c = {}
    for value in a:
        if value not in b:
            b.append(value)
            c[value] = 1
        else:
            c[value] += 1

    final = {}
    for length in a:
        if c[length] > 1:
            final[length] = []
            d = []
            for column in paper:
                if len(column) == length:
                    d.append(column)
            x = d[0]
            for i, column in enumerate(d[:-1]):
                for j, column_2 in enumerate(d[1:]):
                    if i == j + 1:
                        continue
                    if column == column_2:
                        final[length].append(i)
                        final[length].append(j + 1)



    # horizontal check
    a = []
    rows = [[] for _ in range(len(paper))]
    for i, column in enumerate(paper):
        for value in column:
            rows[value - 1].append(i + 1)
    print()

    a = []
    for row in rows:
        a.append(len(column))
    b = []
    c = {}
    for value in a:
        if value not in b:
            b.append(value)
            c[value] = 1
        else:
            c[value] += 1

    for value in b:
        if c[value] == value:
            print(value)



def test2(rows):
    def convert_to_rows(columns):
        # Converting to rows
        rows = [[] for _ in range(len(columns[0]))]
        for column in columns:
            for height in range(len(columns[0])):
                rows[height].append(column[height])
        return rows
    def convert_to_columns(rows):
        # converting to columns
        columns = [[] for _ in range(len(rows[0]))]
        for row in rows:
            for width in range(len(rows[0])):
                columns[width].append(row[width])
        return columns
    # Source

    columns = convert_to_columns(rows)

    # Printing first State
    for row in rows:
        print(row)
    print()

    new_columns = []
    for column in columns:
        length = 0
        for x in column:
            length += x
        new_columns.append([column, length])

    coordinates_to_check = []   # Those are columns that are an identical pairs,
                                # each value is [[column1.x, column2.x], number_of_true_values_in_column]
    for i, column in enumerate(new_columns[:-1]):
        for j, column_2 in enumerate(new_columns[i+1:]):
            if column == column_2:
                x = [i, j + i + 1]  # first and second column that are identical
                coordinates_to_check.append([x, column[1]])  # column[1] is the length

    # comparing with rows
    rows_to_be_edited = []  # should be a simple array of pairs of values
    for coordinates in coordinates_to_check:
        rows_to_check = []

        for coordinate in coordinates[0]:
            for i, value in enumerate(columns[coordinate]):
                if value == 1:
                    rows_to_check.append(i)

        for checked_row in rows_to_check:
            length = 0
            for value in rows[checked_row]:
                length += value

            if length > coordinates[1]:  # comparing desired length
                rows_to_be_edited.append([checked_row, coordinates[0]])  # row_number  columns that should remain

    """
    Now there should be something like a merge of cordinates to check
    for every row thats edited check if the lenth is corect if not then
    maybe do it like that: clean a row, then for every column value that should be saved
    just upload it, and that shwo you clean
    
    """

    # clearing columns that should be edited
    for row_to_edit in rows_to_be_edited:
        rows[row_to_edit[0]] = [0 for _ in range(len(rows[row_to_edit[0]]))]

    # editing rows
    for row_to_edit in rows_to_be_edited:
        for value in row_to_edit[1]:
            rows[row_to_edit[0]][value] = 1
    for row in rows:
        print(row)


    return rows


def test3(rows):
    def convert_to_rows(columns):
        # Converting to rows
        rows = [[] for _ in range(len(columns[0]))]
        for column in columns:
            for height in range(len(columns[0])):
                rows[height].append(column[height])
        return rows

    def convert_to_columns(rows):
        # converting to columns
        columns = [[] for _ in range(len(rows[0]))]
        for row in rows:
            for width in range(len(rows[0])):
                columns[width].append(row[width])
        return columns

    # Source

    columns = convert_to_columns(rows)

    # Printing first State
    '''for row in rows:
        print(row)
    print()'''

    for angle in range(2):  # First we search with columns then we search with rows
        if angle == 0:
            vectors = columns
            side = rows
        else:
            vectors = rows
            side = columns

        new_vectors = []  # adding to each vector a sum of values
        for vector in vectors:
            length = 0
            for x in vector:
                length += x
            new_vectors.append([vector, length])

        coordinates_to_check = []  # Those are columns that are an identical pairs,
        # each value is [[vector1.x, vector2.x], number_of_true_values_in_column]
        for i, vector in enumerate(new_vectors[:-1]):
            for j, vector_2 in enumerate(new_vectors[i + 1:]):
                if vector == vector_2:
                    x = [i, j + i + 1]  # first and second column that are identical
                    coordinates_to_check.append([x, vector[1]])  # vector[1] is the length

        # comparing with side
        side_to_be_edited = []  # should be a simple array of pairs of values
        for coordinates in coordinates_to_check:
            side_to_check = []

            for coordinate in coordinates[0]:
                side_sum = 0
                for i, value in enumerate(side[coordinate]):

                    if value == 1:
                        side_sum += 1
                if side_sum > coordinates[1]: # comparing desired length
                    side_to_be_edited.append([coordinate, coordinates[0]]) # row_number  columns that should remain



        """
        Now there should be something like a merge of cordinates to check
        for every row thats edited check if the lenth is corect if not then
        maybe do it like that: clean a row, then for every column value that should be saved
        just upload it, and that shwo you clean
    
        """

        # clearing columns that should be edited
        for row_to_edit in side_to_be_edited:
            side[row_to_edit[0]] = [0 for _ in range(len(side[row_to_edit[0]]))]

        # editing side
        for row_to_edit in side_to_be_edited:
            for value in row_to_edit[1]:
                side[row_to_edit[0]][value] = 1

    # Printing results
    '''for row in side:
        print(row)'''

    return side



def search_for_empty(rows):
    """
    Search for empty square space that should be reflected after swapping X with Y
    :param rows:
    :return:
    """
    def convert_to_columns(rows):
        # converting to columns
        columns = [[] for _ in range(len(rows[0]))]
        for row in rows:
            for width in range(len(rows[0])):
                columns[width].append(row[width])
        return columns
    columns = convert_to_columns(rows)
    """
    First approach, we sort the array, while remembering how to restore it at the end
    """

    old_rows = []
    old_columns = []
    for row in rows:
        old_rows.append(sum(row))
    for column in columns:
        old_columns.append(sum(column))

    new_rows = old_rows.copy()
    new_columns = old_columns.copy()




    def swap_rows(grid, a, b):
        grid[a], grid[b] = grid[b], grid[a]

    def swap_columns(grid, a, b):
        for i in range(len(grid)):
            grid[i][a], grid[i][b] = grid[i][b], grid[i][a]

    history = []  # history of changes, [0 - rows / 1 - co ; a ; b]


    def search_in_rows(grid, x, y):
        for i in range(y + 1, len(grid)):
            if grid[i][x] == 1:
                return i
        return 0


    def search_in_columns(grid, x, y):
        for i in range(x + 1, len(grid[0])):
            if grid[y][i] == 1:
                return i
        return 0

    grid = rows
    old_is_not_rows = True
    old = []
    #while old_is_not_rows:
    for attempts in range(200000):
        if old == grid:
            break
        old = grid.copy()

        for x in range(len(grid[0])):
            for y in range(len(grid)):
                if grid[y][x] != 1:
                    id = search_in_rows(grid, x, y)
                    if id == 0:
                        id = search_in_columns(grid, x, y)
                        if id == 0:
                            continue
                        swap_columns(grid, x, id)
                    swap_rows(grid, y, id)

    for row in grid:
        print(row)

    old_id = []
    #for row in old_rows:'''










def paper_removing_squares(paper):
    """
    This advanced method
    First we go on Y axis, lets say we have 4 missing,
    :param collection:
    :return:
    """

    a = []
    for column in paper:
        a.append(len(column))
    b = []
    c = []
    for value in a:
        pass


    properties_list = [
        [2, 2, 2],
        [2, 1, -1],
        [1, -1, 2],
        [1, -2, -1],
        [-1, 2, 1],
        [-1, 1, -2],
        [-2, -1, 1],
        [-2, -2, -2]]
    for attempts in range(8):
        old_state = paper.copy()

        pairs = []
        for i, column in enumerate(paper):
            if len(column) == 2:
                pairs.append(column)


        occurrences = 0
        x = 0
        for i, item in enumerate(paper):
            if row in item:
                occurrences += 1
                x = i

            """ Maximum occurences usefulness is 4
                                        """
            if occurrences == 1:
                paper[x] = [row]


        if paper == old_state:  # last iteration didn't change anything
            break
    print()

def ingredients():
    # each ingredient has 3 circles with + or - inside and the small or large size
    # red, green, blue - large/small - +/-
    # those values c
    paper = paper_generation()
    stuff = []
    for i in range(8):
        stuff.append(Ingredient(i, i, paper))

    print(stuff[0].properties_list)

    for i in range(1, 8):
        stuff[i].remove_variant([2, 2, 2])

    '''
    # Mixing every item with talon
    for i in range(1, 8):
        potion = stuff[0].create_potion(stuff[i])
        stuff[0].remove_variants(potion)
        print(stuff[0].properties_list)'''


    print()
    paper_removing_unique(paper)
    #removing_unique(stuff)
    print()



'''    print(talon.properties_list)
    talon.remove_variants([0, True])
    print(talon.properties_list)
    talon.remove_variants([1, False])
    print(talon.properties_list)
    talon.remove_variants([2, True])
    print(talon.properties_list)'''


def swap_rows(grid, a, b):
    grid[a], grid[b] = grid[b], grid[a]


def swap_columns(grid, a, b):
    for i in range(len(grid)):
        grid[i][a], grid[i][b] = grid[i][b], grid[i][a]


def sort_columns(grid):
    def search_in_columns(grid, starting_column):
        # searching for available rows
        earliest = 0
        available_columns = []
        for y in range(len(grid)):
            for x in range(starting_column, len(grid[0])):
                if grid[y][x] == 1:
                    available_columns.append(x)
            if len(available_columns) == 0:
                continue
            elif len(available_columns) == 1:
                return available_columns[0]
            else:
                earliest = y
                break

        # determining best available row
        for y in range(earliest + 1, len(grid)):
            present_at_this_height = []
            for column in available_columns:
                if grid[y][column] == 1:
                    present_at_this_height.append(column)

            if len(present_at_this_height) == 1:
                return present_at_this_height[0]

            if len(present_at_this_height) > 0:
                available_columns = present_at_this_height

        return available_columns[0]

    for x in range(len(grid[0])):
        id = search_in_columns(grid, x)
        # id = search_in_columns_len(grid, x)
        if x != id:
            swap_columns(grid, x, id)


def sort_rows(rows):
    """
    Search for empty square space that should be reflected after swapping X with Y
    :param rows:
    :return:
    """

    '''def convert_to_columns(rows):
        # converting to columns
        columns = [[] for _ in range(len(rows[0]))]
        for row in rows:
            for width in range(len(rows[0])):
                columns[width].append(row[width])
        return columns
    columns = convert_to_columns(rows)'''
    """
    First approach, we sort the array, while remembering how to restore it at the end
    """

    '''old_rows = []
    old_columns = []
    for row in rows:
        old_rows.append(sum(row))
    for column in columns:
        old_columns.append(sum(column))

    new_rows = old_rows.copy()
    new_columns = old_columns.copy()'''
    history = []  # history of changes, [0 - rows / 1 - co ; a ; b]


    def search_in_rows(grid, starting_row):
        # searching for available rows
        earliest = 0
        available_rows = []
        for x in range(len(grid[0])):
            for y in range(starting_row, len(grid)):
                if grid[y][x] == 1:
                    available_rows.append(y)
            if len(available_rows) == 0:
                continue
            elif len(available_rows) == 1:
                return available_rows[0]
            else:
                earliest = x
                break

        # determining best available row
        for x in range(earliest + 1, len(grid[0])):
            present_at_this_width = []
            for row in available_rows:
                if grid[row][x] == 1:
                    present_at_this_width.append(row)

            if len(present_at_this_width) == 1:
                return present_at_this_width[0]

            if len(present_at_this_width) > 0:
                available_rows = present_at_this_width

        return available_rows[0]



    def search_in_rows_len(grid, starting_row):
        best_row = 0
        best_id = 0
        for row in range(starting_row, len(grid)):
            value = sum(grid[row])
            if best_row < value:
                best_row = value
                best_id = row
        return best_id

    def search_in_columns_len(grid, starting_column):
        best_column = 0
        best_id = 0
        for column in range(starting_column, len(grid[0])):
            value = 0
            for y in range(len(grid)):
                value += grid[y][column]

            if best_column < value:
                best_column = value
                best_id = column
        return best_id

    grid = rows
    old_is_not_rows = True
    old = []
    #while old_is_not_rows:
    for attempts in range(1):
        if old == grid:
            break
        old = grid.copy()


        for y in range(len(grid)):
            id = search_in_rows(grid, y)
            # by the closest to the left
            if y != id:
                swap_rows(grid, y, id)





        '''for x in range(len(grid[0])):
            id = search_in_columns(grid, x) 
            if x != id:
                swap_columns(grid, x, id)'''

    old_id = []
    #for row in old_rows:'''



def sort_tests(grid):
    draw_grid(grid)

    print("SORT ROWS")
    sort_rows(grid)
    draw_grid(grid)

    old_state = grid
    print("TEST 3")
    test3(grid)
    draw_grid(grid)
    if old_state == grid:
        print("No changes were made")
    else:
        print("Changes are present")

    print("SORT COLUMNS")
    sort_columns(grid)
    draw_grid(grid)

    old_state = grid
    print("TEST 3")
    test3(grid)
    draw_grid(grid)
    if old_state == grid:
        print("No changes were made")
    else:
        print("Changes are present")


def place_spot(table, x, y):
    table.pop(y)
    for row in table:
        row.pop(x)

def better_copy(grid):
    new_grid = []
    for row in grid:
        new_grid.append(row[:])  # row[:] prevents original row from being referenced
    return new_grid

def attempts_test(grid):
    """
    method that aims to test every possible combination of inputs in order to find a spots that cannot be chosen
    Method uses recursion
    :param grid:
    :return:
    """

    def search_next_spot(grid):
        """
        It's a recursion that searches for a spot that once chosen makes the puzzle unsolvable.
        After finding it, it should return it
        :param grid: a matrix of at least 1 : 1 in size
        :return:
        """
        # On current grid we are searching for every selectable spot

        for y in range(len(grid)):
            for x in range(len(grid[0])):

                if x == 3:  # DEBUG
                    print()

                if grid[y][x] == 1:  # if spot can be selected, we test it
                    if len(grid) == 1:  # Branch is successful
                        return True

                    # grid has more spaces to be tested
                    # START OF NEW SERIES OF TESTS
                    # NEW BRANCH
                    current_grid = better_copy(grid)  # Copy on which we will be working

                    # CHOICE
                    place_spot(current_grid, x, y)  # removing rows and columns aligned with selected spot

                    # result: TRUE (previous choice was correct) we can forget about current grid

                    # False (Previous choice was a mistake)
                    # search rest of the branches

                    # Path is False until we find at least 1 correct path
                    result = search_next_spot(current_grid)  # We test every possibility for each previous choice

                    if result:
                        return True

                    # END OF A BRANCH

        # This place is reached only if grid was empty, which means that the branch is false
        return False

    #draw_grid(grid)
    problems = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 1:
                current_grid = better_copy(grid)  # new branch

                place_spot(current_grid, x, y)  # removing rows and columns aligned with selected spot

                result = search_next_spot(current_grid)
                if result is False:
                    problems.append([x, y])
                    grid[y][x] = 0

    if len(problems) == 0:
        print("it's a correct grid")
    else:
        print("it's not a correct grid, problems: ", problems)
    return problems






def randomise_source(rows):

    for _ in range(20):
        a = []
        b = []
        for _ in range(2):
            a.append(random.randrange(0, len(rows)))
            b.append(random.randrange(0, len(rows[0])))

        swap_columns(rows, a[0], a[1])
        swap_rows(rows, b[0], b[1])


def draw_grid(grid):
    for row in grid:
        for value in row:
            if value == 1:
                print("|#|", end="")
            else:
                print("| |", end="")
        print()
    print()

def testing_methods():

    source_basic = [[1, 0, 1, 0],
                    [0, 1, 0, 1],
                    [1, 0, 1, 1],
                    [0, 1, 0, 1]]

    # 2 = rows of source_basic
    source_basic2 = [[1, 0, 1, 0],
                     [0, 1, 0, 1],
                     [0, 0, 1, 1],
                     [0, 0, 1, 1]]

    source_basic3 = [[1, 1, 0, 0],
                     [0, 1, 0, 1],
                     [0, 0, 1, 1],
                     [0, 1, 0, 1]]

    source_basic4 = [[1, 0, 0, 0],
                     [0, 1, 0, 0],
                     [0, 0, 1, 1],
                     [0, 0, 1, 1]]

    source_basic5 = [[0, 1],
                    [1, 1]]

    source_basic6_false = [[1, 0, 1],
                           [1, 1, 0],
                           [0, 0, 1]]

    source_basic6_true = [[1, 0, 1],
                          [1, 1, 0],
                          [1, 0, 1]]

    source_advanced = [
        [0, 0, 1, 1, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 0, 0, 0],
        [1, 0, 1, 1, 0, 0, 1, 1],
        [1, 1, 1, 1, 0, 0, 1, 1],

        [0, 0, 0, 0, 1, 1, 1, 1],
        [0, 0, 0, 0, 1, 1, 0, 1],
        [0, 0, 0, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 1, 1, 0, 0]]

    source_advanced2 = [
        [1, 0, 1, 1, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 0, 0, 0],
        [1, 0, 0, 1, 1, 1, 0, 0],
        [1, 1, 1, 1, 1, 1, 0, 0],

        [0, 0, 0, 0, 1, 0, 1, 1],
        [0, 0, 0, 0, 0, 1, 0, 1],
        [0, 0, 0, 0, 1, 0, 1, 1],
        [0, 0, 0, 0, 1, 1, 1, 1]]

    for source in [source_basic3]:
    #for source in [source_basic6_true, source_basic6_false]:
        #randomise_source(source)

        old_state = better_copy(source)

        #new_state = test3(source)
        #new_state = sort_tests(source)


        while True:
            problems = attempts_test(source)
            if len(problems) == 0:
                break
            for problem in problems:
                source[problem[1]][problem[0]] = 0


        if old_state == source:
            print("No changes were made")
        else:
            print("Changes are present")
        draw_grid(old_state)
        draw_grid(source)


if __name__ == '__main__':
    print("start")

    testing_methods()
    #ingredients()
