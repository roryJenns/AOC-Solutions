class Probe ():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.startVelocity = (0,0)
        self.xVelocity = 0
        self.yVelocity = 0
        self.xRange = (0,0)
        self.yRange = (0,0)
        self.highestY = 0
    
    def iterateMove(self):
        self.x += self.xVelocity
        self.y += self.yVelocity
        if self.xVelocity > 0:
            self.xVelocity -= 1
        elif self.xVelocity < 0:
            self.xVelocity += 1
        self.yVelocity -= 1
    
    def setVelocity(self, x ,y):
        self.startVelocity = (x,y)
    
    def setVelocityToStart(self):
        self.xVelocity = self.startVelocity[0]
        self.yVelocity = self.startVelocity[1]

    def addVelocity(self, velo):
        self.xVelocity += velo[0]
        self.yVelocity += velo[1]

    def setTarget(self, x, y):
        self.xRange = x
        self.yRange = y
    
    def checkInTarget(self):
        xmin = self.xRange[0]
        xmax = self.xRange[1]
        ymin = self.yRange[0]
        ymax = self.yRange[1]

        if xmin <= self.x <= xmax and ymin <= self.y <= ymax:
            return True
        else:
            return False
    
    def checkBeyondTarget(self):
        ymin = self.yRange[0]
        ymax = self.yRange[1]

        if self.y < ymin and self.yVelocity < 0:
            return True
        else:
            return False

    def printCoords(self):
        print(self.x, self.y)
    
    def reset(self):
        self.x = 0
        self.y = 0
        self.setVelocityToStart()
    
    def checkIfValid(self):
        highest = 0
        self.reset()
        i = 0
        while not self.checkBeyondTarget():
            i += 1
            self.iterateMove()
            highest = max(self.y, highest)
            # if i % 1 == 0:
            #     self.printCoords()
            if self.checkInTarget():
                self.highestY = highest
                # print("IN TARGET")
                return True
        return False

# TEST TARGET
# x=20..30
# y=-10..-5

# TARGET AREA
# x=253..280, 
# y=-73..-46


def main():
    xRange = (253, 280)
    yRange = (-73,-46)

    print("give start velocity")
    # x = int(input())
    # y = int(input())

    probe = Probe()
    probe.setTarget(xRange, yRange)
    print(xRange, yRange)

    distinctVelocities = []

    startX = 22
    endX = 280
    minY = -73
    failureInARow = 0
    i = 0
    for x in range(startX, endX+1):
        for y in range(minY, 100+1):
            probe.setVelocity(x,y)
            if probe.checkIfValid():
                # print("HIT WITH:",x,y)
                distinctVelocities.append((x,y))
    
    #print(distinctVelocities)
    print(len(distinctVelocities))

main()
