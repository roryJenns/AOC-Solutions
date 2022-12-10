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

    counter = 0
    value = 0

    data = list(map(lambda x : (x,0) if x=="noop" else (x.split(" ")[0], int(x.split(" ")[1])), raw))

    counter = 0
    value = 1

    updates = {0:1}

    for line in data:
        command = line[0]
        if command == ("noop"):
            counter += 1
        else:
            counter += 2
            val = line[1]
            value += val
            updates[counter+1] = value
    
    return updates

def processData2():
    data = processData1()

    for key in sorted(data.keys()):
        value = data[key]
        i = key + 1
        while i not in data and i < 241:
            data[i] = value
            i += 1
    
    return data

def part1():
    data = processData2()
    endCounter = 221
    sum = 0

    for key in range(20,endCounter,40):
        signalStrength = key * data[key] 
        sum += signalStrength

    return sum

def writeToFile(grid, filename):
    with open("output/"+filename, "w+") as f:
        for line in grid:
            f.write(''.join(line) + "\n")
        
def part2():

    data = processData2()

    lines = int(240/40)

    grid = [[]] * lines
    for lineNumber in range(lines):
        message = ['.'] * 40
        for col in range(40):
            mid = data[lineNumber*40 + col+1]
            if col == mid or col == mid-1 or col == mid+1:
                message[col] = '#'
        grid[lineNumber] = message

    writeToFile(grid,INPUT_FILENAME)

    return "Look in file"

def main():
    total = part1()
    print("PART 1:",total)

    total2 = part2()
    print("PART 2:",total2)



main()

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



