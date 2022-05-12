from node import Node

class Graph():
    def __init__(self):
        self.nodes = []
    
    def AddNode(self, name):
        self.nodes.append(Node(name))
    
    def RemoveNode(self, name):
        inside = self.InGraph(name)
        if inside:
            self.nodes.remove(inside)

    def InGraph(self, name):
        for node in self.nodes:
            if node.name == name:
                return node
        return False

    def FindNode(self, name):
        for node in self.nodes:
            if node.name == name:
                return node
        return 0
    
    def AddEdge(self, from_name, to_name):
        fromN = self.FindNode(from_name)
        if not fromN:
            self.AddNode(from_name)
            fromN = self.FindNode(from_name)

        toN = self.FindNode(to_name)
        if not toN:
            self.AddNode(to_name)
            toN = self.FindNode(to_name)

        fromN.AddEdge(toN)
        toN.AddEdge(fromN)
        
    
    def Print(self):
        for node in self.nodes:
            print(node.name, end=" ")
            node.PrintEdges()

    def PrintNodes(self):
        for node in self.nodes:
            print(node.name)
