

TEST_INPUT = "test_input.txt"
REAL_INPUT = "input.txt"
# INPUT_FILENAME = TEST_INPUT
INPUT_FILENAME = REAL_INPUT


def readData(filename):
    file = "input/"+filename
    with open(file, "r") as f:
        data = list(map(lambda x : x[:-1], f.readlines()))
    return data


def processData1():
    data = readData(INPUT_FILENAME)
    elf_split = list(map(lambda x : x.split(","), data))
    elf_values = list(map(lambda pair : list(map(lambda x: x.split("-"), pair)), elf_split))
    int_elf = list(map(lambda l_2 : list(map(lambda l : list(map(int, l)), l_2)), elf_values))
    return int_elf


def part1():
    assignments = processData1()

    full_count = 0
    for left , right in assignments:
        if left[0] <= right[0] and left[1] >= right[1]:
            full_count += 1
        elif left[0] >= right[0] and left[1] <= right[1]:
            full_count += 1

    return full_count

def processData2():
    data = readData(INPUT_FILENAME)
    return data

def part2():
    assignments = processData1()

    part_count = 0
    for left, right in assignments:
        if max(left[0], right[0]) <= min(left[1], right[1]):
            part_count += 1

    return part_count

def main():
    total = part1()
    print("PART 1:",total)

    total2 = part2()
    print("PART 2:",total2)

main()

# C:\Users\roryj\OneDrive - The University of Nottingham\AOC-Solutions\2022\Day4\input
