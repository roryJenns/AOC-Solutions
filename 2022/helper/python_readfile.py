
def readData(filename):
    file = "input/"+filename
    with open(file, "r") as f:
        data = list(map(lambda x : x[:-1], f.readlines()))
    return data

def writeData(file, data):
    with open(file, "w+") as f:
        for l in data:
            if l == "":
                f.write("-1\n")
            else:
                f.write(str(l)+"\n")