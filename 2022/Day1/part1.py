INPUT_FILENAME = "input.txt"

def readData():
    f = open(INPUT_FILENAME, "r")
    data = list(map(lambda x : x[:-1], f.readlines()))
    f.close()
    return data


def processData():
    raw = readData()

    per_elf = []
    temp = []
    for c in raw:
        if c == "":
            per_elf.append(temp)
            temp = []
        else:
            temp.append(int(c))

    per_elf.append(temp)
    return per_elf


def main():
    data = processData()

    sums = max(map(sum, data))
    
    print(sums)

main()