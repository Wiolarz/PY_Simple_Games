import village
import random
import universe













def main_menu():
    '''
    Allows to:
    create new save
    load a save
    exit the game
    '''

    saved_games = []

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
    earth = universe.class_world()
    village.new_village(earth)
    return earth




if __name__ == '__main__':
    main_menu()

