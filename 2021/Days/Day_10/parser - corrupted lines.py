
#INPUT_FILENAME =  "test_input.txt" # Test File
INPUT_FILENAME =  "input.txt" # Real File
#OUTPUT_FILENAME = "test_output - corrupted.txt" # Test Output File
OUTPUT_FILENAME = "output - corrupted.txt" # Real output

#FILE_LINES = 10 # test data
FILE_LINES = 102 # real data

 
## There is something about "illegal" lines? idk, I didn't account for it but test data works

point_reference = {")": 3,"]": 57, "}": 1197, ">": 25137}
combo = {"{":"}", "[":"]", "(":")", "<":">",}
left_brackets = ["{","[","(","<"]
data = []

point_total = 0

class Node():
    def __init__(self, data):
        self.next = -1
        self.data = data

class Stack():
    def __init__(self):
        self.tail = -1
    
    def PushStack(self, node):
        if self.tail == -1:
            self.tail = node
        else:
            node.next = self.tail
            self.tail = node
    
    def PopStack(self):
        node = self.tail
        self.tail = node.next
        return node.data

    def PeekStack(self):
        return self.tail.data

f = open(INPUT_FILENAME, "r")
for x in range(FILE_LINES):
    data.append(f.readline())
f.close()

def main():
    global point_total
    for x in range(FILE_LINES):
    #for x in range(1):
        stack = Stack()
        line = data[x]
        i = 0
        char = line[i]
        while char != "\n":
            if char in left_brackets:
                stack.PushStack(Node(char))
            else:
                left = stack.PopStack()
                if combo[left] != char:
                    f.write("Line {}, Char {}: Expected {}, but found {} instead.\n".format(x, i, combo[left], char))
                    point_total += point_reference[char]
                    break

            i += 1
            char = line[i]


f = open(OUTPUT_FILENAME, "w+")
main()
f.write("Point Total : {}\n".format(point_total))
f.close()

print(point_total)