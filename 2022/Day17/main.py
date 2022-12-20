"""####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##
"""

TEST_INPUT = "test_input.txt"
REAL_INPUT = "input.txt"
INPUT_FILENAME = TEST_INPUT
# INPUT_FILENAME = REAL_INPUT


def readData():
    file = "input/"+INPUT_FILENAME
    with open(file, "r") as f:
        data = list(map(lambda x : x[:-1], f.readlines()))
    return data


def processData():
    