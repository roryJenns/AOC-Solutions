
f = open("input.txt", "r")

line = f.readline()[:-1]
length = len(line)

print(length)

zeros_count = [0 for _ in range(length)]
ones_count = [0 for _ in range(length)]

while length == len(line):
    string = line
    for pos, char in enumerate(string):
        if char == "0":
            zeros_count[pos] += 1
        else: # char == "1"
            ones_count[pos] += 1
    line = f.readline()[:-1]

f.close()

gamma_string = ""
epsilon_string = ""
for i in range(length):
    if zeros_count[i] > ones_count[i]:
        gamma_string = gamma_string + "0"
        epsilon_string = epsilon_string + "1"
    else: # zeros < ones
        gamma_string = gamma_string + "1"
        epsilon_string = epsilon_string + "0"

gamma_count = 0
epsilon_count = 0
for i in range(length):
    gamma_count += int(gamma_string[length-i-1]) * 2**i
    epsilon_count += int(epsilon_string[length-i-1]) * 2**i

power_consumption = gamma_count * epsilon_count

print(zeros_count)
print(ones_count)

print(gamma_string, epsilon_string)
print("Gamma count:",gamma_count, "Epsilon count:",epsilon_count)
print("Power Consumption:", power_consumption)
