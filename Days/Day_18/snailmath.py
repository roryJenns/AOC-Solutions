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
    return result

def add(first, second):
    addition_node = Node(first, second)
    reduce(addition_node)
    return addition_node


def reduce(snail_node):
    # if any pair can explode, do that then reset
    while explode(snail_node) or split(snail_node):
        pass


def explode(start_node):
    exploded = False
    queue = [start_node]

    # search for pairs of depth 4
    # 'general search'
    while len(queue) != 0:
        node = queue.pop(0)
        if type(node) != int:
            if node.depth < 4:
                # add to queue
                queue.insert(0, node.right)
                queue.insert(0, node.left)
            else:
                # flag and exit
                exploded = True
                break
    

    if exploded:
        left_add = node.left
        right_add = node.right

        # add left part of pair to left side
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
            if parent.isLeftNumber():
                parent.left += left_add
            else:
                next_left_node = parent.left
                while True:
                    if type(next_left_node) == int:
                        parent.right += left_add
                        break
                    parent = next_left_node
                    next_left_node = parent.right
        
        # add right part of pair to right side
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
            if parent.isRightNumber():
                parent.right += right_add
            else:
                next_right_node = parent.right
                while True:
                    if type(next_right_node) == int:
                        parent.left += right_add
                        break
                    parent = next_right_node
                    next_right_node = parent.left

        # replace node with 0
        set_zero = False
        parent = node.parent
        if not parent.isLeftNumber():
            if parent.left.depth >= 4:
                parent.left = 0
                set_zero = True
        
        if not set_zero and not parent.isRightNumber():
            if parent.right.depth >= 4:
                parent.right = 0
        
        return True
    else:
        return False
    

def split(start_node):
    split_flag = False
    queue = [start_node]

    direction = "left"
    value = -1

    # search for pairs of depth 4
    # 'general search'
    while len(queue) != 0:
        node = queue.pop(0)
        if type(node) != int:
            # add to queue
            queue.insert(0, node.right)
            queue.insert(0, node.left)
            if node.isLeftNumber() and node.left > 9:
                # flag and exit
                split_flag = True
                direction = "left"
                value = node.left
                break
            elif node.isRightNumber() and node.right > 9:
                split_flag = True
                direction = "right"
                value = node.right
                break
    if split_flag:
        branch_node = Node(int(value//2), int(value//2) + (value%2))
        branch_node.parent = node
        branch_node.depth = node.depth + 1
        if direction == "left":
            node.left = branch_node
        if direction == "right":
            node.right = branch_node

    return split_flag


def calculateMagnitude(result):
    pass

def DFS(node, foo, depth=1):
    if type(node) == int:   
        foo(node, depth)
    else:
        DFS(node.left, foo, depth+1)
        DFS(node.right, foo, depth+1)

def printDFS(node, depth=0):
    DFS(node, (lambda text1, text2: print(text1, text2, end=", ")))
    print()

def shortDFS(node, foo, depth=1):
    if node.isLeftNumber():   
        foo(node.left, depth)
    else:
        DFS(node.left, foo, depth+1)
        DFS(node.right, foo, depth+1)

def giveDepthDFS(node, depth=1):
    if type(node) != int:
        setDepth(node, depth)
        giveDepthDFS(node.left, depth+1)
        giveDepthDFS(node.right, depth+1)

def setDepth(node, depth):
    if type(node) != int:
        node.depth = depth
    

def main():
    numbers = readInput()
    printDFS(numbers[0])

    for number in numbers:
        reduce(number)
    printDFS(numbers[0])

    result = addNumbers(numbers)
    print("RESULT")
    printDFS(result)


    magnitude = calculateMagnitude(result)
    print("MAGNITUDE",magnitude)


main()