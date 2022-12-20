"""
In simple terms, Dungeon world, is a game about a heroes where a challenge is to get to an 11th level.
Purpose of this project is to test what is the optimal number of heroes. (generally the more the better,
but by how much the lower number of them affects the outcome of adventures
"""



import random




class Hero:
    def __init__(self):
        self.stats = {
            "str": 0,
            "dex": 0,
            "con": 0,
            "int": 0,
            "wis": 0,
            "cha": 0
        }
        self.bonus = {
            "str": 0,
            "dex": 0,
            "con": 0,
            "int": 0,
            "wis": 0,
            "cha": 0
        }

        self.level = 1
        self.experience = 0

        self.max_hp = 0
        self.hp = 0

        self.dmg = 10

    def character_creation(self):
        values = [16, 15, 13, 12, 9, 8]
        names = ["str", "dex", "con", "int", "wis", "cha"]
        for i, stat_name in enumerate(names):
            self.stat_update(stat_name, values[i])

    def stat_update(self, name, value):

        self.stats[name] += value

        # BONUS
        bonus_table = [3, 5, 8, 12, 15, 17]  # 18 -> +3
        bonus_values = [-3, -2, -1, 0, 1, 2, 3]
        value = self.stats[name]
        x = 0
        for i in bonus_table:
            if i >= value:
                break
            x += 1
        self.bonus[name] = bonus_values[x]

        # HP
        if name == "con":
            self.max_hp = self.stats["con"] + 8  # TODO class related value
            if self.hp < self.max_hp:
                self.hp += 1

    def exp(self, value=1):
        self.experience += value
        if self.experience >= self.level + 7:
            self.experience -= (self.level + 7)
            self.level += 1
            if self.level == 11:
                self.level = 10  # TODO Think how to remove it
                print("You won")
                return "Max level"
            # TODO choose a new advanced move for classes
            # TODO if wizard get a new spell for your book

            # choose a stat, increase it by 1
            names = ["str", "dex", "con", "int", "wis", "cha"]
            names_to_level = []
            for name in names:
                if self.stats[name] < 18:
                    names_to_level.append(name)
            stat_to_lvl = random.choice(names_to_level)

            self.stat_update(stat_to_lvl, 1)




    def print_stats(self):
        names = ["str", "dex", "con", "int", "wis", "cha"]
        for stat in names:
            print(stat, self.stats[stat], self.bonus[stat])
        print()



def dice_roll(bonus):
    value = random.randint(1, 6) + random.randint(1, 6) + bonus
    if value >= 10:
        return 2
    elif value >= 7:
        return 1
    return 0


def move(hero):
    names = ["str", "dex", "con", "int", "wis", "cha"]


    # attack 2 - dmg choose +1d6 / no counter attack 1 dmg
    # shoot 2 - dmg 1 dmg but choose uncool move/ -1d6dmg / -1ammo
    # defend 2 - get 3    1 - get 1
    """
    Redirect an attack from the thing you defend to yourself
    Halve the attack’s effect or damage
    Open up the attacker to an ally giving that ally +1 forward against the attacker
    Deal damage to the attacker equal to your level
    """
    # spout lore  2 GM tells useful thing about the subject relevant to your situation.
    #  1 GM only tells it’s on you to make it useful

    # Discern Realities 2 ask 3    1 ask 1      # take +1 forward on acting on those
    """
    What happened here recently?
    What is about to happen?
    What should I be on the lookout for?
    What here is useful or valuable to me?
    Who’s really in control here?
    What here is not what it appears to be?
    """

    # Parley 2 ok   1 ok but you need a proof

    # every stat - defy danger 2 ok 1 ok BUT

    # Aid/interfere roll + bond  2 choose +1 / -2  1 same as 2 but you also uncool


    # special moves

    # death 2 - cool 1 bargain
    # take watch wisdom  2 everyone gets +1 forward 1 cool 0 enemy gets a drop
    # undertake journey 3 guys get a job, no one can have more than 1.    On 2:
    ''' quartermaster reduces number of rations required by 1
    Trailblazer half the journey time 
     scout give a drop on an enemy '''

    # Special effects:

    # Encumbrance if weight <= load nothing   <= load + 2 suffer -1  > load + 2 loose 1 weight and roll -1 or auto fail
    # make camp

    """ Receiving EXP    
    Did we learn something new and important about the world?
    Did we overcome a notable monster or enemy?
    Did we loot a memorable treasure?
    For each True mark 1 exp for each hero
    """



    score = dice_roll(hero.bonus[names[0]])



if __name__ == '__main__':
    print("start")

    h = Hero()
    h.character_creation()
    for i in range(4000):
        if i % 5 == 0:
            h.print_stats()
        h.exp(1)




    print("end")