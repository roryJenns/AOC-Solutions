INPUT = "input.txt"
OUTPUT = "output.txt"

squares = []
instructions = []


def ReadInput():
    f = open(INPUT, "r")
    read = f.readline()
    while len(read) > 1:
        line = int(read[:-1].split(",")[0])
        squares.append(line)
        read = f.readline()

    line = f.readline()

    while len(line) > 1:
        linemod = line[11:].split("=")
        linemod[1] = int(linemod[1])
        instructions.append(tuple(linemod))
        line = f.readline()

    f.close()


ReadInput()

f = open(OUTPUT, "w+")
for x in range(655):
    if x in squares:
        f.write(str("#"))
    else:
        f.write(str("."))
f.write("\n")
for x in range((655*2+1)-1,655,-1):
    if x in squares:
        f.write(str("#"))
    else:
        f.write(str("."))


f.close()