
import sys
 
# setting path
sys.path.append('')

from helper.fileHander import readData

DAY_NUMBER = 1
TEST_INPUT = "DAY"+str(DAY_NUMBER)+"_test_input.txt"
REAL_INPUT = "DAY"+str(DAY_NUMBER)+"_input.txt"
INPUT_FILENAME = TEST_INPUT


def processData():
    raw = readData(INPUT_FILENAME)
    return raw


def main():
    data = processData()
    
    print(data)

    print("PART 1:","N/A")
    print("PART 2:","N/A")
    pass

main()