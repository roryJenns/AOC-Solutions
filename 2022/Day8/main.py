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
    raw = readData()

    data = list(map( lambda x: list(map(int,x)), raw))

    return data


def part1():
    data = processData1()

    width = len(data[0])
    height = len(data)

    visible = [[0 for _ in range(width)] for _ in range(height)]

    tallest = -1

    # verticle
    for column in range(width):
        # from top
        tallest = -1
        for row in range(0,height):
            if data[row][column] > tallest:
                tallest = data[row][column]
                visible[row][column] = 1
        # from bottom
        tallest = -1
        for row in range(height-1,-1,-1):
            if data[row][column] > tallest:
                tallest = data[row][column]
                visible[row][column] = 1
    # horizontal
    for row in range(height):
        # from left
        tallest = -1
        for column in range(0,width):
            if data[row][column] > tallest:
                tallest = data[row][column]
                visible[row][column] = 1
        # from right
        tallest = -1
        for column in range(width-1,-1,-1):
            if data[row][column] > tallest:
                tallest = data[row][column]
                visible[row][column] = 1

    # for line in visible:
    #     print(line)

    return sum(map(sum,visible))

def part2():
    data = processData1()

    width = len(data[0])
    height = len(data)

    views = [[0 for _ in range(width)] for _ in range(height)]

    def calcView(x,y):
        dists = [0,0,0,0]
        tree_height = data[y][x]

        # going up
        row = y-1
        while row >= 0:
            dists[0] += 1
            if data[row][x] >= tree_height:
                break
            row -= 1

        # going left
        col = x-1
        while col >= 0:
            dists[1] += 1
            if data[y][col] >= tree_height:
                break
            col -= 1
        
        # going down
        row = y+1
        while row < height:
            dists[2] += 1
            if data[row][x] >= tree_height:
                break
            row += 1
        
        # going right
        col = x+1
        while col < width:
            dists[3] += 1
            if data[y][col] >= tree_height:
                break
            col += 1
            
        # if (x,y) == (2,3):
        #     print(dists)
        
        return dists[0]*dists[1]*dists[2]*dists[3]


    for y in range(height):
        for x in range(width):
            views[y][x] = calcView(x,y)


    # for line in views:
    #     print(line)

    return max(map(max,views))

def main():
    total = part1()
    print("PART 1:",total)

    total2 = part2()
    print("PART 2:",total2)

main()