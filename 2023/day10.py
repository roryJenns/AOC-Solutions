N = 140

def pipe_id(x, y):
    return x + N*y

def id_to_coords(id: int):
    return id%N, id//N

class Pipe:
    def __init__(self, x,y,c):
        self.coords = x,y
        self.c = c
        self.x = x
        self.y = y
        self.n, self.e, self.s, self.w = self.directions()
    
    def directions(self):
        return {
            "|": (True, False, True, False),
            "-": (False, True, False, True),
            "L": (True, True, False, False),
            "J": (True, False, False, True),
            "7": (False, False, True, True),
            "F": (False, True, True, False),
            ".": (False, False, False, False),
            "S": (True, True, True, True),
        }[self.c]
    
    def get_pipe_id(self):
        return pipe_id(self.x, self.y)
    
    def move_options(self):
        ls = []
        if self.n:
            ls.append(pipe_id(self.x, self.y-1))
        if self.e:
            ls.append(pipe_id(self.x+1, self.y))
        if self.s:
            ls.append(pipe_id(self.x, self.y+1))
        if self.w:
            ls.append(pipe_id(self.x-1, self.y))
        
        return ls
    
    def safe_moves(self):
        if self.x == 0:
            self.w = False
        if self.x == N-1:
            self.e = False
        if self.y == 0:
            self.n = False
        if self.y == N-1:
            self.s = False


class PipeMap:
    def __init__(self, data):
        self.pipes = data
        self.start = self._find_start()
    
    def _find_start(self) -> int:
        for line in self.pipes:
            for pipe in line:
                if pipe.c == "S":
                    pipe: Pipe
                    pipe.safe_moves()
                    
                    return pipe.get_pipe_id()
        raise
    
    def get_start(self) -> int:
        return self._find_start() #self.start.get_pipe_id()
    
    def pipe_by_id(self, id) -> Pipe:
        x, y = id_to_coords(id)
        return self.pipes[y][x]

    def steps(self, come:int) -> list:
        tos = self.pipe_by_id(come).move_options()
        res = [tos for tos in tos if come in self.pipe_by_id(tos).move_options()]
        return res
    
    def next_step(self, prev:int, curr:int) -> int:
        a, b = self.steps(curr)
        if a != prev:
            return a
        if b != prev:
            return b
    
    def print(self):
        for line in self.pipes:
            for pipe in line:
                print(pipe.c, end="")
            print()


def make_pipe(y):
    def inner_make_pipe(group):
        x, c = group
        return Pipe(x,y,c)
    return inner_make_pipe

def parse(group):
    i, line = group
    pipes = list(map(make_pipe(i), enumerate(line[:-1])))
    return pipes


with open("input_day10.txt","r") as f:
    pipe_map = PipeMap(list(map(parse, enumerate(f.readlines()))))

start:int = pipe_map.get_start()
steps:int = 1
prev:int = start
curr:int = start

loop_path = [['.' for _ in range(N)] for _ in range(N)]
x, y = id_to_coords(start)
loop_path[y][x] = '#'
while (next := pipe_map.next_step(prev, curr)) != start:
    steps += 1
    prev = curr
    curr = next
    x, y = id_to_coords(curr)
    loop_path[y][x] = '#'

print("Part 1:", steps //2)

with open("out_day10.txt", "w+") as f:
    f.write("\n".join(map(lambda x:"".join(x), loop_path)))


