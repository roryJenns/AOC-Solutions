import numpy as np


TEST_INPUT = "test_input.txt"
REAL_INPUT = "input.txt"
INPUT_FILENAME = TEST_INPUT
INPUT_FILENAME = REAL_INPUT


def readData():
    file = "input/"+INPUT_FILENAME
    with open(file, "r") as f:
        data = list(map(lambda x : x[:-1], f.readlines()))
    return data


def right(pair):
    return (pair[0]+1, pair[1])

def left(pair):
    return (pair[0]-1, pair[1])

def up(pair):
    return (pair[0], pair[1]+1)

def down(pair):
    return (pair[0], pair[1]-1)

def processData1():
    raw = readData()
    
    letter_to_func = {"L": left, "R": right, "U": up, "D": down}

    data = list(map(lambda x: (letter_to_func[x.split(" ")[0]], int(x.split(" ")[1])), raw))

    return data


def catchUp(head, tail):
    diff = (head[0]-tail[0],head[1]-tail[1])

    no_move = [(0,0),(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]

    if diff in no_move:
        return tail
    
    if diff == (0,2):
        return (tail[0],tail[1]+1)
    if diff == (0,-2):
        return (tail[0],tail[1]-1)
    if diff == (2,0):
        return (tail[0]+1,tail[1])
    if diff == (-2,0):
        return (tail[0]-1,tail[1])

    if diff in [(2,2),(2,1),(1,2)]:
        return (tail[0]+1,tail[1]+1)
    if diff in [(-2,2),(-2,1),(-1,2)]:
        return (tail[0]-1,tail[1]+1)
    if diff in [(2,-2),(2,-1),(1,-2)]:
        return (tail[0]+1,tail[1]-1)
    if diff in [(-2,-2),(-2,-1),(-1,-2)]:
        return (tail[0]-1,tail[1]-1)
        

    print(diff)
    exit()


def printFile(arr, filename):
    with open("output/"+filename, "w+") as f:
        for row in arr:
            for col in row:
                c = " " if col == 0 else "#"
                f.write(c)
            f.write("\n")

def printToGrid(visited, name):
    min_x = min(visited, key=lambda x: x[0])[0]
    max_x = max(visited, key=lambda x: x[0])[0]
    min_y = min(visited, key=lambda x: x[1])[1]
    max_y = max(visited, key=lambda x: x[1])[1]

    print(min_x, max_x, min_y, max_y)

    grid = np.zeros((max_y-min_y+1, max_x-min_x+1), dtype=int)

    for x,y in visited:
        grid[y-min_y][x-min_x] = 1

    printFile(grid, name)
    
def part1():
    data = processData1()

    visited = set()

    head_coords = (0,0)
    tail_coords = (0,0)

    visited.add(tail_coords)

    for move, count in data:
        for i in range(count):
            head_coords = move(head_coords)
            tail_coords = catchUp(head_coords, tail_coords)
            visited.add(tail_coords)

    printToGrid(visited, "grid1.txt")
    return len(visited)

def part2():
    data = processData1()

    visited = set()

    KNOT_COUNT = 10
    TAIL = KNOT_COUNT - 1
    knots = [(0,0) for _ in range(KNOT_COUNT)]
    visited.add(knots[TAIL])

    for move, count in data:
        for i in range(count):
            knots[0] = move(knots[0])
            for i in range(1,KNOT_COUNT):
                knots[i] = catchUp(knots[i-1], knots[i])
            visited.add(knots[-1])

    printToGrid(visited, "grid2.txt")

    return len(visited)

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



