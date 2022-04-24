import random


class Class_World:
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
            monsters.append(Monster(name, stats))
        return monsters

    def __repr__(self):
        return "save_" + str(self.current_village)


class Monster:
    def __init__(self, name, stats):
        self.name = name
        self.stats = stats
        self.lore = 0
        self.knowledge = []
        self.power = max(stats)

        # maximum range for specific value
        ranges_of_power = [4, 6, 8, 10, 12, 20]
        for info_value in self.stats:
            for power_level in ranges_of_power:
                if power_level >= info_value:
                    self.knowledge.append([1, power_level])
                    break

    def info(self):
        info = ""
        for stat_range in self.knowledge:
            if stat_range[0] == stat_range[1]:
                info += str(stat_range[0]) + "  "
            else:
                info += str(stat_range[0]) + "-" + str(stat_range[1]) + "  "
        return info

    def update_info(self):  # single increase in knowledge
        self.lore += 1
        if self.lore >= self.power:  # full knowledge
            self.knowledge = ([x, x] for x in self.stats)
            return

        # generating ranges for possible stats
        # current possible max range (useless for player) 1-8

        info_for_player = []
        for i, info_value in enumerate(self.knowledge):
            edge_values = [info_value[0], info_value[1]]

            if random.randint(0, 1) == 0 and edge_values[0] != self.stats[i]:
                edge_values[0] += 1
            elif edge_values[1] != self.stats[i]:
                edge_values[1] -= 1
            elif edge_values[0] != self.stats[i]:
                edge_values[0] += 1
            info_for_player.append(edge_values)
        self.knowledge = info_for_player

