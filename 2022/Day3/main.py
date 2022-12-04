

TEST_INPUT = "test_input.txt"
REAL_INPUT = "input.txt"
# INPUT_FILENAME = TEST_INPUT
INPUT_FILENAME = REAL_INPUT


def readData(filename):
    file = "input/"+filename
    with open(file, "r") as f:
        data = list(map(lambda x : x[:-1], f.readlines()))
    return data


def getScore(c):
    value = ord(c)
    if 65 <= value <= 90:
        value -= 38 # 27 - 65
    else:
        value -= 96
    # print(c,ord(c),value) # Debug
    return value

def processData1():
    data = readData(INPUT_FILENAME)
    return list(map(lambda line: (line[:int(len(line)/2)], line[int(len(line)/2):]), data))


def part1():
    rucksacks = processData1()

    def containsDuplicate(comp1, comp2):
        hash = {}

        for element in comp1:
            if element in hash:
                hash[element] += 1
            hash[element] = 1
        
        for element in comp2:
            if element in hash:
                return element
    
        return -1

    score = 0
    for bag in rucksacks:
        element = containsDuplicate(bag[0],bag[1])
        score += getScore(element)
    return score

def processData2():
    data = readData(INPUT_FILENAME)
    lines = len(data)
    grouped_data = [(data[i],data[i+1],data[i+2]) for i in range(0, lines, 3)]
    return grouped_data


def part2():
    data = processData2()
    def containsDuplicate(comp1, comp2, comp3):
        hash = {}

        for element in comp1:
            if not element in hash:
                hash[element] = 1
        
        for element in comp2:
            if element in hash:
                hash[element] = 2
        
        for element in comp3:
            if element in hash:
                if hash[element] == 2:
                    return element
    
    score = 0
    for group in data:
        element = containsDuplicate(group[0],group[1],group[2])
        score += getScore(element)
    return score

def main():
    total = part1()
    print("PART 1:",total)

    total2 = part2()
    print("PART 2:",total2)

main()

# C:\Users\roryj\OneDrive - The University of Nottingham\AOC-Solutions\2022\Day2\input
