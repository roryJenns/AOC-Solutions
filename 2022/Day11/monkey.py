class Monkey:
    def __init__(self, items:list [int], operation, test:int, true:int, false:int):
        self.items = items
        self.op = operation
        self.test = test
        self.true = true
        self.false = false
        self.inspectCount = 0

    def inspectItem (self, item):
        self.inspectCount += 1
        return self.op(item)
    
    def inspectItems(self):
        self.items = list(map(self.inspectItem, self.items))
    
    def testItem(self,item):
        return item % self.test == 0
    
    def testItemResult(self,item):
        if self.testItem(item):
            return self.true
        else:
            return self.false
    
    def testAllItems(self):
        throwItems = zip(list(map(self.testItemResult, self.items)), self.items)
        self.items = []
        return throwItems
    
    def replaceItems(self, newItems):
        self.items = newItems
    
    def print(self):
        print(self.items,self.op,self.test,self.true,self.false)
    
    def relief(self):
        self.items = list(map(lambda x: int(x//3), self.items))
    
    def takeTurnPart1(self):
        self.inspectItems()
        self.relief()
        return self.testAllItems()

    def takeTurnPart2(self):
        self.inspectItems()
        # self.relief()
        return self.testAllItems()
    
    def addItem(self,item):
        self.items.append(item)
