class BinaryTree:
    def __init__(self):
        self.root = None
    
    def addNode(self, val):
        if self.root == None:
            self.root = Node(val)
        pass

    def defaultTree(self):
        self.root = Node(5, Node(2, Node(1, Node(0), None), Node(3, None, Node(4))), Node(7, Node(6), Node(8)))
    
    def printInOrder(self):
        self.funcInOrder(lambda node : print(node.val))

    def sumTree(self):
        self.x = 0
        def addX(self, v):
            self.x += v
        self.funcInOrder(lambda node : addX(self, node.val))
        print(self.x)
    
    def funcInOrder(self, foo):
        def helper(node:Node, depth:int = 0):
            if node == None:
                return
            helper(node.left, depth + 1)
            foo(node)
            helper(node.right, depth + 1)
        helper(self.root)


class Node:
    def __init__(self, val=0, l=None, r=None):
        self.val = val
        self.left = l
        self.right = r
    
    def addLeft(self, val):
        self.left = Node(val)
    
    def addRight(self, val):
        self.right = Node(val)
    

if __name__ == "__main__":
    b = BinaryTree()
    b.defaultTree()
    # b.printInOrder()
    b.sumTree()
