# def getFirstLine(f):
#     line = f.readline()
#     line = line[:-1]
#     return line

def getLineInt(f):
    line = f.readline()
    line = line[:-1]
    try:
        return int(line)
    except:
        return -1

f = open("input.txt", "r")

number = getLineInt(f)

increasedCounter = 0
newNum = 0

while (newNum != -1):
    if newNum > number:
        increasedCounter += 1
    number = newNum
    newNum = getLineInt(f)

f.close()
print(increasedCounter)
