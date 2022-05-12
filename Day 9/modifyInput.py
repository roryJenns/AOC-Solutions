INPUT_FILENAME = "input.txt"
OUTPUT_FILENAME = "mod_input.txt"

DATA_WIDTH = 100

data = []
f = open(INPUT_FILENAME, "r")
for x in range(DATA_WIDTH):
    data.append(f.readline()[:-1])
f.close()

f = open(OUTPUT_FILENAME, "w+")
for x in range(102):
    f.write("9")
f.write("\n")
for line in data:
    f.write("9")
    for char in line:
        f.write("{}".format(char))
    f.write("9")
    f.write("\n")
for x in range(102):
    f.write("9")
f.write("\n")
f.close()