INPUT = "input.txt"
OUTPUT = "output.txt"

squares = []
instructions = []

# We will compress the data! - Old method had too much empty space anyways

def ReadInput():
    f = open(INPUT, "r")
    read = f.readline()
    while len(read) > 1:
        line = list(map(int,read[:-1].split(",")))
        squares.append(line)
        read = f.readline()

    line = f.readline()

    while len(line) > 1:
        linemod = line[11:].split("=")
        linemod[1] = int(linemod[1])
        instructions.append(tuple(linemod))
        line = f.readline()

    f.close()


def FoldX(coord):
    print(coord)
    width = int(coord*2 + 1)
    # print(width)
    for item in squares:
        x = item[0]
        y = item[1]
        if x == coord:
            continue
        elif x > coord:
            adjusted = list((width-x-1,y))
            
            squares.remove(item)
            if not(adjusted in squares):
                squares.append(adjusted)

def FoldY(coord):
    global squares
    height = coord*2 + 1
    for x,y in squares:
        if y >= coord:
            adjusted = [x,height-y-1]
            squares.pop(squares.index([x,y]))
            if adjusted in squares:
                pass
            else:
                squares.append(adjusted)

def main():
    ReadInput()
    # for instruction in instructions:
    #     inst, num = instruction
    #     if inst == "x":
    #         FoldX(num)
    #     elif inst == "y":
    #         FoldY(num)
    #     print(len(squares))

    inst, num = instructions[0]
    if inst == "x":
        FoldX(num)
    elif inst == "y":
        FoldY(num)
    print(len(squares))
    # print(squares)

    return len(squares)


total = main()
print(squares)
print("After all folds:",total)
