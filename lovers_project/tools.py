def player_interface (choices=None):
    """
    This is a function that should replace input system like this one inside of village.gameplay_loop
    :param choices:
    :return:
    """
    if choices is None:
        pass


def player_input (choices=None):
    if choices is None:
        return 0
    choice = int(input())
    if choice > choices or choice < 0:
        return 0
    return choice


def greatest_enum (enum):
    max_value = 0
    for en in enum:
        if max_value < en.value:
            max_value = en.value
    return max_value


def print_enum (enum):
    for i in enum:
        i.print()
        break
