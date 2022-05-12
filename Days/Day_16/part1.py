
INPUT_FILENAME = "input.txt"

def readData():
    f = open(INPUT_FILENAME, "r")
    line = f.readline()[:-1]
    f.close()
    return hexToBin(line)

def hexToBin(line):
    hex_to_bin = {
        "0":"0000",
        "1":"0001",
        "2":"0010",
        "3":"0011",
        "4":"0100",
        "5":"0101",
        "6":"0110",
        "7":"0111",
        "8":"1000",
        "9":"1001",
        "A":"1010",
        "B":"1011",
        "C":"1100",
        "D":"1101",
        "E":"1110",
        "F":"1111"
        }
    bin_string = ""
    for char in line:
        bin_string = bin_string + hex_to_bin[char]
    return bin_string

def binToDex(string):
    total = 0
    for index in range(len(string)):
        char = string[-index-1]
        if char == "1":
            total += 2**index
    return total


def getVersion(packet):
    versionBin = packet[:3]
    version = binToDex(versionBin)
    return version

def getTypeID(packet):
    typeIDBin = packet[3:6]
    typeID = binToDex(typeIDBin)
    return typeID

def getLengthTypeID(packet):
    return int(packet[6])

def getNumberFromType4(packet):
    global global_index
    numberBinary = ""

    i = 6
    prefix = packet[i]

    while prefix == "1":
        numberBinary += packet[i+1:i+5]
        i += 5
        prefix = packet[i]
    
    numberBinary += packet[i+1:i+5]

    number = binToDex(numberBinary)

    global_index += i + 5

    return number


def getTypeZeroPacketSize(packet):
    return binToDex(packet[7:22]) # 7 + 15 = 22

def getTypeOnePacketCount(packet):
    return binToDex(packet[7:18]) # 7 + 11 = 18


def analyseTypePacket(packet): 
    # OPPACKET -> TypeID, (TypeLengthID, length)
    # LITERAL  -> TypeID, Value
    global global_index

    typeID = getTypeID(packet)
    if typeID == 4:
        return 4, getNumberFromType4(packet)
    else:
        lengthTypeID = getLengthTypeID(packet)
        if lengthTypeID == 0:
            packetSize = getTypeZeroPacketSize(packet)
            global_index += 7 + 15
            return typeID, (0, packetSize)
        elif lengthTypeID == 1:
            packetCount = getTypeOnePacketCount(packet)
            global_index += 7 + 11
            return typeID, (1, packetCount)
    

def writeData(array):
    f = open("processed_packets.txt", 'w')
    for line in array:
        f.write(line)
    f.close()


def main():

    array = []
    binary = readData()
    
    sum = 0
    version = getVersion(binary)
    old_index = global_index
    while global_index +6 < len(binary):
        typeID, data = analyseTypePacket(binary[global_index:])
        size = global_index-old_index
        old_index = global_index
        
        if type(data) == int:
            print(typeID,size,data)
            array.append("{},{},{}\n".format(typeID, size, data))
        else:
            print(typeID,size,data[0],data[1])
            array.append("{},{},{},{}\n".format(typeID, size, data[0],data[1]))
        sum += version
        version = getVersion(binary[global_index:])

    print(sum)
    writeData(array)
    

global_index = 0
main()


# print(readData())
# analysePacket("110100101111111000101000")
# print(binToDex("11011"))

# OUTPUT FILE FORMAT
# OPERATOR : typeID, packetsize, lengthTypeID, length
# LITERAL  : typeID, packetsize, number