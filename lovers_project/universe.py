import random

class class_world:
    def __init__(self):
        self.current_village = None
        self.monsters = self.generate_monsters()

    def generate_monsters(self):
        names = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
        monsters = []
        for name in names:
            stats = []
            for i in range(3):
                stats.append(random.randint(1, 8))
            monsters.append(monster(name, stats))
        return monsters

    def __repr__(self):
        return "save_" + str(self.current_village)

class monster:
    def __init__(self, name, stats):
        self.name = name
        self.stats = stats
        self.knowledge = 0

    def info(self):
        if self.knowledge == 0:
            return "? ? ?"
        power = 0
        for stat in self.stats:
            if power < stat:
                power = stat

        if self.knowledge > power:
            return self.stats
        else:
            # generating ranges for possible stats
            # current possible max range (useless for player) 1-8
            '''
            for i in range(self.knowledge):
            '''
            return "1-8 1-8 1-8"

