from time import time

INPUT_FILENAME = "input.txt"
DATA_SIZE = 100  # Test data - 10, Real data - 100

# Don't want to overestimate, try at different values [1-9]
MANHATTAN_MULTIPLIER = 10


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
        self.arr = []
    
    def arr(self):
        return self.arr

    def append(self, n):
        self.arr.append(n)

    def valueInQ(self, n):
        return (n in self.arr)
    
    def remove(self, n):
        self.arr.remove(n)
    
    def empty(self):
        return len(self.arr) == 0


def ReadData(graph):
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
            #dist[u.Index()] += u.Weight()
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
    
    dist[start.Index()] = 0
    f_score[start.Index()] = h(start)

    while not Q.empty():
        min = 9999
        for index in Q.arr:
            if f_score[index] < min:
                min = f_score[index]
                u = graph.GetFromIndex(index)

        Q.remove(u.Index())

        if u == end:
            return dist[u.Index()]

        for v in GetAdjacent(graph, u):
            if Q.valueInQ(v.Index()):
                alt = dist[u.Index()] + v.Weight()
                if alt < dist[v.Index()]:
                    dist[v.Index()] = alt
                    f_score[v.Index()] = alt + h(node)

def main():
    graph = Graph()
    ReadData(graph)

    print("# data is read")

    start = graph.GetFromCoords(0,0)
    end = graph.GetFromCoords(-1,-1)

    t = time()
    weight = dijkstra(graph, start, end)
    dtime = time()-t
    print("dijkstra search time",dtime)

    t = time()
    weight = AStar(graph, start, end, heuristic)
    
    astime = time()-t
    print("A* search time",astime)

    print(astime/dtime * 100)
    print("weight",weight)

main()


# RESULTS - dijkstra says 691, if add final weight 699
# AoC Says somewhere in between
