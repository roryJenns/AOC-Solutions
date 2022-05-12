from importlib.resources import path
from graph import Graph
from queue import Stack

INPUT_FILENAME = "test_input_1.txt"
OUTPUT_FILENAME = "alex_read.txt"

def ReadDataToGraph(graph):
    f = open(INPUT_FILENAME, "r")
    line = f.readline()
    while line:
        pair = line[:-1].split('-')
        graph.AddEdge(pair[0],pair[1])
        line = f.readline()
    f.close()

def WriteToOutputFile(string):
    global fw
    fw.write(string)

def DepthFirstSearch(queue, node):
    queue.Push(node)
    if node.name == "end":
        WriteToOutputFile(queue.PrintString())
        queue.Delete()
        global path_count
        path_count += 1
        return
    adjacentVertices = node.GetEdges()
    for nextVertex in adjacentVertices:
        if not queue.Visited(nextVertex):
            newQueue = queue.Duplicate()
            DepthFirstSearch(newQueue, nextVertex)


def main():
    graph = Graph()
    graph.AddNode("start")
    graph.AddNode("end")

    ReadDataToGraph(graph)

    # print("Graph")
    # graph.Print()
    # print()

    ## Now we have a full graph
    ## Do pathfinding to find all routes

    queue = Stack()
    start = graph.FindNode("start")
    # print("Paths")
    DepthFirstSearch(queue, start)

    print(path_count)

path_count = 0
fw = open(OUTPUT_FILENAME, "w+")
main()