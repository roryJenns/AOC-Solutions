

TEST_INPUT = "test_input.txt"
REAL_INPUT = "input.txt"
# INPUT_FILENAME = TEST_INPUT
INPUT_FILENAME = REAL_INPUT


def readData(filename):
    file = "input/"+filename
    with open(file, "r") as f:
        data = list(map(lambda x : x[:-1], f.readlines()))
    return data

def processData():
    raw = readData(INPUT_FILENAME)

    abcrps = {"A":"rock","B":"paper","C":"scissors"}
    xyzrps = {"X":"rock","Y":"paper","Z":"scissors"}

    data = [(abcrps[round[0]], xyzrps[round[2]]) for round in raw]

    return data

def part1():
    data = processData()

    wins = {"rock":"paper","paper":"scissors","scissors":"rock"}
    scoring = {"rock":1,"paper":2,"scissors":3}

    total = 0
    for you, me in data:
        total += scoring[me]
        if you == me:
            total += 3
        if me == wins[you]:
            total +=  6

    return total

def processData2():
    raw = readData(INPUT_FILENAME)

    abcrps = {"A":"rock","B":"paper","C":"scissors"}
    xyzrps = {"X":"lose","Y":"draw","Z":"win"}

    data = [(abcrps[round[0]], xyzrps[round[2]]) for round in raw]

    return data

def part2():
    data = processData2()

    wins = {"rock":"paper","paper":"scissors","scissors":"rock"}
    ldw = {"lose":0,"draw":3,"win":6}
    scoring = {"rock":1,"paper":2,"scissors":3}

    total = 0
    for you, outcome in data:
        total += ldw[outcome]
        if outcome == "win":
            total += scoring[wins[you]]
        elif outcome == "draw":
            total += scoring[you]
        elif outcome == "lose":
            total += scoring[wins[wins[you]]]
    return total


def main():
    total = part1()
    total2 = part2()

    print("PART 1:",total)
    print("PART 2:",total2)

main()


# C:\Users\roryj\OneDrive - The University of Nottingham\AOC-Solutions\2022\Day2\input
