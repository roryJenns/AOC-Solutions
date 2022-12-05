import numpy as np

TEST_INPUT = "test_input.txt"
REAL_INPUT = "input.txt"
# INPUT_FILENAME = TEST_INPUT
INPUT_FILENAME = REAL_INPUT


def readData(filename):
    file = "input/"+filename
    with open(file, "r") as f:
        data = list(map(lambda x : x[:-1], f.readlines()))
    return data


def processData1():
    data = readData(INPUT_FILENAME)
    middle = data.index("")
    crate_d = data[:middle]
    for i, row in enumerate(crate_d):
        crate_d[i] = [row[j] for j in range(1,len(row), 4)]

    ins_d = data[middle+1:]


    columns = len(crate_d[0])
    rows = len(crate_d)
    crate_d_t = [[0 for x in range(rows)] for y in range(columns)]
    for x in range(columns):
        for y in range(rows):
            crate_d_t[x][rows-y-1] = crate_d[y][x]
    
    for stack in crate_d_t:
        while stack[-1] == ' ':
            stack.pop()

    for i, ins in enumerate(ins_d):
        ins = ins.split(" ")
        ins = (int(ins[1]),int(ins[3]),int(ins[5]))
        ins_d[i] = ins
    
    return crate_d_t, ins_d


def part1():
    stacks,instructions = processData1()

    # print(stacks)

    while len(instructions) > 0:
        num, frm, to = instructions.pop(0)
        frm -= 1
        to -= 1

        hold = []
        for _ in range(num):
            hold.append(stacks[frm].pop())
        
        for _ in range(num):
            stacks[to].append(hold.pop(0))
        
        # add bounds checking on stacks
        # print(stacks)
    
    word = ""
    for stack in stacks:
        word = word + stack[-1]

    # print(stacks)

    return word

def processData2():
    data = readData(INPUT_FILENAME)
    return data

def part2():
    stacks,instructions = processData1()

    # print(stacks)

    while len(instructions) > 0:
        num, frm, to = instructions.pop(0)
        frm -= 1
        to -= 1

        hold = []
        for _ in range(num):
            hold.append(stacks[frm].pop())
        
        for _ in range(num):
            stacks[to].append(hold.pop())
        
        # add bounds checking on stacks
        # print(stacks)
    
    word = ""
    for stack in stacks:
        word = word + stack[-1]

    # print(stacks)

    return word

def main():
    total = part1()
    print("PART 1:",total)

    total2 = part2()
    print("PART 2:",total2)

main()

# C:\Users\roryj\OneDrive - The University of Nottingham\AOC-Solutions\2022\Day5\input
