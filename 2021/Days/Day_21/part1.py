

P1_START = 3
P2_START = 7



def roll_dice () :
    global last_roll, num_rolls
    last_roll += 1
    num_rolls += 1
    if last_roll == 101:
        last_roll = 1
    return last_roll

def roll_thrice ():
    return roll_dice() + roll_dice() + roll_dice() % 10


def move(position):
    x = (position + roll_thrice()) % 10
    if x == 0:
        x = 10
    return x
        

def main():
    player_data = [[P1_START,0],[P2_START,0]]

    i = 0
    while player_data[0][1] < 1000 and player_data[1][1] < 1000:
        pos = move(player_data[i][0])
        player_data[i][0]  = pos
        player_data[i][1] += pos

        i = not i

    print(player_data)
    global num_rolls
    print(num_rolls * min(player_data[0][1], player_data[1][1]))  

last_roll = 0
num_rolls = 0

main()
