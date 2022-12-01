class Node():
    def __init__(self, name):
        self.name = name
        self.type = NameType(name)
        self.edges = []
    
    def AddEdge(self, node):
        self.edges.append(node)
    
    def PrintEdges(self):
        for edge in self.edges:
            print(edge.name, end=" ")
        print()
    
    def Print(self):
        print(self.name, end=" ")
        self.PrintEdges()
    
    def isLarge(self):
        return self.type
    
    def isSmall(self):
        return not self.type
    
    def GetEdges(self):
        return self.edges
    
    def GetEdgeNames(self):
        arr = []
        for node in self.edges:
            arr.append(node.name)
        return arr


def NameType(name):
    if name < "a":
        return True
    else:
        return False