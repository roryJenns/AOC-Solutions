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

starts = [node for node in dmap if node[-1] == "A"]

loop_size = len(directions)
Nstarts = len(starts)

def find_loop_to_z(c):
    visits = []
    start, offset = -1, -1
    count = 0
    for _ in range(N*10000):
        c = step(c, directions[count % N])
        if c[-1] == "Z":
            if len(visits) > 0 and ((count - visits[0]) % loop_size) == 0:
                start = visits[0]
                offset = count - visits[0]
                visits.append(count)
                break
            visits.append(count)
            
        # step_all(currents, directions[count % N])
        
        count += 1
    print(c, start, offset)
    visit_diffs = [visits[i+1] - visits[i] for i in range(len(visits)-1)]
    return start, visit_diffs


class Hold:
    def __init__(self,start,diffs,i=0):
        self.current = start
        self.diffs = diffs
        self.i = i
        self.n = len(self.diffs)
    
    def __eq__(self, other):
        return self.current == other.current
    
    def __lt__(self, other):
        return self.current < other.current
    
    def __str__(self):
        return str(self.current)
    
    def __repr__(self):
        return self.__str__()

    def inc(self):
        self.i = (self.i + 1) % self.n

    def step(self):
        self.current += self.diffs[self.i]
        self.inc()
    
    def step_to(self, val):
        while self.current < val:
            self.step()

def equal(it):
    v = it[0].current
    for x in it:
        if x.current != v:
            return False
    return True


# def find_lcm_with_offset(a,b):
#     a_c = a[0]
#     for i in range(100000):
#         b_c = b[0]
#         for j in range(100000):
#             if a_c == b_c:
#                 print(i,j,b_c)
#                 return b_c
#             b_c += b[1]
#         a_c += a[1]

def gcd(a,b):
    c,d = max(a,b), min(a,b)
    if d == 0:
        return c
    return gcd(d, c % d)

def find_lcm(a,b):
    return a * (b / gcd(a,b))

def find_shared_lcm(values):
    while len(values) >= 2:
        print(values)
        values.append(find_lcm(values.pop(0), values.pop(0)))
    return values[0]



loop_info = []
for c in starts:
    loop_info.append(find_loop_to_z(c))

print(f"{find_shared_lcm([x[0] for x in loop_info]):.30f}")
exit()
# offset_lcms = [find_lcm_with_offset(a,b) for a,b in zip(loop_info[::2], loop_info[1::2])]
# out = find_shared_lcm(offset_lcms)
# print("Part 2:", count)
currents = [Hold(v[0], v[1]) for v in loop_info]
i = 0
for current in currents:
    current.step_to(100000000000)
while not equal(currents):
    m = max(currents).current
    for v in currents:
        v.step_to(m)
    i += 1
    if i % 100000 == 0:
        i=0
        print(currents, max(currents).current - min(currents).current)

for c in currents:
    print(c.current)
