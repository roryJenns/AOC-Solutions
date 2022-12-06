import numpy as np

TEST_INPUT = "test_input.txt"
REAL_INPUT = "input.txt"
# INPUT_FILENAME = TEST_INPUT
INPUT_FILENAME = REAL_INPUT


def readData():
    file = "input/"+INPUT_FILENAME
    with open(file, "r") as f:
        data = list(map(lambda x : x[:-1], f.readlines()))
    return data


def processData1():
    data = readData()
    return data[0]

def uniqueWindow(window_max):
    line = processData1()
    length = len(line)

    window_size = 1
    chars = [line[0]]
    start=0
    end=0

    while window_size < window_max and end+1 < length:
        end += 1
        window_size += 1
        c = line[end]
        while c in chars:
            start += 1
            window_size -= 1
            chars.pop(0)
        chars.append(c)

    return end + 1


def part1():
    return uniqueWindow(4)

def part2():

    return uniqueWindow(14)

def main():
    total = part1()
    print("PART 1:",total)

    total2 = part2()
    print("PART 2:",total2)

main()

# C:\Users\roryj\OneDrive - The University of Nottingham\AOC-Solutions\2022\Day5\input
