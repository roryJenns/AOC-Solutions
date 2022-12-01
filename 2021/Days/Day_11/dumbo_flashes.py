INPUT_FILENAME = "input.txt"
OUTPUT_FILENAME = "output.txt"

ITERATIONS = 100

total_flashes = 0

def IncFlashes():
    global total_flashes
    total_flashes += 1

class Dumbo():
    def __init__(self):
        self.energy = 0
        self.flashed = False
        self.connected = []

    def incEnergy(self):
        self.energy += 1
        if self.energy > 9:
            self.flash()
    
    def flash(self):
        if not self.flashed:
            self.flashed = True
            IncFlashes()
            for coord in self.connected:
                grid[coord[1]][coord[0]].incEnergy()
            True
        False

    def setEnergy(self, energy):
        self.energy = energy
    
    def reset(self):
        if self.energy > 9:
            self.energy = 0
            self.flashed = False

    def addConnection(self, x,y):
        self.connected.append([x,y])

def PrintGrid():
    for line in grid:
        for dumbo in line:
            if dumbo.energy > 9:
                print(".", end="")
            else:
                print(dumbo.energy, end="")
        print()
    print()

grid = [[Dumbo() for x in range(10)] for x in range(10)]
xoff = [-1,0,1,-1,1,-1,0,1]
yoff = [-1,-1,-1,0,0,1,1,1]

f = open(INPUT_FILENAME, "r")
for y in range(10):
    for x in range(10):
        grid[y][x].energy = int(f.read(1))
        for i in range(8):
            xaim = x+xoff[i]
            yaim = y+yoff[i]

            if max(xaim, yaim) >= 10 or min(xaim,yaim) < 0:
                continue

            grid[y][x].addConnection(xaim,yaim)
    f.read(1)
f.close()

def OneIter():
    for row in grid:
        for dumbo in row:
            dumbo.incEnergy()
def OneReset():
    for row in grid:
        for dumbo in row:
            dumbo.reset()

f = open(OUTPUT_FILENAME, "w+")

# print("Start")
# PrintGrid()
for x in range(1,ITERATIONS+1):
    # print("Run:",x)
    OneIter()
    OneReset()
    # PrintGrid()

    # if x % 10 == 0:
    f.write("{}:{}\n".format(x,total_flashes))
        
f.write("{}:{}\n".format(x,total_flashes))
f.close()

print(total_flashes)
# print("end")
