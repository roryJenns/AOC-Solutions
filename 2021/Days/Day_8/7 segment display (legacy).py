INPUT_FILENAME = "input.txt"

def main():

    codes, output = ReadData()

    codes, transfer, fives, sixes = SortCodes(codes)

    wiring = {}
    temp = [transfer[7][i] for i in range(3)]

    # Find 'a' from 1 and 7
    # Find 'f' and 'c' from 1 with 0 and 6
    one = transfer[1]
    for i in range(2):
        temp.pop(temp.index(one[i]))
    wiring["a"] = temp[0]
    for i in range(3):
        val = sixes[i]
        a = one[0] in val
        b = one[1] in val
        if a and b:
            pass
        elif a:
            wiring["f"] = one[0]
            wiring["c"] = one[1]
        elif b:
            wiring["f"] = one[1]
            wiring["c"] = one[0]
    
    # eight = transfer[8]
    # zero = transfer[0]
    # for i in range(7):
    #     if not (eight[i] in zero):
    #         wiring["d"] = eight[i]
    #         break
    # for i in range(7):
    #     if not (transfer[4][i] in wiring):
    #         wiring["b"] = transfer[4][i]
    

    for i in range(4):
        output[i] = list(output[i])
        output[i].sort()
    
    one = [wiring["c"],wiring["f"]]
    one.sort()
    rewired = {1:one}
    totals = [x for x in range(10)]
    for out in output:
        if rewired[1] == out:
            totals[1] += 1
        elif rewired[7] == out:
            totals[7]
    
    
    print(wiring)
    #print(total_ones)
    print(transfer)
    print(rewired[1])
    print(output)


def ReadData():
    f = open(INPUT_FILENAME, "r")
    codes, output = f.readline().split("|")
    f.close()


    codes = codes.split(" ")[:-1]
    output = output.split(" ")[1:]
    output[-1] = output[-1][:-1]

    return codes, output


def SortCodes(codes):
    transfer = {}
    fives = []
    sixes = []
    for code in codes:
        length = len(code)
        x = list(code)
        if length == 2:
            transfer[1] = x
        elif length == 3:
            transfer[7] = x
        elif length == 4:
            transfer[4] = x
        elif length == 7:
            transfer[8] = x
        elif length == 6:
            sixes.append([i for i in x])
        elif length == 5:
            fives.append([i for i in x])
    return codes, transfer, fives, sixes


def PrintFinal(transfer, codes, output):
    print(transfer)
    print(codes)
    print(output)


main()