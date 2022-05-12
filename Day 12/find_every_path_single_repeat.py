from importlib.resources import path
from graph import Graph
from queue import Stack

INPUT_FILENAME = "input.txt"
OUTPUT_FILENAME = "output2.txt"

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

def DepthFirstSearch(queue, node, canRevisit):
    queue.Push(node)
    if node.name == "end":
        queue.Print()
        WriteToOutputFile(queue.PrintString())
        queue.Delete()
        global path_count
        path_count += 1
        return
    adjacentVertices = node.GetEdges()
    for nextVertex in adjacentVertices:
        if not queue.Visited(nextVertex):
            newQueue = queue.Duplicate()
            DepthFirstSearch(newQueue, nextVertex, canRevisit)
        elif canRevisit and (nextVertex.name != "start"):
                newQueue = queue.Duplicate()
                DepthFirstSearch(newQueue, nextVertex, False)


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
    DepthFirstSearch(queue, start, True)

    print(path_count)

path_count = 0
fw = open(OUTPUT_FILENAME, "w+")
main()