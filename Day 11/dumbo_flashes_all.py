INPUT_FILENAME = "input.txt"
OUTPUT_FILENAME = "output_all.txt"

MAX_ITERATIONS = 10000

round_flashes = 0

def IncFlashes():
    global round_flashes
    round_flashes += 1

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

for x in range(1,MAX_ITERATIONS+1):
    round_flashes = 0

    OneIter()
    OneReset()

    f.write("{}:{}\n".format(x,round_flashes))
    if round_flashes == 100:
        break
        
f.write("{}:{}\n".format(x,round_flashes))
f.close()

print(round_flashes)
# print("end")
