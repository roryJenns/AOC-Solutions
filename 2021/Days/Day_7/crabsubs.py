OUTPUT_FILE = "output1.txt"

def CalculateFuelUsage(aim):
    global data
    total = 0
    for x in data:
        total += abs(x-aim)
    return total

f = open("input.txt","r")
data = f.readline().split(",")
data[-1] = data[-1][:-1]
f.close()

for x in range(len(data)):
    data[x] = int(data[x])

max_val = max(data)

f = open(OUTPUT_FILE, "w+")

min_fuel = CalculateFuelUsage(1)

f.write("{:4}:{}\n".format(1,min_fuel))

for x in range(2, max_val):
    val = CalculateFuelUsage(x)
    f.write("{:4}:{}\n".format(x, val))
    min_fuel = min(min_fuel, val)

f.write("Min Fuel : {}\n".format(min_fuel))
f.close()

print("Min Fuel :",min_fuel)