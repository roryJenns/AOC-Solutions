def parse(line):
    return line[:-1]

with open("input_day3.txt") as f:
    data = list(map(parse, f.readlines()))

n, m = len(data[0]), len(data)
visited = [[False for _ in range(n)] for _ in range(m)]


class Tool:
    def __init__(self, x,y,val, char):
        self.coords = (x,y)
        self.val = val
        self.chars = [c for c in char]
    
    def __str__(self):
        print(f"Tool at {self.coords[0]}, {self.coords[1]}, with {self.val}, {self.chars}")

def get_number(x,y) -> Tool:
    number = []
    endx = 0
    for i in range(x,n):
        if '0' <= (c := data[y][i]) <= '9':
            number.append(c)
            visited[y][i] = True
        else:
            endx = i
            break
    value = int("".join(number))

    parts = []
    for i in range(max(0, x-1), min(n, endx+1)):
        for j in range(max(0, y-1), min(m, y+1+1)):
            c = data[j][i]
            if c != '.' and not ('0' <= c <= '9'):
                parts.append(c)

    return Tool(x, y, value, parts)

tools = []
for j in range(m):
    for i in range(n):
        if visited[j][i]:
            continue
        if '0' <= data[j][i] <= '9':
            tools.append(get_number(i,j))

print([tool.__str__() for tool in tools])
total = 0
for tool in tools:
    if len(tool.chars) > 0:
        total += tool.val
print(total)

