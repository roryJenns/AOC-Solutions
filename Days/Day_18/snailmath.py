class Node():
    def __init__(self):
        self.left = -1
        self.right = -1

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def setLeft(self, left):
        self.left = left
    def setRight(self, right):
        self.right = right

    def isLeftNumber(self):
        return type(self.left)==int
    def isRightNumber(self):
        return type(self.right)==int

INPUT = "test_input.txt"
OUTPUT = "test_output.txt"

def readInput():
    numbers_to_add = []
    with open(INPUT, "r") as f:
        data = list(map(lambda line: line[:-1],f.readlines()))
        numbers_to_add = list(map(constructSnailNumber, data))
        

def constructSnailNumber(string):
    depth=0

    left, right = splitString(string)

    SN_node = Node()
    SN_node.left = constructSnailNumber(left)
    SN_node.right = constructSnailNumber(right)

    return SN_node
    

def splitString(string):
    index = 0
    while not (char == ',' and depth == 1) and index < len(string):
        char = string[index]
        if char == '[':
            depth += 1
        elif char == ']':
            depth -= 1

        index += 1
    
    left = string[1:index]
    right = string[index+1:-1]

    if len(left) == 1:
        left = int(left)
    if len(right) == 1:
        right = int(right)
    
    return left, right
    

def main():
    readInput()


main()