INPUT_FILENAME = "input.txt"
OUTPUT_FILENAME = "output.txt"

letters = {"a":1,"b":2,"c":4,"d":8,"e":16,"f":32,"g":64}
totals_counter = [0 for x in range(10)]

class Code():
    def __init__(self):
        self.letters = ""
        self.length = 0
        self.number = 0
        self.meaning = -1

    def SetLetters(self, letters):
        self.letters = letters
        self.SetCode()
        self.SetLength()
    
    def SetCode(self):
        for letter in self.letters:
            self.number += letters[letter]
    
    def SetLength(self):
        self.length = len(self.letters)


def bidict(d):
    d2 = d.copy()
    for k, v in d.items():
        # if v in d2.keys():
        #     raise KeyError(
        #         "Cannot create bidirectional dict."
        #         + "Either d has a value that is the same as one of "
        #         + "its keys or multiple keys have the same value."
        #     )
        d2[v] = k
    return d2

def ReadData():
    codes = f.readline().split(" ")

    codes.pop(10)
    codes[-1] = codes[-1][:-1]
    
    codes_arr = [Code() for x in range(14)]
    for i, code in enumerate(codes):
        codes_arr[i].SetLetters(code)
    
    return codes_arr[:10], codes_arr[10:]

# def PrintWiring():
#     print("  {0:2}  ".format(wiring[0]))
#     print("{:2}   {:2}".format(wiring[1], wiring[2]))
#     print("  {0:2}  ".format(wiring[3]))
#     print("{:2}   {:2}".format(wiring[4], wiring[5]))
#     print("  {0:2}  ".format(wiring[6]))

def main():
    wiring = [-1 for x in range(7)]

    ten_codes, outputs = ReadData()

    found_dict = {}
    
    fives = []
    sixes = []

    #print(ten_codes[0].number)

    for code in ten_codes:
        length = code.length
        if length == 5:
            fives.append(code)
        elif length == 6:
            sixes.append(code)
        elif length == 2:
            code.meaning = 1
            found_dict[1] = code.number
        elif length == 3:
            code.meaning = 7
            found_dict[7] = code.number
        elif length == 4:
            code.meaning = 4
            found_dict[4] = code.number
        elif length == 7:
            code.meaning = 8
            found_dict[8] = code.number

    
    wiring[0] = found_dict[1] ^ found_dict[7]
    for code in fives:
        if code.number & found_dict[7] == found_dict[7]:
            code.meaning = 3
            found_dict[3] = code.number
            break
    for code in sixes:
        if code.number & found_dict[1] != found_dict[1]:
            code.meaning = 6
            found_dict[6] = code.number
            sixes.remove(code)
            break
    
    wiring[2] = found_dict[6] ^ found_dict[8]
    wiring[5] = found_dict[1] ^ wiring[2]
    working = (found_dict[4] ^ found_dict[1])
    wiring[3] = found_dict[3] & working
    wiring[1] = wiring[3] ^ working
    
    sixes[0]
    if sixes[0].number & wiring[3] != 0:
        x = 0
    else:
        x = 1
    sixes[x].meaning = 9
    found_dict[9] = sixes[x].number
    sixes[x-1].meaning = 0
    found_dict[0] = sixes[x-1].number

    for code in fives:
        if code.meaning == -1:
            if code.number & wiring[1] != 0:
                code.meaning = 5
                found_dict[5] = code.number
            else:
                code.meaning = 2
                found_dict[2] = code.number

    #######################
    # Manage Output Stage #
    #######################

    results_dict = bidict(found_dict)

    for output in outputs:
        totals_counter[results_dict[output.number]] += 1

    #print(totals_counter)


## START ##
f = open(INPUT_FILENAME, "r")
for x in range(200):
    main()
f.close()
print(totals_counter)

print(totals_counter[1],totals_counter[4],totals_counter[7],totals_counter[8])
totals_sum1478 = totals_counter[1]+totals_counter[4]+totals_counter[7]+totals_counter[8]
print(totals_sum1478)

f = open(OUTPUT_FILENAME, "w+")
for x in range(len(totals_counter)):
    f.write("{} : {}\n".format(x, totals_counter[x]))
f.write("Total of 1, 4, 7, 8 : {}\n".format(totals_sum1478))
f.close()


## END ##