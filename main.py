import random

from basic_tools import output


# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.



def testitng_roman_numbers():
    for i in range(50):
        value = random.randint(0, 2000)
        print(value, " " + output.roman_numbers(value))






# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    '''words = ["apple", "it", "creek", "pelican", "subsequent", "horse",
             "apothecary"]
    wordslen = [len(word) for word in words]
    print(wordslen[-1])
    '''
    a = 5
    while a != 2 and a != 1:
        a -= 1





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
