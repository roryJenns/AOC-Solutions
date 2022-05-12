# This program is to get an upper bound 
# for the size of the (simple) graph, 
# to reduce 'dumb' searching when the cost is 
# already above the lowest.
# Running it finds that there is a path
# with a cost of {1204}

from node import Node

DATA_SIZE = 100
INPUT_FILENAME = "input.txt"

def ReadData():
    global graph
    graph = [[0 for x in range(DATA_SIZE)] for y in range(DATA_SIZE)]
    f = open(INPUT_FILENAME, "r")
    for row in range(DATA_SIZE):
        line = f.readline()[:-1]
        for col, data in enumerate(line):
            graph[row][col] = Node(int(data), col, row)
    f.close()


def GetAdjacent(node):
    arr = []
    row = node.GetRow()
    col = node.GetCol()
    if 0 < row:
        arr.append(graph[row-1][col])
    if row < DATA_SIZE-1:
        arr.append(graph[row+1][col])
    if 0 < col:
        arr.append(graph[row][col-1])
    if col < DATA_SIZE-1:
        arr.append(graph[row][col+1])
    return arr


def main():
    ReadData()

    global graph
    total = 0
    for node in graph[0]:
        total += node.GetWeight()
    for index in range(DATA_SIZE):
        total += graph[index][-1].GetWeight()
    print(total)

graph = []
main()