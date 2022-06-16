class Node():
    def __init__(self, left=-1, right=-1):
        self.left = left
        self.right = right
        self.parent = -1
        self.depth = 0

    def isLeftNumber(self):
        return type(self.left)==int
    def isRightNumber(self):
        return type(self.right)==int
    
    def setParent(self, node_parent):
        self.depth = node_parent.depth + 1
        self.parent = node_parent