test_data = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)""".split("\n")

with open("input_day8.txt") as f:
    input_data = list(map(lambda x : x[:-1], f.readlines()))

class Node:
    def __init__(self, name, left, right):
        self.name = name
        self.left = left
        self.right = right


def get_data():
    x = input_data
    directions = x[0]
    dmap = {}
    nodes = x[2:]
    for node, _ , l, r in map(lambda x: tuple(x.split(" ")), nodes):
        dmap[node] = Node(node, l[1:-1], r[:-1])

    return directions, dmap

directions, dmap = get_data()
N = len(directions)

def stepL(current):
    return dmap[current].left

def stepR(current):
    return dmap[current].right

def step(current, direction):
    if direction == "L":
        return dmap[current].left
    return dmap[current].right

def step_all(As, direction):
    for i, a in enumerate(As):
        As[i] = step(a, direction)

current = "AAA"
count = 0
while current != "ZZZ":
    current = step(current, directions[count % N])
    count += 1
print("Part 1:", count)


def endz(currents):
    return all(map(lambda x: x[-1] == "Z", currents))

# def how_many(start, directions):
#     current = start
#     visited = {current:[0]}
#     repeated
#     for i in range(len(directions) * 100):
#         current = step(current, directions[i % N])
#         if current not in visited:
#             visited[current]
#             break

#     return 
    
currents = [node for node in dmap if node[-1] == "A"]

Nstarts = len(currents)
count = 0
# while not endz(currents):
for j in range(N*10000):
    step_all(currents, directions[count % N])
    for i, node in enumerate(currents):
        if node[-1] == "Z":
            print(i, node, count)
    count += 1
print("Part 2:", count)
