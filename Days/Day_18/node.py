class Node():
    def __init__(self, left=-1, right=-1):
        self.left = left
        self.right = right
        self.parent = -1
        self.depth = 0
        self.magnitude = 0

    def isLeftNumber(self):
        return type(self.left)==int
    def isRightNumber(self):
        return type(self.right)==int
    
    def setParent(self, node_parent):
        self.depth = node_parent.depth + 1
        self.parent = node_parent

    def calcMagnitude(self):
        if self.isLeftNumber():
            leftMag = self.left
        else:
            leftMag = self.left.calcMagnitude()

        if self.isRightNumber():
            rightMag = self.right
        else:
            rightMag = self.right.calcMagnitude()

        return 3*leftMag + 2*rightMag