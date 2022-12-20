import numpy as np
from time import time

import heapq


TEST_INPUT = "test_input.txt"
REAL_INPUT = "input.txt"
INPUT_FILENAME = TEST_INPUT
# INPUT_FILENAME = REAL_INPUT


def readData():
    file = "input/"+INPUT_FILENAME
    with open(file, "r") as f:
        data = list(map(lambda x : x[:-1], f.readlines()))
    return data

def listify(line, i=0):
    res = []
    while i < len(line):
        if line[i] == ']':
            return (res, i+1)

        elif line[i] == '[':
            l, i = listify(line, i+1)
            res.append(l)
            
        elif line[i] == ',':
            i+=1
        else:
            val = int(line[i])
            i += 1
            if line[i] == '1' and line[i+1] == '0':
                i += 1
                val = 10
            res.append(val)
    return res

def processData():
    data = readData()

    pairs = [(listify(data[i]), listify(data[i+1])) for i in range(0, len(data), 3)]

    # [print(x) for x in pairs]

    return pairs


ARBITRARILY_LARGE = 90
def compare(left, right,i=0, debug=False):
    if debug:
        print(i,"#",left,right)
    while True:
        if not len(left):
            return True
        if not len(right):
            return False

        l = left.pop(0)
        r = right.pop(0)

        if type(l) == int and type(r) == int:
            if l > r:
                return False
        
        if type(l) != int and type(r) == int:
            r = [r]# + [11 for _ in range(ARBITRARILY_LARGE)]
        if type(r) != int and type(l) == int:
            l = [l]
        
        if type(l) != int and type(r) != int:
            if not compare(l,r,i+1, debug):
                return False

    return True
            



def part1():
    DEBUG = False
    pairs = processData()
    count = [0,0]
    total = []
    for index, pair in enumerate(pairs):
        left, right = pair
        flag = compare(left,right, debug=DEBUG)
        print(flag)
        if flag:
            count[0] += 1
            total.append(index+1)
        else:
            count[1] += 1
    print(total)
    return sum(total)

def part2():
    return 0

def main():
    a = part1()
    print("1:",a)
    b = part2()
    print("2:",b)

main()





