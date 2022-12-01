
INPUT_FILENAME = "input.txt"

NUMBER_OF_ITERATIONS = 40 # Part 1 - 10, Part 2 - 40

def ReadDataFromFile():
    global polymer, polymer_template, polymer_pair_count, zero_polymer_pair_count, zero_letter_count

    f = open(INPUT_FILENAME, "r")

    polymer = f.readline()[:-1]
    f.readline()

    line = f.readline()
    while line != "":
        pair, result = line[:-1].split(" -> ")
        polymer_template[pair] = result
        zero_polymer_pair_count[pair] = 0

        zero_letter_count[pair[0]] = 0
        zero_letter_count[pair[1]] = 0
        
        line = f.readline()

    f.close()

    print(len(polymer_template.items()))


def ConvertToPairCount():
    global polymer, polymer_template, polymer_pair_count

    polymer_pair_count = zero_polymer_pair_count.copy()

    for index in range(1, len(polymer)):
        pair = polymer[index-1:index+1]
        polymer_pair_count[pair] += 1


def IterateTest(polymer, polymer_template, polymer_pair_count): # there is no way this will be efficient enough
    new_polymer = polymer[0]

    monomer1 = ""
    monomer2 = ""

    for index in range(1, len(polymer)):
        monomer1 = polymer[index-1]
        monomer2 = polymer[index]

        new_polymer = new_polymer + polymer_template[monomer1+monomer2] + monomer2

    return new_polymer


def Iterate():
    global polymer_template, polymer_pair_count

    result = ""
    
    temp_polymer_pair_count = zero_polymer_pair_count.copy()

    for pair, count in polymer_pair_count.items():
        result = polymer_template[pair]
        start_mod_pair = pair[0] + result
        end_mod_pair = result + pair[1]

        temp_polymer_pair_count[start_mod_pair] += count
        temp_polymer_pair_count[end_mod_pair] += count

    polymer_pair_count = temp_polymer_pair_count.copy()

    return 


def PrintPairCount():
    global polymer_pair_count

    print("PRINT PAIR COUNTS")
    for pair, count in polymer_pair_count.items():
        print(pair, count)


def CalculateTotals():
    global polymer_pair_count

    letters = zero_letter_count.copy()

    for pair, count in polymer_pair_count.items():
        letters[pair[0]] += count
        letters[pair[1]] += count
    
    total = 0
    print("CALCULATE LETTER TOTALS")
    for letter, count in letters.items():
        true_count = -(-count//2) # ceiling division
        total += true_count
        print(letter, true_count) 
    print("Total:",total)


def CalculateResult():
    global polymer_pair_count

    letters = zero_letter_count.copy()

    for pair, count in polymer_pair_count.items():
        letters[pair[0]] += count
        letters[pair[1]] += count
    
    for letter, count in letters.items():
        letters[letter] =  -(-count//2) # ceiling division

    max_count = 0
    min_count = letters["N"]

    for letter, count in letters.items():
        max_count = max(count, max_count)
        min_count = min(count, min_count)

    print("MAX - MIN :", max_count - min_count)
    return max_count - min_count


def main():
    ReadDataFromFile()
    ConvertToPairCount()

    for iter_count in range(NUMBER_OF_ITERATIONS):
        Iterate()

    PrintPairCount()
    CalculateTotals()

    CalculateResult()

polymer = ""
polymer_template = {}

zero_polymer_pair_count = {}
polymer_pair_count = {}

zero_letter_count = {}

main()
