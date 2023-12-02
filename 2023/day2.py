
R = 0
G = 1
B = 2

def parse_input(line):
    parts = line.split(" ")
    id = int(parts[1][:-1])
    r,g,b = 0,0,0
    # pulls = []
    # add=False
    for num, col in zip(parts[2::2], parts[3::2]):
        # if col[-1] == ';':
        #     add=True
        colour = col[:-1]
        number = int(num)

        if colour == "red":
            r=max(r,number)
        if colour == "green":
            g=max(g,number)
        if colour == "blue":
            b=max(b,number)
        
        # if add:
        #     pulls.append(r,g,b)
        #     r,g,b=0,0,0
        #     add=False

    return (id, r, g, b)


with open("input_day2.txt") as f:
    data = list(map(parse_input, f.readlines()))

# part 1
max_c = (12, 13, 14)

total = 0
for game, r, g, b in data:
    if r <= max_c[R] and g <= max_c[G] and b <= max_c[B]:
        total += game

# part 2
power = 0
for game, r, g, b in data:
    power += r*g*b

print("Part 1:", total)
print("Part 2:", power)