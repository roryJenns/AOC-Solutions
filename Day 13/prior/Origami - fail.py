INPUT = "input.txt"
OUTPUT = "output.txt"

squares = []
instructions = []

maxs = tuple([0,0])

# data is too big to literally simulate
# I put in array, length in ~1300 which 
# 1300>1024 aka 2^10 aka apparently the array size limit lol

# Works for small data though!


def ReadInput():
    global maxs
    f = open(INPUT, "r")
    read = f.readline()
    while len(read) > 1:
        line = list(map(int,read[:-1].split(",")))
        squares.append(line)
        maxs = max(line[0],maxs[0]), max(line[1],maxs[1])
        read = f.readline()
        #print(read)

    maxs = maxs[0] + 1, maxs[1] + 1

    line = f.readline()

    while len(line) > 1:
        linemod = line[11:].split("=")
        linemod[1] = int(linemod[1])
        instructions.append(tuple(linemod))
        line = f.readline()

    f.close()

def CreateGrid(sizes):
    grid = [[0 for x in range(maxs[0])] for y in range(maxs[1])]
    for coord in squares:
        grid[coord[1]][coord[0]] = 1
    return grid

def FoldX(coord, grid):
    width = len(grid[0])
    half_width = int(width/2)
    height = len(grid)
    newgrid = [[0 for x in range(half_width)] for y in range(height)]
    for y, line in enumerate(grid):
        for x in range(half_width):
            newgrid[y][x] = max(line[x], line[width-x-1])

    return newgrid

def FoldY(coord, grid):
    width = len(grid[0])
    height = len(grid)
    half_height = int(height/2)
    
    newgrid = [[0 for x in range(width)] for y in range(half_height)]
    for y in range(half_height):
        line = grid[y]
        for x, val in enumerate(line):
            newgrid[y][x] = max(val, grid[height-y-1][x])

    return newgrid

def CountGrid(grid):
    total = 0
    for line in grid:
        for val in line:
            total += val
    return total

def PrintGrid(grid):
    p = ['.','#']
    for line in grid:
        for val in line:

            print(p[val], end="")
        print()
    print("END")

def WriteGrid(grid, file):
    p = ['.','#']
    with open(file, "w+") as f:
        for line in grid:
            for val in line:
                f.write(p[val])
            f.write("\n")

def main():
    ReadInput()
    grid = CreateGrid(maxs)
    filec = 0

    WriteGrid(grid, f"output{filec}.txt")
    filec += 1

    for instruction in instructions:
        print(CountGrid(grid))
        inst, num = instruction
        if inst == "x":
            grid = FoldX(num, grid)
        elif inst == "y":
            grid = FoldY(num, grid)
        WriteGrid(grid, f"output{filec}.txt")
        filec += 1
        # PrintGrid(grid)
    
    print(CountGrid(grid))
    
    total = CountGrid(grid)
    return total

total = main()

print("After all folds:",total)


