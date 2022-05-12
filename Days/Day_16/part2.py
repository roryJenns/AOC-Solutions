class Packet():
    def __init__(self):
        self.size = 0

    def setSize(self,size):
        self.size = size
    
    def print(self):
        print(self.size, end=" ")

class PacketLiteral(Packet):
    def __init__(self):
        super().__init__()
        self.number = 0
    
    def setNum(self,num):
        self.number = num
    
    def resolveValue(self):
        return self.number
    
    def print(self):
        super().print()
        print(self.number, end=" ")

class PacketOperator(Packet):
    def __init__(self):
        super().__init__()
        self.args = []
        self.lengthType = 0
        self.length = 0
    
    def addArgument(self, packet):
        self.args.append(packet)
    
    def addLengthInformation(self, lengthType, length):
        self.lengthType = lengthType
        self.length = length
    
    def print(self):
        super().print()
        print(self.lengthType,self.length,end=" ")


class PacketSum(PacketOperator):
    def __init__(self):
        super().__init__()

    def resolveValue(self):
        # print("SUM(",end=" ")
        sum = 0
        for arg in self.args:
            val = arg.resolveValue()
            sum += val
            # print(val,end=",")
        # print(")",end=" ")
        return sum

class PacketProduct(PacketOperator):
    def __init__(self):
        super().__init__()
    
    def resolveValue(self):
        # print("PRODUCT(",end=" ")
        product = 1
        for arg in self.args:
            val = arg.resolveValue()
            product *= val
        #     print(val,end=",")
        # print(")",end=" ")
        return product

class PacketMax(PacketOperator):
    def __init__(self):
        super().__init__()
    
    def resolveValue(self):
        # print("MAX(",end=" ")
        maximum = self.args[0].resolveValue()
        for arg in self.args:
            maximum = max(maximum, arg.resolveValue())  
        #     print(maximum,end=",")
        # print(")",end=" ")  
        return maximum

class PacketMin(PacketOperator):
    def __init__(self):
        super().__init__()

    def resolveValue(self):
        # print("MIN(",end=" ")
        minimum = self.args[0].resolveValue()
        for arg in self.args:
            minimum = min(minimum, arg.resolveValue())    
        #     print(minimum,end=",")
        # print(")",end=" ")
        return minimum

class PacketGreater(PacketOperator):
    def __init__(self):
        super().__init__()

    def resolveValue(self):
        # print("GREATER(",end=" ")
        a = self.args[0].resolveValue()
        b = self.args[1].resolveValue()
        # print(str(a)+","+str(b),end=")")
        return int(a > b)

class PacketLess(PacketOperator):
    def __init__(self):
        super().__init__()

    def resolveValue(self):
        # print("LESSER(",end=" ")
        a = self.args[0].resolveValue()
        b = self.args[1].resolveValue()
        # print(str(a)+","+str(b),end=")")
        return int(a < b)

class PacketEqual(PacketOperator):
    def __init__(self):
        super().__init__()
    
    def resolveValue(self):
        # print("EQUAL(",end=" ")
        a = self.args[0].resolveValue()
        b = self.args[1].resolveValue()
        # print(str(a)+","+str(b),end=")")
        return int(a == b)

INPUT_FILENAME = "processed_packets.txt"

def readData():
    typeIDtoObject = [PacketSum, PacketProduct,PacketMin,PacketMax,PacketLiteral,PacketGreater,PacketLess,PacketEqual]
    packets = []
    f = open(INPUT_FILENAME, 'r')
    line = f.readline()
    count = 0
    while line != "":
        packetInfo = list(map(int, line[:-1].split(',')))

        typeID = packetInfo[0]
        packetSize = packetInfo[1]

        packet = typeIDtoObject[typeID]()
        packets.append(packet)
        packet.setSize(packetSize)

        if typeID == 4:
            packet.setNum(packetInfo[2])
        else:
            lengthTypeID = packetInfo[2]
            length = packetInfo[3]
            packet.addLengthInformation(lengthTypeID, length)

        line = f.readline()

    f.close()
    return packets


def calcBitSize(packets, current, final):
    total = 0
    for index in range(current+1,final+1):
        total += packets[index].size
    return total

def giveOperatorsArguments(packets, index):
    packet = packets[index]
    if index >= len(packets):
        return 0
    if type(packet) == PacketLiteral:
        return index
    
    if packet.lengthType == 0:
        bitsPassed = 0
        nextPacket = index + 1
        
        while bitsPassed < packet.length:
            arg = packets[nextPacket]
            packet.addArgument(arg)

            lastPassedPacket = giveOperatorsArguments(packets, nextPacket)
            bitsPassed = calcBitSize(packets, index, lastPassedPacket)
            nextPacket = lastPassedPacket + 1
        
        return lastPassedPacket
            
    elif packet.lengthType == 1:
        numberOfArguments = packet.length
        nextPacket = index + 1
        for packetNum in range(numberOfArguments):
            arg = packets[nextPacket]
            packet.addArgument(arg)

            lastPassedPacket = giveOperatorsArguments(packets, nextPacket)
            nextPacket = lastPassedPacket + 1
        return lastPassedPacket
    else:
        print("big heckin problem")



def main():
    packets = readData()

    giveOperatorsArguments(packets, 0)

    result = packets[0].resolveValue()

    return result

    ## PLAN
    # read data #
    # turn into packets #
    # put packets into array #
    # loop through packets
    #       set args
    # resolve value the first
    # results :)


evaluation = main()

print(evaluation)
