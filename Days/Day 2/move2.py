
f = open("input.txt", "r")

totals = {"horizontal":0, "aim":0, "depth":0}
mapping = {"forward":"horizontal","down":"aim","up":"aim"}
line = ""

line = f.readline().split(" ")

while line[0] != "0":
    command = mapping[line[0]]
    magnitude = int(line[1][:-1])
    direction = 1

    if line[0] == "up":
        direction = -1
        
    totals[command] += magnitude * direction

    if command == "horizontal":
        totals["depth"] += magnitude * totals["aim"]

    line = f.readline().split(" ")


f.close()

print(totals["horizontal"], totals["depth"])
print(totals["horizontal"] * totals["depth"])