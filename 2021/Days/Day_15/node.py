class Node():
    def __init__(self, weight, x, y):
        self.weight = weight
        self.col = x
        self.row = y
    
    def GetWeight(self):
        return self.weight

    def GetCoords(self):
        return tuple(self.col,self.row)
    
    def GetX(self):
        return self.col
    
    def GetY(self):
        return self.row

    def GetCol(self):
        return self.col
    
    def GetRow(self):
        return self.row


class Stack():
    def __init__(self):
        self.__stack = []

    def Push(self, node):
        self.__stack.append(node)
    
    def Pop(self):
        return self.__stack.pop()

    def Peek(self):
        return self.__stack[-1]
    
    def Visited(self, node):
        for vertex in self.__stack:
            if vertex == node:
                return True
        return False

    def Duplicate(self):
        queue = Stack()
        for node in self.__stack:
            queue.Push(node)
        return queue
    
    def Copy(self, queue):
        for node in queue.__stack:
            self.Push(node)
    
    def Delete(self):
        for i in range(len(self.__stack)):
            self.Pop()

    def Print(self):
        for node in self.__stack:
            print(node.GetWeight(), end=",")
        print()