INPUT_FILENAME = "mod_input.txt"
POINTS_FILENAME = "minimum_points.txt"
OUTPUT_FILENAME = "output_part2.txt"

DATA_SIZE = 209
DATA_WIDTH = 102

data = []
basins = []

class Basin():
    def __init__(self, min):
        self.min = min
        self.size = 0
        self.points = []

    def getMinCoords(self):
        return self.min[0], self.min[1]
    
    def addPoint(self, x, y):
        self.points.append([x,y])
        self.size += 1


f = open(INPUT_FILENAME, "r")
for x in range(DATA_WIDTH):
    data.append(f.readline()[:-1])
f.close()

f = open(POINTS_FILENAME, "r")
for x in range(DATA_SIZE):
    coords = f.readline()[:-1].split(",")
    basins.append(Basin([int(coords[0]), int(coords[1])]))
f.close()

def FindBasin(basin, x,y):
    #if data[x,y] == "9" or [x,y] in basin.points:
    #print(x,y)
    if max(x,y) > 101 or min(x,y) < 1:
        return 
    if data[y][x] == "9":
        return
    if [x,y] in basin.points:
        return
    basin.addPoint(x,y)
    FindBasin(basin, x,y+1)
    FindBasin(basin, x+1,y)
    FindBasin(basin, x,y-1)
    FindBasin(basin, x-1,y)

def main():
    for basin in basins:
        coords = basin.getMinCoords()
        FindBasin(basin, coords[0], coords[1])


## START CODE ##

main()

largest = [basins[i].size for i in range(3)]
basin_largest = [basins[i] for i in range(3)]

for i in range(3, len(basins)):
    small = min(largest)
    new = basins[i].size
    if new > small:
        basin_largest[largest.index(small)] = basins[i]
        largest[largest.index(small)] = new

final = largest[0] * largest[1] * largest[2]

f2 = open(OUTPUT_FILENAME, "w+")
for basin in basins:
    f2.write("{},".format(basin.size))
f2.write("\n")
for basin in basin_largest:
    f2.write("{}\n".format(basin.min))
f2.write("{}\n".format(largest))
f2.write("{}\n".format(final))
f2.close()





