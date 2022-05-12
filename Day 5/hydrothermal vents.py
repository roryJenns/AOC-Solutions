WIDTH = 991
HEIGHT = 990

MAX = 1000

array = [[0 for x in range(WIDTH)] for y in range(HEIGHT)]

f = open("input.txt", "r")
line = f.readline()

while line != "-1":
#for i in range(10):
    start, end = line.split(" -> ")
    startstr = start.split(",")
    endstr = end.split(",")
    endstr[-1] = endstr[-1][:-1]

    startstr = list(map(int, startstr))
    endstr = list(map(int, endstr))

    x = startstr[0]
    y = startstr[1]
    xinc = 0
    yinc = 0
    index = 0
    if startstr[0] > endstr[0]:
        xinc = -1
    elif startstr[0] < endstr[0]:
        xinc = 1
    if startstr[1] > endstr[1]:
        yinc = -1
    elif startstr[1] < endstr[1]:
        yinc = 1
    if xinc == 0:
        index = 1
    for i in range(abs(startstr[index] - endstr[index])+1):
        array[y][x] += 1
        x += xinc
        y += yinc
    
    line = f.readline()
f.close()


counter = 0
fw = open("output.txt", "w")
for line in array:
    for item in line:
        
        #for line in array:
        if item == 1:
            fw.write(".")
        elif item > 1:
            fw.write("#")
        else:
            fw.write(" ")
        
        if item >= 2:
            counter += 1
    fw.write("\n")

fw.close()

print(counter)

