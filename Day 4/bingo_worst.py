
def calculate_winning_depth(board, order):

    # I'm sad because Diagonals don't count :(

    size = len(board)
    # Maximum index per row
    row_max = [0 for x in range(size)]
    col_max = [0 for x in range(size)]
    #diag_max = [0,0]

    for i in range(size):
        row_max[i] = max([order.index(board[i][x]) for x in range(size)])
        col_max[i] = max([order.index(board[x][i]) for x in range(size)])

    #diag_max[0] = max([int(board[x][x]) for x in range(size)])
    #diag_max[1] = max([int(board[x][size-x-1]) for x in range(size)])

    row_min = min(row_max)
    col_min = min(col_max)
    #diag_min = min(diag_max)

    line_min = min([row_min, col_min]) #, diag_min])

    return line_min


f = open("input.txt", "r")

order = f.readline().split(",")
order[-1] = order[-1][:-1]
#print(order)

empty = f.readline()
bingoBoards = []

while empty != "-1":
    bingoBoards.append([])
    for x in range(5):
        bingoBoards[-1].append(f.readline().split(" "))
        bingoBoards[-1][-1][-1] = bingoBoards[-1][-1][-1][:-1]
        while '' in bingoBoards[-1][-1]:
            bingoBoards[-1][-1].remove('')

    empty = f.readline()

f.close()
print(len(bingoBoards))

amount_needed = [-1 for _ in range(len(bingoBoards))]

for index, board in enumerate(bingoBoards):
    amount_needed[index] = calculate_winning_depth(board, order)

min_needed = max(amount_needed)
minBoardIndex = amount_needed.index(min_needed)
winningBoard = bingoBoards[minBoardIndex]

adjusted_order = order[:min_needed+1]
last_call = int(order[min_needed])

unused_total = 0

print("board:")
for line in winningBoard:
    for item in line:
        if item in adjusted_order:
            print("--", end=" ")
        else:
            print(item, end=" ")
            unused_total += int(item)
    print()
print("index:",minBoardIndex)
print("number of calls:",min_needed)
print("last call:", last_call)
print("unused sum:", unused_total)

print("unused sum * last call :", unused_total*last_call)






