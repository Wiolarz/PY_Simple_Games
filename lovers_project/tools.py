def player_input(range=None):
    if range == None:
        return 0
    choice = int(input())
    if choice > range or choice < 0:
        return 0
    return choice


def greatest_enum(enum):
    max_value = 0
    for en in enum:
        if max_value < en.value:
            max_value = en.value
    return max_value