from time import time

INPUT_FILENAME = "input.txt"
REAL_DATA_SIZE = 100 # Test data - 10, Real data - 100

DATA_SIZE_MULTIPLIER = 5
DATA_SIZE = DATA_SIZE_MULTIPLIER*REAL_DATA_SIZE  

# Don't want to overestimate, try at different values [1-9]
MANHATTAN_MULTIPLIER = 5

class Pair():
    def __init__(self, num, dist):
        self.num = num
        self.dist = dist
    
    def print(self):
        print(self.num, self.dist)

class Node():
    def __init__(self, weight, x, y):
        self.weight = weight
        self.x = x
        self.y = y

    def Weight(self):
        return self.weight

    def X(self):
        return self.x
    
    def Y(self):
        return self.y

    def Index(self) -> int:
        return CoordsToNum(self.x, self.y)


class Graph():
    def __init__(self):
        self.arr = [[0 for x in range(DATA_SIZE)] for y in range(DATA_SIZE)]
    
    def GetArr(self):
        return self.arr

    def GetFromCoords(self, x, y):
        return self.arr[y][x]
    
    def GetFromIndex(self, n):
        x, y = NumToCoords(n)
        return self.arr[y][x]

    def SetFromCoords(self, x, y, val):
        self.arr[y][x] = val
    
    def SetFromIndex(self, n, val):
        x, y = NumToCoords(n)
        self.arr[y][x] = val
    
    def Print(self):
        for line in self.arr:
            for obj in line:
                print(obj.Weight(), end=",")
            print()


class MinPriorityQueue():
    def __init__(self):
        self.arr = []

    def empty(self):
        return len(self.arr) == 0

    def getChildren(self, pair):
        i = self.index(pair)
        left, right = self.getChildIndices(i)
        return tuple(self.arr[left], self.arr[right])
    
    def getParent(self, pair):
        i = self.index(pair)
        return self.arr[self.getParentIndex(i)]
    
    def getChildIndices(self, i):
        left = 2*i+1
        right = 2*i+2
        return left, right
    
    def getParentIndex(self, i):
        return int((i-1)/2)

    def index(self, pair):
        return self.arr.index(pair)
    
    def upHeap(self, pair):
        pairIndex = self.index(pair)
        if pairIndex == 0:
            return
        parent = self.getParentIndex(pairIndex)

        if self.arr[parent].dist > self.arr[pairIndex].dist:

            temp = self.arr[parent]

            self.arr[parent] = pair
            self.arr[pairIndex] = temp
            self.upHeap(pair)

    def downHeap(self, pair): # swap with child
        pairIndex = self.index(pair)
        childLeft, childRight = self.getChildIndices(pairIndex)
        
        smallest = pairIndex
        if childLeft < len(self.arr) and self.arr[childLeft].dist < self.arr[smallest].dist:
            smallest = childLeft
        if childRight < len(self.arr) and self.arr[childRight].dist < self.arr[smallest].dist:
            smallest = childRight
        

        # print("HEAP:",pair.num,pair.dist, self.arr[smallest].num, self.arr[smallest].dist)
        if smallest != pairIndex:
            tempPair = self.arr[smallest]

            self.arr[smallest] = pair
            self.arr[pairIndex] = tempPair
            self.downHeap(pair)

    def extractMin(self):
        value = self.arr[0]
        endValue = self.arr.pop()
        if len(self.arr) > 0:
            self.arr[0] = endValue
            self.downHeap(self.arr[0])
        return value
    
    def addWithPriority(self, num, dist):
        pair = Pair(num, dist)
        self.arr.append(pair)
        self.upHeap(pair)
    
    def add(self, num, dist):
        self.arr.append(Pair(num, dist))

    def decreasePriority(self, num, dist):
        pair = self.findInQueue(num)
        if pair:
            pair.dist = dist
            self.downHeap(pair)
        else:
            self.addWithPriority(num, dist)
    
    def findInQueue(self, n):
        for pair in self.arr:
            if pair.num == n:
                return pair
        return False 

    def print(self):
        for pair in self.arr:
            pair.print()


def ReadDataExpanded(graph):
    weight_adjust = [0,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]
    for row_iteration in range(5):
        f = open(INPUT_FILENAME, "r")
        for row in range(REAL_DATA_SIZE):
            line = f.readline()[:-1]
            for col_iteration in range(5):
                for col, data in enumerate(line):
                    weight = weight_adjust[int(data)+col_iteration+row_iteration]
                    col_pos = REAL_DATA_SIZE*col_iteration+col
                    row_pos = REAL_DATA_SIZE*row_iteration+row
                    node = Node(weight, col_pos, row_pos)
                    graph.SetFromCoords(col_pos,row_pos,node)
        f.close()

def ReadDataSimple(graph):
    f = open(INPUT_FILENAME, "r")
    for row in range(DATA_SIZE):
        line = f.readline()[:-1]
        for col, data in enumerate(line):
            node = Node(int(data), col, row)
            graph.SetFromCoords(col,row,node)
    f.close()

def CoordsToNum(x,y):
    return y*DATA_SIZE + x


def NumToCoords(n):
    y = int(n//DATA_SIZE)
    x = n%DATA_SIZE
    return x, y


def GetAdjacent(graph, node):
    arr = []
    col = node.X()
    row = node.Y()
    if 0 < row:
        arr.append(graph.GetFromCoords(col, row-1))
    if row < DATA_SIZE-1:
        arr.append(graph.GetFromCoords(col, row+1))
    if 0 < col:
        arr.append(graph.GetFromCoords(col-1, row))
    if col < DATA_SIZE-1:
        arr.append(graph.GetFromCoords(col+1, row))
    return arr


def PrintPath(graph, path):
    for index in path:
        print(NumToCoords(index), graph.GetFromIndex(index).Weight())#,end=",")
    print()


def CreatePath(n, prev):
    path = []
    while prev[n] != -1:
        path.append(n)
        n = prev[n]

    return path[::-1]


def heuristic(node):
    manhattan_distance = 2*DATA_SIZE - node.X() - node.Y()
    manhattan_distance = manhattan_distance * MANHATTAN_MULTIPLIER
    return manhattan_distance


def AStar(graph, start, end, h):
    Q = MinPriorityQueue()
    dist = [9999 for x in range(DATA_SIZE*DATA_SIZE)] # AKA G(n) score
    f_score = [9999 for x in range(DATA_SIZE*DATA_SIZE)]
    in_arr = [1 for x in range(DATA_SIZE*DATA_SIZE)]

    start_index = start.Index()
    
    dist[start_index] = 0
    f_score[start_index] = h(start)

    Q.addWithPriority(0, 0)

    while not Q.empty():
        index = Q.extractMin().num
        in_arr[index] = 0
        u = graph.GetFromIndex(index)

        if u == end:
            return dist[u.Index()]

        for v in GetAdjacent(graph, u):
            Vindex = v.Index()
            if in_arr[Vindex]:
                alt = dist[u.Index()] + v.Weight()
                if alt < dist[Vindex]:
                    dist[Vindex] = alt
                    f_score[Vindex] = alt + h(v)
                    Q.decreasePriority(Vindex, dist[Vindex])


def main():
    graph = Graph()
    ReadDataExpanded(graph)

    print("# data is read")

    start = graph.GetFromCoords(0,0)
    end = graph.GetFromCoords(-1,-1)

    start_time = time()
    weight = AStar(graph, start, end, heuristic)
    print("weight",weight)
    print("Time Taken:", time()-start_time)

main()

"""
def toyCase():
    Q = MinPriorityQueue()

    max = 20
    for x in range(20):
        Q.add(x, max)
    
    Q.addWithPriority(20, 19)
    a = Q.extractMin()
    a.print()

    Q.decreasePriority(10, 5)
    Q.decreasePriority(9, 4)
    Q.decreasePriority(19, 6)
    Q.decreasePriority(10, 7)
    print("##")
    Q.print()
    print("##")
    Q.extractMin().print()
    Q.extractMin().print()
    Q.extractMin().print()

toyCase()
"""


# CORRECT ANSWER - 2952
# A* with heap - 10.28 seconds
# Manhattan distance of 5 - runs just under 10 seconds
