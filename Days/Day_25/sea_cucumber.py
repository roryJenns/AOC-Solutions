INPUT = "test_input.txt"


def setupGrid():
    char_to_num = {".":0, ">":1, "v":2}
    with open(INPUT, "r") as f:
        return [list(map(lambda a: char_to_num[a], list(line[:-1]))) for line in f.readlines()]

def iteration(grid):
    width = len(grid[0])
    height = len(grid)
    # East
    moved_prev = False
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            prev_index = x-1
            prev_square = grid[y][prev_index]
            
            if moved_prev:
                moved_prev = False
                continue

            if char == 0 and prev_square == 1:
                grid[y][x] = 1
                grid[y][prev_index] = 0
                moved_prev = True
    
    # South
    moved_prev = False
    for x in range(width):
        for y in range(height):
            char = grid[y][x]
            prev_index = y-1
            
            prev_square = grid[prev_index][x]

            if moved_prev:
                moved_prev = False
                continue

            if char == 0 and prev_square == 2:
                grid[y][x] = 2
                grid[prev_index][x] = 0
                moved_prev = True

def print_grid(grid):
    num_to_char = [".", ">", "v"]
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            print(num_to_char[char], end="")
        print()

def main():
    grid = setupGrid()

    # print_grid(grid)
    for x in range(58):
        iteration(grid)
        # print()
    print_grid(grid)
    

main()