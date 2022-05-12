TEST_INITIAL = [3,4,3,1,2]
NUMBER_OF_DAYS = 256
OUTPUT_FILENAME = "output256.txt"

import time

def calcsize(arr):
    total = 0
    for data in arr:
        total += data
    return total

def Index(offset, aim):
    result = (offset + aim) % 9
    return result

current =  time.perf_counter()

f = open("input.txt","r")
initial = f.readline().split(",")
initial[-1] = initial[-1][:-1]
f.close()

f = open(OUTPUT_FILENAME, "w+")

#initial = TEST_INITIAL # test case
data = [0 for x in range(9)]
for d in initial:
    data[int(d)] += 1

offset = 0
for x in range(NUMBER_OF_DAYS):
    size = calcsize(data)
    data[Index(offset,7)] += data[Index(offset,0)]
    f.write("{} : {} - {}\n".format(x+1, size, [data[Index(offset,i)] for i in range(9)]))
    offset += 1

delta =  time.perf_counter()-current

f.write("Time Taken = {}\n".format(delta))
f.write("Number of Fish = {}\n".format(calcsize(data)))
f.close()

print("Time Taken =", delta)
print("Number of Fish =", calcsize(data))