
import sys
 
# setting path
sys.path.append('')

from helper.fileHander import readData


TEST_INPUT = "DAYX_test_input.txt"
REAL_INPUT = "DAYX_input.txt"
INPUT_FILENAME = REAL_INPUT



def processData():
    raw = readData(INPUT_FILENAME)

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

    sums = sorted(list(map(sum, data)), reverse=True)
    top = sums[0]
    top_three = sums[0] + sums[1] + sums[2]

    print("PART 1 :",top)
    print("PART 2 :",top_three)

main()