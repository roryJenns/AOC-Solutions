
def readData(filename):
    file = "input/"+filename
    f = open(file, "r")
    data = list(map(lambda x : x[:-1], f.readlines()))
    f.close()
    return data