from time import time


INPUT_FILENAME = "input.txt"
REAL_DATA_SIZE = 100 # Test data - 10, Real data - 100

DATA_SIZE_MULTIPLIER = 5
DATA_SIZE = DATA_SIZE_MULTIPLIER*REAL_DATA_SIZE  

# Don't want to overestimate, try at different values [1-9]
MANHATTAN_MULTIPLIER = 3


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


class Queue():
    def __init__(self):
        self.dontVisit = []
        self.unvisited = []
    
    def arr(self):
        return self.unvisited
    
    def searchUnvisited(self):
        return self.unvisited
    
    def maxVals(self):
        return self.dontVisit

    def append(self, n):
        self.dontVisit.append(n)

    def valueInQ(self, n):
        return (n in self.unvisited) or (n in self.dontVisit)
    
    def remove(self, n):
        self.unvisited.remove(n)
    
    def empty(self):
        return len(self.unvisited) + len(self.dontVisit) == 0
    
    def notMax(self, n):
        self.dontVisit.remove(n)
        self.unvisited.append(n)


def ReadData(graph):
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


def dijkstraPath(graph, start, end):
    Q = Queue()
    dist = [9999 for x in range(DATA_SIZE*DATA_SIZE)]
    prev = [-1 for x in range(DATA_SIZE*DATA_SIZE)]

    for line in graph.GetArr():
        for node in line:
            Q.append(node.Index())
    
    dist[start.Index()] = 0
    # print("dist",dist)
    # print("Q",Q.arr)

    while not Q.empty():
        min = 9999
        for index in Q.arr:
            if dist[index] < min:
                min = dist[index]
                u = graph.GetFromIndex(index)

        Q.remove(u.Index())
        

        if u == end:
            print("FOUND END")
            path = CreatePath(u.Index(), prev)
            return dist[u.Index()], path

        for v in GetAdjacent(graph, u):
            if Q.valueInQ(v.Index()):
                alt = dist[u.Index()] + v.Weight()
                if alt < dist[v.Index()]:
                    dist[v.Index()] = alt
                    prev[v.Index()] = u.Index()


def dijkstra(graph, start, end):
    Q = Queue()
    dist = [9999 for x in range(DATA_SIZE*DATA_SIZE)]

    for line in graph.GetArr():
        for node in line:
            Q.append(node.Index())
    
    dist[start.Index()] = 0

    while not Q.empty():
        min = 9999
        for index in Q.arr:
            if dist[index] < min:
                min = dist[index]
                u = graph.GetFromIndex(index)

        Q.remove(u.Index())

        if u == end:
            return dist[u.Index()]

        for v in GetAdjacent(graph, u):
            if Q.valueInQ(v.Index()):
                alt = dist[u.Index()] + v.Weight()
                if alt < dist[v.Index()]:
                    dist[v.Index()] = alt


def heuristic(node):
    manhattan_distance = 2*DATA_SIZE - node.X() - node.Y()
    manhattan_distance = manhattan_distance * MANHATTAN_MULTIPLIER
    return manhattan_distance


def AStar(graph, start, end, h):
    Q = Queue()
    dist = [9999 for x in range(DATA_SIZE*DATA_SIZE)] # AKA G(n) score
    f_score = [9999 for x in range(DATA_SIZE*DATA_SIZE)]


    for line in graph.GetArr():
        for node in line:
            Q.append(node.Index())
    
    Q.notMax(0)
    
    dist[start.Index()] = 0
    f_score[start.Index()] = h(start)

    while not Q.empty():
        min = 9999
        for index in Q.searchUnvisited():
            if f_score[index] < min:
                min = f_score[index]
                u = graph.GetFromIndex(index)

        Q.remove(u.Index())

        if u.X()%10 == 0 and u.Y()%10 == 0:
            print([u.X(), u.Y()], u.Weight())

        if u == end:
            return dist[u.Index()]

        for v in GetAdjacent(graph, u):
            Vindex = v.Index()
            if Q.valueInQ(Vindex):
                alt = dist[u.Index()] + v.Weight()
                if alt < dist[Vindex]:
                    if dist[Vindex] == 9999:
                        Q.notMax(Vindex)
                    dist[Vindex] = alt
                    f_score[Vindex] = alt + h(node)

def main():
    graph = Graph()
    ReadData(graph)

    print("# data is read")

    start = graph.GetFromCoords(0,0)
    end = graph.GetFromCoords(-1,-1)

    weight = AStar(graph, start, end, heuristic)
    print("weight",weight)

main()


# RESULTS - 2952
# A* with unsorted Q took 15 minutes to run, 
