"""
Mythic is a tool for solo role playing, this code aims to allow for save system, and smooth gameplay experience,
while using this tool

#TODO:
1 Fate check
2 chaos factor
3
4 export results




Mythic game loop:
1 Follow expectations (general story structure, continue story)
2 If there is uncertainty about either: a) story choices b) details --> Use Fate chart/check


Fate chart/check:
1 form a yes/no question
2 assign odds 5- 5+ 0 (50/50, Likely, Very
    Likely, Nearly Certain, Certain, Unlikely, Very
    Unlikely, Nearly Impossible, or Impossible
3 Check chart/get modifiers
4 roll 1d100 / 2d10 (total sum: 2-4 <10 11< 18-20)
5 if both numbers of the roll are the same like 9-9 5-5 and the single digit is smaller or equal to a chaos factor
    random event occurs

Random events:
1 fate question / Interrupt scene
2 consider context
3 1d100 random event focus table
4 Choose a Meaning table that fits, roll for 2 inspirational words
5 combine

Roll something from list

First scene, 3 methods:
1 write
2 random event
3 meaning table 2 words inspiration
4 4W meaning table structure: who, what, where, why

Testing scenes:
1 expected
2 1d10 chaos factor to check if altered/interrupted (odd/even

Altered scene:
1 next expectation -> doit
2 Tweak change a single element
3 fate question
4 meaning table pair
5 1d10 scene adjustment table

Interrupt scene
1 random event

Begin and End scenes

1 Interesting thing happening
2 certain time period or location
3 narrative shift
4 mood
5 automatic interrupt?? Choose to
have a Scene begin as an Interrupt without
testing it against the Chaos Factor.


Generate NPC behaviour
1 Expectations - not crucial -> doit
2 no idea -> meaning table
3 expectations - crucial -> fate question

End of scene bookkeeping
1 edit list elements
2 adjust chaos factor: if player in control -1 if not +1

Determine NPC Statistics:
1 expected -> doit
2 fate question
3 Interpret fate question -> value above 25% higher; expected; value -25%; value -50%;
random event - generate random event associated


Thread progress track:
1 focus thread
2 choose a track (10, 15, 20)
3 Progress - resolving the focus thread in a scene awards 2 progress points
4 flash-point - dramatic event -> 2 progress, mark did flash-point happen
5 track flash-point - if enough progress and no flash-point -> it occurs
(random event with automatic event focus of current context)
6 discovery check: fate is something discovered? (no less than 50/50)
yes -> thread discovery table
exceptional yes -> roll twice
no - pass
exceptional no -> you cannot make another discovery check for the rest of the scene


Plot Armor:
the focus thread cannot be resolved through normal mythic play as long as the thread progress track is still in progress
any adventure results that would complete or end the thread, must be interpreted differently
Conclusion:
when the progress track is completed -> random event with auto event focus

Peril Points:
default number is 2
choose how they replenish
each point can avert outcome that would end the adventure or an important narrative



"""
import sys
import random


def fate_chart():
    pass  # TODO fate chart number generator (195)

def check_fate(chaos=5, odds=5):
    roll = roll2d10()
    if roll[0] == roll[1]:
        print("random event", end=" ")

    if odds <= 2:  # TODO think about changing odds to -+ value same with chaos
        odds -= 1
    elif odds >= 8:
        odds += 1

    if chaos <= 2:
        chaos -= 1
    elif chaos >= 8:
        chaos += 1

    result = sum(roll) + chaos + odds - 10


    if result <= 4:
        return 3
    elif result <= 10:
        return 2
    elif result <= 17:
        return 1
    return 0


def event_focus_table():
    score = random.randint(1, 100)
    results = {5: "remote event",
               10: "ambiguous event",
               20: "new npc",
               40: "npc action",
               45: "npc negative",
               50: "npc positive",
               55: "move toward a thread",
               65: "move away from a thread",
               70: "close a thread",
               80: "PC negative",
               85: "PC positive",
               100: "Current context"}
    for res_key in results.keys():
        if int(res_key) >= score:
            print(results[res_key])
            return
    """
    REMOTE EVENT
Your PC is expecting news 
from afar and now seems like 
a good time for it to arrive.
AMBIGUOUS EVENT
The adventure has slowed and you 
are ready for a mystery to pursue.
NEW NPC
There is a logical reason for 
a new NPC to appear in your 
adventure right now.
NPC ACTION
Your PC is waiting on the 
action of NPCs to move the 
adventure forward.
NPC NEGATIVE or  NPC POSITIVE
You want to shift the focus of 
your adventure onto an NPC 
right now, maybe to develop new 
storylines in your adventure.
MOVE TOWARD A THREAD
Your adventure has stalled 
and needs a push forward. 
This is especially useful for 
an Interrupt Scene.
MOVE AWAY FROM A THREAD or  PC NEGATIVE
You want a new challenge 
for your PC to face.
PC POSITIVE
Your PC is having a hard time 
and could use a break.
CLOSE A THREAD
The adventure has gotten 
complicated and you want to 
thin out the Threads List.
CURRENT CONTEXT
 » The Random Event could help 
explain a Fate Question result.
 » A Random Event could be 
disruptive to the current action.
    """


def scene_adjustment_table():
    roll1 = random.randint(1, 10)
    roll2 = 11
    two_rolls = False
    if roll1 >= 7:
        two_rolls = True
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
    results = {
        1: "Remove A Character",
        2: "Add A Character",
        3: "Reduce/Remove An Activity",
        4: "Increase An Activity",
        5: "Remove An Object",
        6: "Add An Object"}
        #7: "Make 2 Adjustments"}

    for res_key in results.keys():
        if int(res_key) >= roll1:
            print(results[res_key])
            if two_rolls:
                two_rolls = False
            else:
                return
        if int(res_key) >= roll2:
            print(results[res_key])
            if two_rolls:
                two_rolls = False
            else:
                return

class Thread:
    def __init__(self, max_points):
        self.name = ""
        self.points = 1
        self.max_points = max_points

        """
        for every 5 points there is a seperate checkmark "did falshpoint happen
        on last spot there is a text "Flashpoint +2"
        last spot is always conclusion (no flash point text in last 5 points)
        """

    def points_change(self, value):
        self.points += value
        # TODO add checking for max and flashpoints
        return "points change " + str(value)

    def discovery_check(self):
        random.randint(1, 10) + self.points
        results = {9: self.points_change(2),
                   10: "flash point +2",
                   14: self.points_change(1),  # weak event  (nothing happened act is noticed)
                   17: self.points_change(3),
                   18: "flash point +3",
                   19: self.points_change(2), # weak event  (nothing happened act is noticed)
                   24: self.points_change(1),  # something related to previous event progression
                   30: self.points_change(2)}  # -|-
        for res_key in results.keys():
            if int(res_key) >= score:
                print(results[res_key])
                return




def roll2d10():
    return [random.randint(1, 10), random.randint(1, 10)]



def generate_meaning_tables():
    source = open("meaning_tables.txt").read().split("\n")
    list_of_all_tables = []
    current_list = []
    for line in source:
        if line[0] == "#":
            list_of_all_tables.append(current_list)
            current_list = [line[2:]]
        else:
            if line[1] == ":":
                current_list.append(line[4:])
            else:
                current_list.append(line[5:])
    list_of_all_tables.pop(0)

    meaning_tables = {}

    for list in list_of_all_tables:
        meaning_tables[list[0]] = list[1:]
        #print(len(list), list)
    print(len(list_of_all_tables))
    for key in meaning_tables:
        print(key, meaning_tables[key])




def basic_gameplay():
    while True:
        print("1: 2d10   2: event_focus   3: scene adjustment    4: ")
        keyboard = input()
        if keyboard == "1":
            print(roll2d10())
        elif keyboard == "2":
            event_focus_table()
        elif keyboard == "3":
            scene_adjustment_table()
        elif keyboard == "4":
            pass

        #generate_meaning_tables()

    '''for _ in range(100):
        scene_adjustment_table()
        print()'''


def current_tests():
    pass



if __name__ == '__main__':
    print('Start')


    import time
    a = time.process_time()
    basic_gameplay()
    # current_tests()
    b = time.process_time()
    print(a, b)
    print("End")



