
f = open("input.txt", "r")

totals = {"forward":0, "down":0, "up":0}
line = ""


line = f.readline().split(" ")


while line[0] != "0":
    line[1] = int(line[1][:-1])
    totals[line[0]] += line[1]
    line = f.readline().split(" ")


f.close()
forwardTotal = totals["forward"]
downTotal = totals["down"]-totals["up"]
print(forwardTotal, downTotal)
print(forwardTotal * downTotal)