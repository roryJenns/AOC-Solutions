from matplotlib import pyplot as plt    
from matplotlib import style    
style.use('ggplot')    

SIZE_OF_DATA = 1935
FILENAME = "output2.txt"

x = [i for i in range(SIZE_OF_DATA)]
f = open(FILENAME, "r")
y = []
for a in range(SIZE_OF_DATA):
    y.append(int(f.readline().split(":")[-1][:-1]))
f.close()

print(len(x), len(y))

plt.scatter(x, y)    
    
plt.title("The fuel expediture of Crab Submarines")    
plt.ylabel("Total Fuel Cost")    
plt.xlabel("Position to Move to")    
    
plt.show()    