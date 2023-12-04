def parse_input(line):
    try:
        parts = list(filter(lambda x : x != '', line[:-1].split(" ")))
        id = parts[1][:-1]
        winners = tuple(map(int, parts[2:2+10]))
        numbers = tuple(map(int, parts[2+11:]))
    except Exception as e:
        print(line)
        raise e
    return (id, winners, numbers)

with open("input_day4.txt") as f:
    data = list(map(parse_input, f.readlines()))

total = 0
for id, winners, numbers in data:
    count = 0
    for numb in numbers:
        if numb in winners:
            count += 1
    if count > 0:
        total += 1 << (count - 1)

print("part 1:", total)

mem = [1 for _ in range(200)]
mem[0] = 0
for card in range(1, 200):
    id, winners, numbers = data[card-1]
    
    win_count = len(list(filter(lambda x : x in winners, numbers)))
    for i in range(win_count):
        mem[card+1+i] += mem[card]

print("Part 2:",sum(mem))