import numpy as np
from time import time

import heapq


TEST_INPUT = "test_input.txt"
REAL_INPUT = "input.txt"
# INPUT_FILENAME = TEST_INPUT
INPUT_FILENAME = REAL_INPUT

SOURCE_X = 500
SOURCE_Y = 0


def readData():
    file = "input/"+INPUT_FILENAME
    with open(file, "r") as f:
        data = list(map(lambda x : x[:-1], f.readlines()))
    return data


def processData():
    minx = SOURCE_X
    miny = SOURCE_Y
    maxx = SOURCE_X
    maxy = SOURCE_Y

    raw = readData()

    def process(line:str):
        return list(map(lambda x : list(map(int, x.split(","))), line.split(" -> ")))

    data = list(map(process, raw))
    for line in data:
        for x,y in line:
            minx = min(minx,x)
            miny = min(miny,y)
            maxx = max(maxx,x)
            maxy = max(maxy,y)
    
    SPACING = 3
    data = list(map(lambda line : list(map( lambda pair : (pair[0]-minx+SPACING, pair[1]-miny) , line)), data))

    return data, (maxx-minx + 2*SPACING, maxy-miny + 2), (SOURCE_X-minx+SPACING,SOURCE_Y-miny)

AIR = 0
ROCK = 1
SAND = 2
SOURCE = 3

def printCave(cave_map):
    for l in cave_map:
        for c in l:
            if c == AIR:
                print(".",end="")
            elif c == ROCK:
                print("#",end="")
            elif c == SAND:
                print("o",end="")
            elif c == SOURCE:
                print("+",end="")
        print("")

def carveCave():
    DEBUG = False
    data, bounds, source = processData()
    x_range, y_range = bounds

    cave_map = [[AIR for _ in range(x_range)] for _ in range(y_range)]
    cave_map[source[1]][source[0]] = SOURCE
    for path in data:
        start = path[0]
        for point in path:
            # paint from point to point
            # print(point)
            for y in range(min(start[1], point[1]), max(start[1], point[1])+1):
                for x in range(min(start[0], point[0]), max(start[0], point[0])+1):
                    cave_map[y][x] = ROCK
            start = point

    return cave_map, source

def fillCave(cave_map, source):
    cave_depth = len(cave_map)
    end_flag = False
    resting_sand = 0
    while not end_flag:
        sand = source
        while True:
            if sand[1]+1 == cave_depth:
                end_flag = True
                break

            if cave_map[sand[1]+1][sand[0]] == AIR:
                sand = (sand[0], sand[1] + 1)
            elif cave_map[sand[1]+1][sand[0]-1] == AIR:
                sand = (sand[0]-1, sand[1] + 1)
            elif cave_map[sand[1]+1][sand[0]+1] == AIR:
                sand = (sand[0]+1, sand[1] + 1)
            else:            
                resting_sand += 1
                cave_map[sand[1]][sand[0]] = SAND
                break
    return resting_sand

def fillCaveFloor(cave_map, source):
    cave_depth = len(cave_map)
    cave_width = len(cave_map[0])
    end_flag = False
    resting_sand = 0
    while not end_flag:
        sand = source
        while True:
            if sand[1]+1 == cave_depth: # on floor
                resting_sand += 1
                cave_map[sand[1]][sand[0]] = SAND
                break
            elif cave_map[sand[1]+1][sand[0]] == AIR: # down free
                sand = (sand[0], sand[1] + 1)
            elif sand[0] == 0: # left wall
                resting_sand += cave_depth - sand[1]
                cave_map[sand[1]][sand[0]] = SAND
                break
            elif cave_map[sand[1]+1][sand[0]-1] == AIR: # down left free
                sand = (sand[0]-1, sand[1] + 1)
            elif sand[0] == cave_width-1: # right wall
                resting_sand += cave_depth - sand[1]
                cave_map[sand[1]][sand[0]] = SAND
                break
            elif cave_map[sand[1]+1][sand[0]+1] == AIR: # down right free
                sand = (sand[0]+1, sand[1] + 1)
            else: # comes to rest
                resting_sand += 1
                if cave_map[sand[1]][sand[0]] == SOURCE:
                    end_flag = True
                cave_map[sand[1]][sand[0]] = SAND
                if resting_sand % 100 == 0:
                    printCave(cave_map)
                break
    return resting_sand

def part1():
    cave_map, source = carveCave()

    resting_sand = fillCave(cave_map, source)

    printCave(cave_map)
    
    return resting_sand
    

def part2():
    cave_map, source = carveCave()

    resting_sand = fillCaveFloor(cave_map, source)

    printCave(cave_map)
    
    return resting_sand
    return 0

def main():
    a = part1()
    print("1:",a)
    b = part2()
    print("2:",b)

main()
