INPUT_FILENAME = "mod_input.txt"
OUTPUT_FILENAME = "minimum_points.txt"

DATA_WIDTH = 102

data = []
local_mins = []
local_mins_arr = []

f = open(INPUT_FILENAME, "r")
for x in range(DATA_WIDTH):
    data.append(f.readline()[:-1])
f.close()

def CheckAll(x,y):
    d = data[y][x]
    #if min([d,data[y-1][x],data[y+1][x],data[y][x-1],data[y][x+1]]) == d: # Fun idea but fails on flat surfaces
    #if d < data[y-1][x] and d < data[y+1][x] and d < data[y][x-1] and d < data[y][x+1]: # I don't like this
    if d < min([data[y-1][x], data[y+1][x], data[y][x-1], data[y][x+1]]): # Good compromise
        # local minimum found
        local_mins.append(int(d))
        local_mins_arr.append([x,y])

def CheckTopRow(x,y):
    d = data[y][x]
    if d < min([data[y+1][x], data[y][x-1], data[y][x+1]]):
        local_mins.append(int(d))
def CheckBottomRow(x,y):
    d = data[y][x]
    if d < min([data[y-1][x], data[y][x-1], data[y][x+1]]):
        local_mins.append(int(d))
def CheckRightColumn(x,y):
    d = data[y][x]
    if d < min([data[y-1][x], data[y+1][x], data[y][x-1]]):
        local_mins.append(int(d))
def CheckLeftColumn(x,y):
    d = data[y][x]
    if d < min([data[y-1][x], data[y+1][x], data[y][x+1]]):
        local_mins.append(int(d))
def CheckCorners():
    d = data[0][0]
    if d < min([data[1][0], data[0][1]]):
        local_mins.append(int(d))
    d = data[0][-1]
    if d < min([data[1][-1], data[0][-2]]):
        local_mins.append(int(d))
    d = data[-1][0]
    if d < min([data[-2][0], data[-1][1]]):
        local_mins.append(int(d))
    d = data[-1][-1]
    if d < min([data[-2][-1], data[-1][-2]]):
        local_mins.append(int(d))

def main(): ## Should I also include 0s next to each other?
    # Check Main Body
    for y in range(1,DATA_WIDTH-1):
        for x in range(1,DATA_WIDTH-1):
            CheckAll(x,y)

## START CODE ##

main()
print(local_mins)
risk_level = sum(local_mins)+len(local_mins)
print(risk_level)

f = open(OUTPUT_FILENAME, "w+")
for min in local_mins_arr:
    f.write("{},{}\n".format(min[0],min[1]))
f.write("{}\n".format(risk_level))
f.close()




