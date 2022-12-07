class Tree:
    def __init__(self, name, parent):
        self.name = name
        self.size = 0
        self.children = {}
        self.parent = parent
    
    def addChild(self, file):
        self.children[file.name] = file
    
    def calcSize(self):
        self.size = sum(map(lambda x : x.calcSize(), self.children.values()))
        print(self.name, self.size)
        return self.size

    def calcSizeFoo(self, foo):
        if self.size == 0:
            self.size = sum(map(lambda x : x.calcSizeFoo(foo), self.children.values()))
        foo(self)
        return self.size


class Node:
    def __init__(self, size, name):
        self.size = size
        self.name = name
    
    def calcSize(self):
        return self.size

    def calcSizeFoo(self, foo):
        return self.calcSize()
    

# if __name__ == "__main__":
#     b = BinaryTree()
#     b.defaultTree()
#     # b.printInOrder()
#     b.sumTree()
