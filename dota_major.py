"""
Program aims to showcase the chances each dota 2 team has in getting a direct invite to "TI" by points.
"""

from itertools import permutations

teams = {
    "thunder": 1540,
    "lgd": 1500,
    "tsm": 1380,
    "og": 1340,
    "beastcoast": 1295,
    "tundra": 1212,
    "gladiators": 1130,
    "boom": 1122.5,
    "EG": 1052.5,
    "fnatic": 1020,
    "spirit": 990,
    "aster": 940,
    "liquid": 890,
    "rng": 738.42,
    "outsiders": 660.05,
    "quincy": 582.49,
    "extreme": 440,
    "navi": 341.67,
    "talon": 300,
    "entity": 100
}
major_teams = ["tundra", "og", "liquid", "entity", "spirit", "navi", "outsiders", "rng", "aster", "extreme", "lgd",
               "boom", "talon", "fnatic", "EG", "quincy", "thunder", "beastcoast"]

major_points = [820, 740, 670, 590, 515, 515, 360, 360]

def team_score(team):
    return teams[team]

def direct_TI():
    top_12 = []
    for team in teams:
        top_12.append(team)
    top_12.sort(reverse=True, key=team_score)
    top_12 = top_12[:12]
    return top_12
    #print(top_12)

def permutation():
    """
    Creation of every possible results state. Then comparing number occurrences of being in top 12 by a team
    :return:
    """
    global teams
    teams_copy = teams.copy()
    perm_list = permutations(major_teams, 8)
    leng = 0
    rankings = {}
    for team in teams:
        rankings[team] = 0
    for perm in perm_list:
        leng += 1
        if leng % 100000 == 0:
            print(leng)
        for i, team in enumerate(perm):
            teams[team] += major_points[i]
        top = direct_TI()
        for team in top:
            rankings[team] += 1

        teams = teams_copy.copy()
    print(rankings)

def what_team_needs(team_name="liquid"):
    """
    After providing team name, program provides the user with teams placements needed to get invite
    :return:
    """
    for team_name in major_teams:
        print("\n\n\n")
        print(team_name)
        points = [major_points[x] for x in [7, 5, 3, 2, 1, 0]]
        points.insert(0, 0)  # first position in array represent not getting points

        for place, team_placement in enumerate(points):  # 0 first place 5 "5-6" 7 "7-8"
            score = teams[team_name] + team_placement
            stronger_teams = []
            for enemy_team in teams:
                min_place = None
                if enemy_team in ["thunder", "lgd", "tsm", "og", "entity"]:
                    continue

                for i, enemy_result in enumerate(points):
                    if i == place and i not in [5, 7]:  # don't calculate the same placements
                        continue
                    enemy_score = teams[enemy_team] + enemy_result
                    if enemy_score > score:
                        stronger_teams.append([enemy_team, i])
                        break

            # LIST IS FINISHED
            sum_of_placements = {6: 1, 5: 2, 4: 3, 3: 4, 2: 6, 1: 8}
            wrong_teams = []
            for id, better_team in enumerate(stronger_teams):
                if better_team[1] in sum_of_placements.keys():
                    for spot in range(better_team[1], 0, -1):
                        if sum_of_placements[spot] == 0:
                            wrong_teams.append(better_team)
                            break
                        sum_of_placements[spot] -= 1




            # OUTPUT
            placement_translator = ["any", "TOP-8", "TOP-6", "TOP-4", "TOP-3", "TOP-2", "TOP-1"]
            if len(stronger_teams) - len(wrong_teams) > 12:
                print(placement_translator[place], stronger_teams)
            else:
                print(placement_translator[place], "success")
                break

def draw_test():
    """
    Test to check if there could be a draws in points between teams
    :return:
    """
    points = [major_points[x] for x in [0, 1, 2, 3, 4, 5, 7]]

    for team in major_teams:
        for place, score in enumerate(points):
            test_score = teams[team] + score
            for enemy_team in major_teams:

                for i, e_score in enumerate(points):
                    if i == place and i not in [5, 7]:  # don't calculate the same placements
                        continue
                    enemy_score = teams[enemy_team] + e_score
                    if enemy_team == team:
                        continue
                    if test_score == enemy_score:
                        print(test_score, team, place, enemy_team, i)


def final_score():
    '''score = {'thunder': 13366080, 'lgd': 13366080, 'tsm': 13366080, 'og': 13366080, 'beastcoast': 13366080,
             'tundra': 13366080, 'gladiators': 13302576, 'boom': 12986532, 'EG': 11432640, 'fnatic': 8847160,
             'spirit': 6527736, 'aster': 4870080, 'liquid': 4455360, 'rng': 4378242, 'outsiders': 4166860,
             'quincy': 3687522, 'extreme': 2689268, 'navi': 1615882, 'talon': 1236622, 'entity': 0}
    '''
    score = {'thunder': 1764322560, 'lgd': 1764322560, 'tsm': 1764322560, 'og': 1764322560, 'beastcoast': 1764207360,
             'tundra': 1760751360, 'gladiators': 1669264848, 'boom': 1595864520, 'EG': 1308097440, 'fnatic': 1045013760,
             'spirit': 893829888, 'aster': 799384320, 'liquid': 783999360, 'rng': 726038592, 'outsiders': 657040032,
             'quincy': 526066704, 'extreme': 305309712, 'navi': 168019416, 'talon': 111693168, 'entity': 0}

    for team in score.keys():
        #percentage = "{:.2f}%".format(score[team] / 1764322560)
        percentage = "{:.2f}%".format(score[team] / 1764322560 * 100)
        print(team, percentage)

if __name__ == '__main__':
    what_team_needs()

    #draw_test()

    #final_score()
    #permutation()
    pass
