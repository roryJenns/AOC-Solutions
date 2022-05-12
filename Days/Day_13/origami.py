INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"

def read_file():
    with open(INPUT_FILE, "r") as f:
        line = f.readline()[:-1]
        while line != "":
            pair = list(map(int,line.split(",")))
            coords.append(pair)
            line = f.readline()[:-1]
        line = f.readline()[:-1]
        while line != "":
            command_str = line.split(" ")[-1]
            command = (command_str[0], int(command_str[2:]))
            commands.append(command)
            line = f.readline()[:-1]
    coords.sort()

def remove_duplicates():
    remove_indices = []
    for index, coord in enumerate(coords[:-1]):
        if coord == coords[index+1]:
            remove_indices.append(index)
    
    # remove repeats from back to front
    remove_indices.sort(reverse=True)
    for index in remove_indices:
        coords.pop(index)

def remove_negatives():
    remove_indices = []
    for index, coord in enumerate(coords):
        if coord[0] < 0 or coord[1] < 0:
            remove_indices.append(index)
    
    # remove repeats from back to front
    remove_indices.sort(reverse=True)
    for index in remove_indices:
        coords.pop(index)

def fold_point(fold, value):
    if value < fold:
        return value
    elif value == fold:
        return -1

    distance_above_fold = value - fold
    new_coord = fold - distance_above_fold

    return new_coord


def fold_coordinate(coord, command):
    if command[0] == "x":
        new_x = fold_point(command[1], coord[0])
        return [new_x, coord[1]]
    elif command[0] == "y":
        new_y = fold_point(command[1], coord[1])
        return [coord[0], new_y]


def fold(command):
    for i, coord in enumerate(coords):
        coords[i] = fold_coordinate(coord, command)


def coord_string(base_coords):
    string = ""
    coords = list(map(lambda pair: [pair[1],pair[0]], base_coords))
    x = 0
    y = 0
    i = 0
    while i < len(coords):
        if y < coords[i][1]:
            x = 0
            y += 1
            string = string + "\n"

        if coords[i] == [x,y]:
            string = string + "#"
            i += 1
        else:
            string = string + "."

        x += 1
    return string

def visualise(base_coords):
    print(coord_string(base_coords))

def write_to_file(base_coords):
    with open(OUTPUT_FILE, "w+") as f:
        f.write(coord_string(base_coords))

def main(simple=False):
    read_file()

    if simple:
        fold(commands[0])
        coords.sort()

        remove_duplicates()
        remove_negatives()
    elif not simple:
        for command in commands:
            fold(command)
            coords.sort()

            remove_duplicates()
            remove_negatives()
    visualise(coords)
    write_to_file(coords)
    print("There are",len(coords),"coordinates")
    
    

coords = []
commands = []

main()

## My runs say
# 1 fold - 618 'dots visible'
# all folds - 98 'dots visible'

## After all folds, it spells something out...
# lemme get this


"""
NOTES

"EFFICIENCY" (it's python lol)
 - command axis could be a boolean ig

READABILITY
 - make each command/coord an object of class to remove
    'index' notation, instead use '.' notation
    (would make it difficult to sort)
    ((maybe only do for command?))

"""