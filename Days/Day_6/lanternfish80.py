import time
TEST_INITIAL = [3,4,3,1,2]

f = open("input.txt","r")
data = f.readline().split(",")
data[-1] = data[-1][:-1]
f.close()
size = len(data)
for i in range(size):
    data[i] = int(data[i])

current =  time.perf_counter()
#data = test_data
for x in range(80):
    size = len(data)
    for i in range(size):
        if data[i] == 0:
            data[i] = 6
            data.append(8)
        else:
            data[i] -= 1

delta =  time.perf_counter()-current
print("Time Taken =", delta)
print("Number of Fish =", len(data))