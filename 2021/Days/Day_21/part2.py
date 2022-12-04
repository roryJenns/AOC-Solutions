from functools import cache
import itertools

P1_START = 3
P2_START = 7

@cache
def runGame(p1_pos, p1_score, p2_pos, p2_score, turn):
    if p1_score >= 21:
        return (1,0)
    if p2_score >= 21:
        return (0,1)
    
    pos = p1_pos if turn else p2_pos

    # new positions for each throw

    new_positions = [(pos + throw - 1) % 10 + 1 for throw in throws]

    # new games for each position

    if turn:
        # player1
        subgames = [runGame(new_p, p1_score + new_p, p2_pos, p2_score, not turn) for new_p in new_positions]
    else:
        # player2
        subgames = [runGame(p1_pos, p1_score, new_p, p2_score + new_p, not turn) for new_p in new_positions]

    return (sum(win for win, _ in subgames), sum(win for _, win in subgames))
    


throws = [sum(x) for x in itertools.product([1, 2, 3], repeat=3)]

wins = runGame(P1_START, 0, P2_START, 0, True)

print(max(wins))