"""
Alchemist is a complex board game.
It's main gameplay system is about discovering properties of ingredients
"""

import random


class Ingredient:
    def __init__(self, name_id, values):
        # 2 big +  1 small +   -2 big -   -1 small
        self.properties_list = [[2, 2, 2],
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
        self.name = items_names[name_id]
        self.color = items_colors[name_id]
        self.red = values[0]
        self.green = values[1]
        self.blue = values[2]
        self.properties = values


        self.produced_potions = {}

    def remove_variants(self, type):
        """
        type:: [color, plus(TRUE)/minus(FALSE)]
        """
        to_be_removed = []
        for i, item in enumerate(self.properties_list):
            if type[1]:
                if item[type[0]] > 0:
                    to_be_removed.append(i)
            else:
                if item[type[0]] < 0:
                    to_be_removed.append(i)
        for i in to_be_removed[::-1]:
            self.properties_list.pop(i)

    def possible_variant(self):
        for potion in self.produced_potions:
            if potion[0] == 0:
                pass



    def create_potion(self, second_element):
        # potions are in order red[0, 1] green[2, 3] blue[4, 5]
        for i, color in enumerate(self.properties):
            if {color, second_element.properties[i]} == {1, 2}:
                potion = 0 + (i * 2)
                self.produced_potions.add([potion, second_element])
                return potion
            elif {color, second_element.properties[i]} == {-1, -2}:
                potion = 1 + (i * 2)
                self.produced_potions.add([potion, second_element])
                return potion
        self.produced_potions.add([-1, second_element])
        return -1  # neutral potion



def ingredients():
    # each ingredient has 3 circles with + or - inside and the small or large size
    # red, green, blue - large/small - +/-
    # those values c

    talon = Ingredient(0, 5)
    print(talon.properties_list)
    talon.remove_variants([0, True])
    print(talon.properties_list)
    talon.remove_variants([1, False])
    print(talon.properties_list)
    talon.remove_variants([2, True])
    print(talon.properties_list)



if __name__ == '__main__':
    print("start")
    ingredients()
