from node import Node

class Stack():
    def __init__(self):
        self.__stack = []

    def Push(self, node):
        self.__stack.append(node)
    
    def Pop(self):
        return self.__stack.pop()

    def Peek(self):
        return self.__stack[-1]

    def Print(self):
        for node in self.__stack:
            if node.name == "end":
                break
            print(node.name, end=", ")
        print(node.name)
    
    def PrintString(self):
        string = self.__stack[0].name
        for index in range(1, len(self.__stack)):
            node = self.__stack[index]
            string = string + "," + node.name
        string = string + "\n"
        return string
    
    def Visited(self, node):
        for vertex in self.__stack:
            if vertex.name == node.name:
                return not vertex.isLarge()
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
