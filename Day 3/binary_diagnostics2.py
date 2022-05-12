
def binaryToDecimal(gamma_string,epsilon_string):
    gamma_count = 0
    epsilon_count = 0
    length = len(gamma_string)
    for i in range(length):
        gamma_count += int(gamma_string[length-i-1]) * 2**i
        epsilon_count += int(epsilon_string[length-i-1]) * 2**i

    return gamma_count,epsilon_count


f = open("input destruction.txt", "r")

data = []
line = f.readline()[:-1]
length = len(line)
while (len(line) == length):
    data.append(line)
    line = f.readline()[:-1]

counter = {"0":0,"1":0}

for column in range(length):
    counter["0"] = 0
    counter["1"] = 0
    for x in data:
        counter[x[column]] += 1
    max = "1"

    # Use the first if for MAX / Oxygen Gen, 
    # or the second for MIN / CO2 Scrubber
    
    #if counter["0"] > counter["1"]:
    if counter["0"] <= counter["1"]:
        max = "0"
    #print(max, counter["0"], counter["1"])
    for i in range(len(data)-1,-1,-1):
        if data[i][column] != max:
            data.pop(i)
    if len(data) == 1:
        break

#print("*******")
print(data)

# 010110111111
# 111001011110

a, b = binaryToDecimal("010110111111","111001011110")
print(a,b,a*b)

"""
result = -1
counter = 1
arr = []
while True:
    if len(data[0]) >= len(data[1]):
        arr = data[1]
    else:
        arr = data[0]
    data = [[],[]]
    for line in arr:
        data[int(line[counter])].append(line)
    counter += 1
    if counter > 3:
        print("***********")
        print(counter)
        print(len(arr))
        print(len(data[0]))
        print(len(data[1]))

    if counter > 12:
        print("fail")
        break

    if len(data[0]) + len(data[1]) == 1:
        if len(data[0]) == 1:
            result = data[0][0]
            break
        elif len(data[1]) == 1:
            result = data[1][0]
            break

print(result)
"""
# Most common  - 010110111101
# Least common - 111001011110

# 010110111111
# 111011001011
"""
a, b = binaryToDecimal("010110111111","111011001011")

print(a,b)
print(a*b)
"""