import numpy as np
from time import time

import heapq


TEST_INPUT = "test_input.txt"
REAL_INPUT = "input.txt"
# INPUT_FILENAME = TEST_INPUT
INPUT_FILENAME = REAL_INPUT

DATA_WIDTH = 8 if INPUT_FILENAME == TEST_INPUT else 143
DATA_HEIGHT = 5 if INPUT_FILENAME == TEST_INPUT else 41

DATA_TOTAL = DATA_HEIGHT*DATA_WIDTH


def readData():
    file = "input/"+INPUT_FILENAME
    with open(file, "r") as f:
        data = list(map(lambda x : x[:-1], f.readlines()))
    return data

def processData():
    raw = readData()

    grid = [[0 for _ in range(DATA_WIDTH)] for _ in range(DATA_HEIGHT)]

    se = [0,0]
    end = (0,0)
    def convChar(c:str, x, y) -> int:
        if c == 'S':
            se[0] = (x,y)
            c = 'a'
        if c == 'E':
            se[1] = (x,y)
            c = 'z'
        val = ord(c)-ord('a')
        return val

    for y, word in enumerate(raw):
        for x, char in enumerate(word):
            grid[y][x] = convChar(char,x,y)

    return (grid, se[0], se[1])
 
def getAdjacent(grid, x,y):
    max_next = grid[y][x] + 1
    children = []
    
    def check(x,y):
        if y < 0 or x < 0 or y == DATA_HEIGHT or x == DATA_WIDTH:
            return
        t = grid[y][x]
        if t <= max_next:
            children.append((x,y))

    check(x,y+1)
    check(x,y-1)
    check(x+1,y)
    check(x-1,y)

    return children

def generalSearch(grid,fr,to):
    queue = [fr]

    steps = [[-1 for _ in range(DATA_WIDTH)] for _ in range(DATA_HEIGHT)]

    steps[fr[1]][fr[0]] = 0

    while len(queue) > 0:
        curr = queue.pop(0)
        x,y = curr
        if curr == to:
            return steps[y][x]
        for x2,y2 in getAdjacent(grid, x, y):
            if steps[y2][x2] == -1:
                steps[y2][x2] = steps[y][x] + 1
                queue.append((x2,y2))

    return -1 # -1 if no path

def part1():
    grid, start, end = processData()
    steps = generalSearch(grid,start,end)
    print(steps)
    return steps

def part2():
    grid, start, end = processData()

    starts = []
    for y, line in enumerate(grid):
        for x, h in enumerate(line):
            if h == 0:
                starts.append((x,y))

    steps = []
    for start in starts:
        step_count = generalSearch(grid,start,end)
        steps.append(step_count)

    return min(filter(lambda x: x > 0, steps))

def main():
    steps = part1()
    print("1:",steps)

    min_steps = part2()
    print("2:",min_steps)

main()





