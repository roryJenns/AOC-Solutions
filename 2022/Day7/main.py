import numpy as np

from tree import Tree, Node

TEST_INPUT = "test_input.txt"
REAL_INPUT = "input.txt"
# INPUT_FILENAME = TEST_INPUT
INPUT_FILENAME = REAL_INPUT


def readData():
    file = "input/"+INPUT_FILENAME
    with open(file, "r") as f:
        data = list(map(lambda x : x[:-1], f.readlines()))
    return data


def processData1():
    raw = readData()

    group = []
    data = []

    for line in raw:
        line = line.split(" ")
        if line[0] == "$":
            data.append(group)
            group = [line,[]]
        else:
            group[1].append(line)

    data.append(group)
    
    data.pop(0)


    # make a tree
    root = Tree("/", None)
    curr = root

    for command, output in data:
        commandType = command[1]
        if commandType == "cd":
            moveTo = command[2]
            if moveTo == "/":
                curr = root
            elif moveTo == "..":
                curr = curr.parent
            else:
                if moveTo not in curr.children:
                    dir = Tree(moveTo, curr)
                    curr.addChild(dir)
                    pass
                curr = curr.children[moveTo]
        elif commandType == "ls":
            for line in output:
                name = line[1]
                if line[0] == "dir":
                    file = Tree(name, curr)
                else:
                    size = line[0]
                    file = Node(int(size), name)
                curr.addChild(file)

    return root

def sumTree(self):
    self.x = 0
    def addX(self, v):
        self.x += v
    self.funcInOrder(lambda node : addX(self, node.val))
    print(self.x)

def funcInOrder(root, foo):
    def helper(file):
        if file == None:
            return
        if type(file) == type(Node):
            foo(child)
        if type(file) == type(Tree):
            for child in file.children:
                helper(child)
            
    helper(root)

def part1():
    root = processData1()

    arr = []
    def foo(dir):
        arr.append((dir.name, dir.size))
    root.calcSizeFoo(foo)

    total = 0
    for dir in arr:
        size = dir[1]
        if size <= 100000:
            total += size

    return total

def part2():
    root = processData1()

    arr = []
    def foo(dir):
        # arr.append((dir.name, dir.size))
        arr.append(dir.size)
    root.calcSizeFoo(foo)

    arr = sorted(arr, reverse=True)
    
    diskspace = 70000000
    free_required = 30000000

    taken = arr[0]
    free = diskspace-taken

    new_space = free_required - free

    prev = taken
    for size in arr:
        if size < new_space:
            return prev
        prev = size

    return 0

def main():
    total = part1()
    print("PART 1:",total)

    total2 = part2()
    print("PART 2:",total2)

main()