DAY_NUMBER = 1
TEST_INPUT = "test_input.txt"
REAL_INPUT = "input.txt"
INPUT_FILENAME = TEST_INPUT
INPUT_FILENAME = REAL_INPUT

def readData(filename):
    file = "input/"+filename
    with open(file, "r") as f:
        data = list(map(lambda x : x[:-1], f.readlines()))
    return data

def processData():
    raw = readData(INPUT_FILENAME)
    return raw


def main():
    data = processData()
    
    print(data)

    print("PART 1:","N/A")
    print("PART 2:","N/A")

main()