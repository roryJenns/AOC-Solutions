from math import pow
card_strength = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
powers = list(map(lambda x: pow(13, x), range(5)))
TOP_POWER = pow(13, 6)

def parse(line):
    hand, bid = line[:-1].split(" ")
    return hand, int(bid)

def hand_summary(hand):
    cards = {}
    for card in hand:
        if card not in cards:
            cards[card] = 0
        cards[card] += 1
    
    max_count = 0
    second_count = 0
    joker_count = 0
    for card, count in cards.items():
        if card_strength[0] == 'J' and card == "J":
            joker_count = count
            continue
        if count > second_count:
            if count > max_count:
                second_count = max_count
                max_count = count
            else:
                second_count = count

    return max_count, second_count, joker_count

def hand_type(hand):
    max_count, second_count, joker_count = hand_summary(hand)

    # 1
    if max_count == 1:
        return [1, 2, 4, 6, 7][joker_count]
    # 2
    if max_count == 2 and second_count < 2:
        return [2, 4, 6, 7][joker_count]
    # 3
    if max_count == 2 and second_count == 2:
        return [3, 5][joker_count]
    # 4
    if max_count == 3 and second_count < 2:
        return [4, 6, 7][joker_count]
    # 5
    if max_count == 3 and second_count == 2:
        return 5
    # 6
    if max_count == 4:
        return [6, 7][joker_count]
    # 7
    if max_count == 5 or joker_count == 5:
        return 7

def card_score(hand):
    score = 0
    for position, strength in enumerate(map(card_strength.index, hand)):
        score += powers[-position-1] * strength
    return score

def hand_score(hand):
    return TOP_POWER * hand_type(hand) + card_score(hand)

def get_score(pairing):
    return hand_score(pairing[0])

with open("input_day7.txt") as f:
    game = list(map(parse, f.readlines()))

N = len(game)
def run_it():
    ordered_game = sorted(game, key=get_score)
    return sum(map((lambda pair: pair[0][1]*pair[1] ), zip(ordered_game, range(1,N+1))))
    
result1 = run_it()
print("Part 1:", result1)

card_strength.remove('J')
card_strength.insert(0, 'J')
result2 = run_it()
print("Part 2:", result2)

