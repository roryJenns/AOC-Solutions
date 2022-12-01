
def getLineInt(f):
    line = f.readline()
    line = line[:-1]
    try:
        return int(line)
    except:
        return -1

def queueSum():
    return queue[0] + queue[1] + queue[2]

f = open("input.txt", "r")

queue = [0,0,0]
index = 2
nextIndex = [1,2,0]

number = getLineInt(f)
queue[0] = number
number = getLineInt(f)
queue[1] = number
number = getLineInt(f)
queue[2] = number

increasedCounter = 0
previousTotal = queueSum()
while (number != -1):
#for x in range(50):
    queue[index] = number
    #print(queueSum(), end=" ")
    #print(queue, end=" ")
    if previousTotal < queueSum():
        increasedCounter += 1
        #print("increased", end=" ")
    #print()
    previousTotal = queueSum()
    index = nextIndex[index]
    number = getLineInt(f)

f.close()

print(increasedCounter)
