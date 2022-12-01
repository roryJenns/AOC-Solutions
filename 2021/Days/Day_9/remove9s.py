INPUT_FILENAME = "mod_input.txt"
#OUTPUT_FILENAME = "mod_draw_area_num.txt"
OUTPUT_FILENAME = "mod_draw_borders_num.txt"

data = []
f = open(INPUT_FILENAME, "r")
for x in range(100):
    data.append(f.readline()[:-1])
f.close()

counter = 0
f = open(OUTPUT_FILENAME, "w+")
for line in data:
    counter = 0
    for char in line:
        if char == "9":
        #if char != "9":
            counter = 0
            f.write("#")
        else:
            counter += 1
            f.write("{}".format(counter%10))
            #f.write(".")
    f.write("\n")
f.close()