from bdb import Breakpoint
from numpy import number


class Node():
    def __init__(self, left=-1, right=-1):
        self.left = left
        self.right = right
        self.parent = -1
        self.depth = -1

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

    for number in numbers_to_add:
        giveDepthDFS(number)

    return numbers_to_add
        

def constructSnailNumber(string):
    depth=0

    left, right = splitString(string)

    SN_node = Node()

    if len(left) == 1:
        left = int(left)
    else:
        left = constructSnailNumber(left)
        left.parent = SN_node

    if len(right) == 1:
        right = int(right)
    else:
        right = constructSnailNumber(right)
        right.parent = SN_node

    SN_node.left = left
    SN_node.right = right

    return SN_node
    

def splitString(string):
    depth = 0

    index = 0
    char = string[index]

    while not (char == ',' and depth == 1) and index < len(string):
        
        if char == '[':
            depth += 1
        elif char == ']':
            depth -= 1

        index += 1
        char = string[index]
    
    left = string[1:index]
    right = string[index+1:-1]
    
    return left, right
    
def addNumbers(numbers):
    result = numbers[0]
    for i in range(1, len(numbers)):
        result = add(result, numbers[i])

def add(first, second):
    addition_node = Node(first, second)
    reduce(addition_node)
    return addition_node


def reduce(snail_node):
    while explode(snail_node) or split(snail_node):
        pass

def explode(start_node):
    exploded = False
    queue = [start_node]

    while len(queue) != 0:
        node = queue.pop(0)
        if node.depth < 4:
            queue.insert(0, node.right)
            queue.insert(0, node.left)
        else:
            exploded = True
            break
    
    if exploded:
        left_add = node.left
        right_add = node.right

        none = False
        previous = node
        parent = node.parent
        while parent.left == previous:
            if parent.depth == 1:
                none = True
                break
            previous = parent
            parent = parent.parent
        
        if not none:
            next_left_node = parent.left
            while True:
                if next_left_node.isRightNumber():
                    next_left_node.right += left_add
                    break
        
        none = False
        previous = node
        parent = node.parent
        while parent.right == previous:
            if parent.depth == 1:
                none = True
                break
            previous = parent
            parent = parent.parent
        
        if not none:
            next_right_node = parent.right
            while True:
                if next_right_node.isLeftNumber():
                    next_right_node.left += right_add
                    break

    
    

def split(node):
    pass


def calculateMagnitude(result):
    pass

def DFS(node, foo, depth=1):
    if type(node) == int:   
        foo(node, depth)
    else:
        DFS(node.left, foo, depth+1)
        DFS(node.right, foo, depth+1)

def printDFS(node, depth=0):
    DFS(node, print)

def shortDFS(node, foo, depth=1):
    if node.isLeftNumber():   
        foo(node.left, depth)
    else:
        DFS(node.left, foo, depth+1)
        DFS(node.right, foo, depth+1)

def giveDepthDFS(node, depth=1):
    DFS(node, (lambda node, depth: setValue(node.depth, depth)))

def setValue(a,b):
    a = b



def main():
    numbers = readInput()

    printDFS(numbers[0])


    result = addNumbers(numbers)
    print(result)


    magnitude = calculateMagnitude(result)
    print(magnitude)


main()