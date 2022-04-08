import random
import combat
import universe
import tools

from enum import Enum



# global variable
world = universe.class_world()








class village:
    def __init__(self):
        self.villagers = 10
        self.fighters = [combat.fighter()]

    def new_fighter(self):
        if self.villagers > 0:
            self.fighters.append(combat.fighter())
            self.villagers -= 1
        else:
            new_village()  # Death of a village

    def __repr__(self):
        return "vil[" + str(self.villagers) + "]"

def new_village():
    '''


    :return:
    '''
    world.current_village = village()



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
    '''
    Calls for events related to dawn of a new day
    '''

    # filling min. value of fighters in village
    if len(world.current_village.fighters) == 0:
        world.current_village.new_fighter()




class Player_Action(Enum):
    EXPLORE = 1
    EVENTS = 2
    BUILDING = 3
    EXIT = 9

    def print(self):
        #for i, action in enumerate(Player_Action):
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
        if choice == 1:
            day += 1
            day_change()

        print("Day: ", day)
        #Player_Action.print(Player_Action())

        for i in Player_Action:
            i.print()
            break

        choice = Player_Action(tools.player_input(tools.greatest_enum(Player_Action)))

        if choice == Player_Action.EXPLORE:
            exploration()
        elif choice == Player_Action.EVENTS:
            pass
        elif choice == Player_Action.BUILDING:
            pass



