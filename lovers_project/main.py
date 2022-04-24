import village
import random
import universe
import tools


def main_menu(launch_setting=None):
    '''
    Allows to:
    create new save
    load a save
    exit the game
    '''
    saved_games = []

    if launch_setting == "basic_test":
        saved_games.append(new_save())
        village.world = saved_games[0]
        village.gameplay_loop()

    choice = 0
    while choice != 9:
        print("1 new save 2 play existing save 9 exit the game")
        choice = int(input())

        if choice == 1:
            saved_games.append(new_save())
        elif choice == 2:
            if len(saved_games) == 0:
                saved_games.append(new_save())

            while choice != 0:
                for i, save in enumerate(saved_games):
                    print(i + 1, save, end=" ")
                print("0 return to menu")
                choice = int(input())
                if choice != 0 and choice <= len(saved_games):
                    village.world = saved_games[choice - 1]
                    village.gameplay_loop()

    print("Exiting the game")


def new_save():
    '''
    Generation of general world state. (allows a player for a gameplay progression even after loosing village)
    :return:
    '''
    village.world = universe.Class_World()
    village.new_village()
    return village.world


def monster_info_tests():
    earth = universe.Class_World()
    knowledge = None
    for monster in earth.monsters:
        print("\n\n\n\n\n\n\n")
        print(monster.stats)
        for knowledge in range(monster.power + 1):
            print(knowledge, end="  ")
            print(monster.info())
            monster.update_info()

    print("\n\n\n\n\n\n\n")
    tester = universe.Monster("a", [1, 5, 7])
    print(knowledge, end="  ")
    print(tester.info())


if __name__ == '__main__':
    main_menu("basic_test")
    # monster_info_tests()

