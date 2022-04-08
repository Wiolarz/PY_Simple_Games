import random
import combat
import universe

from enum import Enum




world = universe.class_world()

# global variable






class village:
    def __init__(self):
        self.villagers = 10
        self.fighters = []

    def new_fighter(self):
        if self.villagers > 0:
            hero = combat.fighter()
            self.villagers -= 1
        else:
            new_village()  # Death of a village
            hero = combat.fighter()
            world.current_village.villagers -= 1
    def __repr__(self):
        return "vil[" + str(self.villagers) + "]"

def new_village():
    '''


    :return:
    '''
    world.current_village = village()



def choose_fighter(possible_fighters):
    return possible_fighters[0]

def exploration():

    hero = choose_fighter(world.current_village.fighters)
    combat.forest_exploration(hero, world.monsters)

    if hero.hp <= 0:
        hero = None
    else:
        hero.generate_moves()  # reset hero status



def day_change():

    if len(world.current_village.fighters) == 0:
        world.current_village.new_fighter()




class Player_Action(Enum):
    EXPLORE = 1
    EVENTS = 2
    BUILDING = 3
    EXIT = 9

    def print(self):
        print("1 explore forest 2 manage events 3 manage buildings 9 return to main menu")




def gameplay_loop():
    '''

    :return:
    '''

    choice = 0

    day = 1
    while choice != Player_Action.EXIT:

        # Events related to passing days
        if choice == 1:
            day += 1
            day_change()

        print("Day: ", day)
        #Player_Action.print(Player_Action())
        print(Player_Action.EXIT)
        choice = Player_Action(int(input()))






        if choice == Player_Action.EXPLORE:
            exploration(world.current_village.villagers)

        elif choice == Player_Action.EVENTS:
            pass
        elif choice == Player_Action.BUILDING:
            pass



