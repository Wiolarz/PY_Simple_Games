import random
import combat
import universe
import tools

from enum import Enum


# global variable
world = universe.Class_World()

class Building:
    def __init__(self):
        pass

class Construction_Building:
    def __init__(self):
        self.progress = 3
        self.next_house = Building()

    def day_update(self):
        self.progress -= 1
        if self.progress == 0:
            return True
        return False

    def new_house(self):
        print("House " + str(self.next_house) + " has been finished")
        new_house = self.next_house
        self.next_house = None
        return new_house

    def new_project(self):
        if self.next_house == None:
            self.progress = 3
            self.next_house = Building()  # TODO list of possible building to be built
        return "Currently " + str(self.next_house) + " is being built. Time left: " + str(self.progress)

class Village:
    def __init__(self):
        self.villagers = 10
        self.fighters = [combat.Fighter()]
        self.buildings = []
        self.constructor = Construction_Building()

    def new_fighter(self):
        if self.villagers > 0:
            self.fighters.append(combat.Fighter())
            self.villagers -= 1
        else:
            new_village()  # Death of a village

    def __repr__(self):
        return "vil[" + str(self.villagers) + "]"


def new_village():
    '''

    :return:
    '''
    world.current_village = Village()


def choose_fighter(possible_fighters):
    for fighter in possible_fighters:
        print()
    return possible_fighters[0]


def exploration():

    hero = choose_fighter(world.current_village.fighters)
    combat.forest_exploration(hero, world.monsters)

    if hero.hp <= 0:
        hero = None
    else:
        hero.generate_moves()  # reset hero status


def day_change():
    """
    Calls for events related to dawn of a new day
    """

    # filling min. value of fighters in village
    if len(world.current_village.fighters) == 0:
        world.current_village.new_fighter()

    constructor = world.current_village.constructor
    if constructor.day_update():
        world.current_village.buildings.append(constructor.new_house())


class Player_Action(Enum):
    EXPLORE = 1
    EVENTS = 2
    BUILDING = 3
    EXIT = 9

    def print(self):
        # for i, action in enumerate(Player_Action):
        #    print(i + 1, action, end="  ")
        print("1 explore forest 2 manage events 3 manage buildings 9 return to main menu")


def gameplay_loop():
    '''

    :return:
    '''

    choice = 0
    day = 1
    while choice != Player_Action.EXIT:

        # Events related to passing days
        if choice == Player_Action.EXPLORE:
            day += 1
            day_change()

        print("Day: ", day)
        # Player_Action.print(Player_Action())

        tools.print_enum(Player_Action)

        choice = Player_Action(tools.player_input(tools.greatest_enum(Player_Action)))

        if choice == Player_Action.EXPLORE:
            exploration()
        elif choice == Player_Action.EVENTS:
            pass
        elif choice == Player_Action.BUILDING:
            print(world.current_village.constructor.new_project())
