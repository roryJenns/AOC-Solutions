
#INPUT_FILENAME =  "test_input.txt" # Test File
INPUT_FILENAME =  "input.txt" # Real File
#OUTPUT_FILENAME = "test_output.txt" # Test Output File
OUTPUT_FILENAME = "output - incomplete.txt"

#FILE_LINES = 10 # test data
FILE_LINES = 102 # real data

 
## There is something about "illegal" lines? idk, I didn't account for it but test data works

point_reference = {")": 1,"]": 2,"}": 3,">": 4}
combo = {"{":"}", "[":"]", "(":")", "<":">",}
left_brackets = ["{","[","(","<"]
data = []

strings = []
points = []

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
        return self.tail

f = open(INPUT_FILENAME, "r")
for x in range(FILE_LINES):
    data.append(f.readline())
f.close()

def main():
    for x in range(FILE_LINES):
    #for x in range(1):
        stack = Stack()
        line = data[x]
        i = 0
        char = line[i]
        corrupted = False
        while char != "\n":
            if char in left_brackets:
                stack.PushStack(Node(char))
            else: # right bracket
                left = stack.PopStack()
                if combo[left] != char:
                    # the line is corrupted
                    corrupted = True
                    break
            i += 1
            char = line[i]
        if not corrupted:
            score = 0
            string = ""
            while stack.PeekStack() != -1:
                left = stack.PopStack()
                right = combo[left]
                string = string + right
                score = (5*score) + point_reference[right]
            strings.append(string)
            points.append(score)


main()

new = list(zip(points, strings))
new.sort()

f = open(OUTPUT_FILENAME, "w+")
for i in range(len(points)):
    f.write("{},{}\n".format(new[i][0], new[i][1]))
middle = new[int(len(new)/2)]
f.write("Middle : {}".format(middle[0]))
f.close()
