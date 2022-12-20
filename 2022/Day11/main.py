import numpy as np
from monkey import Monkey

TEST_INPUT = "test_input.txt"
REAL_INPUT = "input.txt"
# INPUT_FILENAME = TEST_INPUT
INPUT_FILENAME = REAL_INPUT

PART1_MAX_ROUND = 20
PART2_MAX_ROUND = 10000

NUM_MONKEYS = 4 if INPUT_FILENAME == TEST_INPUT else 8
LCM = 23*19*13*17 if INPUT_FILENAME == TEST_INPUT else 7*13*5*19*2*11*17*3


# def readData():
#     file = "input/"+INPUT_FILENAME
#     with open(file, "r") as f:
#         data = list(map(lambda x : x[:-1], f.readlines()))
#     return data


def processData1():
    global lcm
    monkeys = [None] * NUM_MONKEYS
    if INPUT_FILENAME == TEST_INPUT:
        monkeys[0] = Monkey([79,98], lambda x: x*19, 23, 2, 3)
        monkeys[1] = Monkey([54,65,75,74], lambda x: x+6, 19, 2, 0)
        monkeys[2] = Monkey([79,60,97], lambda x: x*x, 13, 1, 3)
        monkeys[3] = Monkey([74], lambda x: x+3, 17, 0, 1)
    else:
        monkeys[0] = Monkey([66,79], lambda x: x*11, 7, 6, 7)
        monkeys[1] = Monkey([84, 94, 94, 81, 98, 75], lambda x: x*17, 13, 5,2)
        monkeys[2] = Monkey([85, 79, 59, 64, 79, 95, 67], lambda x: x+8, 5, 4,5)
        monkeys[3] = Monkey([70], lambda x: x+3, 19,6,0)
        monkeys[4] = Monkey([57, 69, 78, 78], lambda x: x+4, 2,0,3)
        monkeys[5] = Monkey([65, 92, 60, 74, 72], lambda x: x+7, 11,3,4)
        monkeys[6] = Monkey([77, 91, 91], lambda x: x*x, 17,1,7)
        monkeys[7] = Monkey([76, 58, 57, 55, 67, 77, 54, 99], lambda x: x+6,3,2,1)

    return monkeys


def part1():
    monkeys = processData1()
    for roundNo in range(PART1_MAX_ROUND):
    # for roundNo in range(2):
        # for i,monkey in enumerate(monkeys):
        #     print(str(i)+"x",monkey.items)
        for i,monkey in enumerate(monkeys):
            # print(str(i)+"y",monkey.items)
            itemList = monkey.takeTurnPart1()
            for indexTo, item in itemList:
                monkeys[indexTo].addItem(item)
        # print(roundNo, "insp:", list(map(lambda m: m.inspectCount, monkeys)))
        
    
    monkeyInspects = sorted(list(map(lambda m: m.inspectCount, monkeys)), reverse=True)

    return monkeyInspects[0] * monkeyInspects[1]

def part2():
    monkeys = processData1()
    for roundNo in range(PART2_MAX_ROUND):
        for i,monkey in enumerate(monkeys):
            itemList = monkey.takeTurnPart2()
            for indexTo, item in itemList:
                t_item = item % LCM
                monkeys[indexTo].addItem(t_item)
        # if roundNo %50 == 0:
        #     print(roundNo)
    
    monkeyInspects = sorted(list(map(lambda m: m.inspectCount, monkeys)), reverse=True)

    return monkeyInspects[0] * monkeyInspects[1]

def main():
    total = part1()
    print("PART 1:",total)

    total2 = part2()
    print("PART 2:",total2)



main()

# C:\Users\roryj\OneDrive - The University of Nottingham\AOC-Solutions\2022

# part 1 - 3213 is too low

# def test(h,t):
#     print(catchUp(h,t))
# test((0,0),(0,0))
# test((1,0),(0,0))
# test((2,0),(0,0))
# test((3,0),(1,0))
# test((4,0),(2,0))
# test((4,1),(3,0))
# test((4,2),(3,0))
# test((4,3),(4,1))
# test((4,4),(4,2))



