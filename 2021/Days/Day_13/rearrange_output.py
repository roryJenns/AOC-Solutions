IN = "output_clean.txt"
OUT = "secret_code.txt"


with open(IN, "r") as f:
    data = list(map(lambda a: a[:-1], f.readlines()))

string = ""

print(data)
height = len(data[0])
width = len(data)

for i in range(height):
    for j in range(width):
        char = data[j][i]
        if char == ".":
            char = " "
        string = string + char
    string += "\n"

print(string)
with open(OUT, "w+") as f:
    f.write(string)

# ALREKFKU ????