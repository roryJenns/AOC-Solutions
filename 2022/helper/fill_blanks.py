import fileHander as fh


FILE_IN = "../input/DAY1_input.txt"
FILE_OUT = "misc/haskell_day1_input.txt"

data = fh.readData(FILE_IN)
fh.writeData(FILE_OUT, data)
