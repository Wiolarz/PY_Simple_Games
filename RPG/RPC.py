"""

"""



if __name__ == '__main__':

    targets = {}

    for hp in range(1, 13):
        for armor in range(0, 11):
            name = "H" + str(hp) + "A" + str(armor)
            targets[name] = {"hp": hp, "armor": armor}
    hp_stats = []

    dmg_stats = []
    pen_stats = []




    # weapons creation
    #cost name dmg penetration range size
    # range 0 melee 1 close 2 normal 3 long
    # size 0 small 1 small 2 medium 3 large
    weapons = [
    [1, "knife", 2, 1, 0, 0],
    [2, "handgun", 3, 3, 1, 0],
    [3, "shotgun", 5, 1, 1, 2],
    [3, "rifle", 4, 2, 2, ],
    [4, "uzi", 4, 1, 1],
    [4, "desert_eagle", 4, 3, 1],
    [5, "galil", 5, 2, 2],
    [5, "pump_shotgun", 6, 1, 1],
    [6, "p90", 6, 2, 1],
    [6, "katana", 8, 5],
    [7, "m4a4", 6, 3],
    [7, "CZ", 4, 2],
    [8, "awp", 7, 4],
    [8, "combat_shotgun", 7, 3],
    [8, "mantis_blades", 7, 5]]






    for target in targets:



                hp = targets[target]["hp"]
                hits = 0
                while hp > 0:
                    arm = targets[target]["armor"] - penetration
                    if arm < 0:
                        arm = 0
                    dmg = damage - arm
                    if dmg <= 0:
                        break
                    hp -= dmg
                    hits += 1
                print(target, " ", hits, " weapons: ", damage, "|", penetration, sep="")

    pass