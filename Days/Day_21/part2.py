

P1_START = 4
P2_START = 8

def newWorldPlayer(player_worlds_at_score):
    p_temp = [0 for _ in range(1+21+9)]
    for initial_score in range(21):
        num_worlds = player_worlds_at_score[initial_score]

        for dice_sum in range(3,9+1):
            worlds_created = outcomes[dice_sum]

            p_temp[initial_score+dice_sum] += worlds_created * num_worlds
    
    for i,x in enumerate(p_temp):
        player_worlds_at_score[i] = x
    
    return player_worlds_at_score


last_roll = 0

outcomes = [0, 0, 0, 1, 3, 6, 7, 6, 3, 1]
player1_worlds_at_score = [0 for _ in range(1+21+9)]
player1_worlds_at_score[0] = 1
player2_worlds_at_score = [0 for _ in range(1+21+9)]
player2_worlds_at_score[0] = 1

p = player1_worlds_at_score
print (p)
p =  newWorldPlayer(p)
print (p)
p =  newWorldPlayer(p)
print (p)
p =  newWorldPlayer(p)
print (p)
p =  newWorldPlayer(p)
print (p)
p =  newWorldPlayer(p)
print (p)
p =  newWorldPlayer(p)
print (p)
p =  newWorldPlayer(p)
print (p)
p =  newWorldPlayer(p)
print (p)
p =  newWorldPlayer(p)
print (p)



