import math


def distance_reached(taken, total):
    return taken * max(0, total - taken)

def optimal_time(total):
    return int(total // 2)

def optimal_distance(total):
    return distance_reached(optimal_time(total), total)

def earliest_time(total, record):
    return math.ceil((total - math.sqrt(total*total - 4 * record)) / 2)

def latest_time(total, record):
    return math.floor((total + math.sqrt(total*total - 4 * record)) / 2)

def possible_times(total, record):
    return earliest_time(total, record), latest_time(total, record)

def number_better_times(total, record):
    start, end = possible_times(total, record)
    if start > end:
        return 0
    if start == end and distance_reached(start, total) == record:
        return 0
    if start == end:
        return 1
    return end - start + 1 - 1 * (distance_reached(start, total) == record) - 1 * (distance_reached(end, total) == record)

def parse_in(line):
    line.split(" ")

# Time:      7  15   30
# Distance:  9  40  200
# Time:        59     68     82     74
# Distance:   543   1020   1664   1022

test_data1 = [(7,9),(15,40),(30,200)]
input_data1 = [(59,543),(68,1020),(82,1664),(74,1022)]

test_data2 = (71530, 940200)
input_data2 = (59688274,543102016641022)

races = input_data1
total = 1
for time, record in races:
    total *= number_better_times(time, record)

print("Part 1:", total)

race = input_data2
print("Part 2:", number_better_times(race[0], race[1]))