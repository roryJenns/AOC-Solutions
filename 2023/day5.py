test_data = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""

input_data = test_data  # mod to main data

class MapRange:
    def __init__(self, t):
        destination, source, size = t
        self.size = size
        self.destination_start = destination
        self.destination_end = destination + size - 1
        self.source_start = source
        self.source_end = source + size - 1
        self.offset = destination - source
    
    def in_range(self, source):
        return self.source_start <= source <= self.source_end
    
    def get_destination(self, source):
        return source + self.offset
    
    def in_reverse_range(self, destination):
        return self.destination_start <= destination <= self.destination_end
    
    def get_source(self, destination):
        return destination - self.offset


class MapHere:
    def __init__(self):
        self.ranges: list[MapRange] = []
        self.name = "NONE"
    
    def add_range(self, range: MapRange):
        self.ranges.append(range)
    
    def append(self, range):
        self.add_range(range)
    
    def get_mapping(self, source):
        for maprange in self.ranges:
            if maprange.in_range(source):
                return maprange.get_destination(source)
        return source
    
    def get_reverse_mapping(self, destination):
        for maprange in self.ranges[::-1]:
            if maprange.in_reverse_range(destination):
                return maprange.get_source(destination)
        return destination


def parse(line):
    return line[:-1]


def push_through_maps(seed: int, printout=False):
    global sections
    maps = sections
    working = seed
    if printout:
        print("["+str(seed), end="")
    for map in maps:
        if printout:
            print(f".{working}", end="")
        working = map.get_mapping(working)
    if printout:
        print(f".{working}]")
    return working

def pull_through_maps(location: int):
    global sections
    maps = sections
    working = location
    for map in maps[::-1]:
        working = map.get_reverse_mapping(working)
    return working


lines = input_data.split("\n")

seeds = list(map(int, lines[0].split(" ")[1:]))
seeds2 = [range(int(a),int(a)+int(b)) for a, b in zip(lines[0].split(" ")[1::2],lines[0].split(" ")[2::2])]

sections = [MapHere() for _ in range(7)]
current = -1
for line in lines[1:]:
    if line == "":
        continue
    if not ('0' <= line[0] <= '9'):
        current += 1
        if current >= 7:
            break
        sections[current].name = line[:-5]
        continue
    sections[current].append(MapRange(tuple(map(int, line.split(" ")))))


# Part 1
locations = []
for seed in seeds:
    locations.append(push_through_maps(seed))

r1 = min(locations)
print("Part 1:", min(locations))

# # Iterate every option
# lowest_location, minseed = float('inf'), 0
# b = len(seeds2)
# for a, gen in enumerate(seeds2):
#     for seed in gen:
#         y = push_through_maps(seed)
#         if y < lowest_location:
#             lowest_location = y
#             minseed = seed
#     print(f"Completed {a+1} of {b} generators")

# push_through_maps(minseed, True)
# print("Part 2:", lowest_location, "-", minseed)

def seed_in_original(seed):
    for seed_range in seeds2:
        if seed in seed_range:
            return True
    return False

# Reverse from locations
minseed = 0
lowest_location = float('inf')
for location in range(10*r1):
    seed = pull_through_maps(location)
    if seed_in_original(seed):
        lowest_location = location
        minseed = seed
        break

print("Part 2:", lowest_location, "-", minseed)
