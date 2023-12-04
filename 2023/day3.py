def parse(line):
    return '.'+line[:-1]+'.'

with open("input"+"_day3.txt") as f:
    data = list(map(parse, f.readlines()))

n, m = len(data[0]), len(data)
visited = [[False for _ in range(n)] for _ in range(m)]


class Tool:
    def __init__(self, x,y,val, char, gears):
        self.coords = (x,y)
        self.val = val
        self.chars = [c for c in char]
        self.gears = [g for g in gears]
        self.gear = len(gears) > 0
    
    def __str__(self):
        return f"Tool at {self.coords[0]}, {self.coords[1]}, with {self.val}, {self.chars}"
    


def get_number(x,y) -> Tool:
    number = []
    endx = None
    for i in range(x,n):
        if '0' <= (c := data[y][i]) <= '9':
            number.append(c)
            visited[y][i] = True
        else:
            endx = i
            break
    if endx == None:
        endx = n
    value = int("".join(number))

    parts = []
    gears = []
    for j in range(max(0, y-1), min(m, y+1+1)):
        for i in range(max(0, x-1), min(n, endx+1)):
            c = data[j][i]
            if c != '.' and not ('0' <= c <= '9'):
                parts.append(c)
            if c == "*":
                gears.append((i,j))

    return Tool(x, y, value, parts, gears)

tools = []
for j in range(m):
    for i in range(n):
        if visited[j][i]:
            continue
        if '0' <= data[j][i] <= '9':
            tools.append(get_number(i,j))

total = 0
for tool in tools:
    if len(tool.chars) > 0:
        total += tool.val
print("Part 1:", total)

gear_tools = filter(lambda x : x.gear, tools)
gear_list = {}
for gt in gear_tools:
    for gear in gt.gears:
        if gear not in gear_list:
            gear_list[gear] = []
        gear_list[gear].append(gt)

from numpy import prod
total2 = 0
for gear_group in gear_list.values():
    if len(gear_group) == 2:
        total2 += prod(list(map(lambda x: x.val, gear_group)))

print("Part 2:", total2)




