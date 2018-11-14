
def isStraight(hand):
    hand_values = [card.value for card in hand]
    hand_values.sort()
    if hand_values[0] == 1 and hand_values[-1] == 13:
        hand_values.pop(0)
    for i, value in enumerate(hand_values):
        if i == 0:
            continue
        else:
            if hand_values[i-1]+1 != hand_values:
                return False
    return True

def isPair(hand):
    counter = 0
    max_counter = 0
    hand_values = [card.value for card in hand]
    hand_values.sort()
    for i, value in enumerate(hand_values[1:]):
        
        if value == hand_values[i]:
            counter += 1
        else:
            counter = 0
        max_counter = max(counter, max_counter)
    return max_counter == 1

def isTwoPair(hand):
    counter = 0
    twoCounter = 0
    max_counter = 0
    hand_values = [card.value for card in hand]
    hand_values.sort()
    for i, value in enumerate(hand_values[1:]):
        if value == hand_values[i]:
            counter += 1
        else:
            counter = 0
        if counter == 1:
            twoCounter += 1
    return twoCounter == 2

def isThree(hand):
    counter = 0
    max_counter = 0
    hand_values = [card.value for card in hand]
    hand_values.sort()
    for i, value in enumerate(hand_values[1:]):
        if value == hand_values[i]:
            counter += 1
        else:
            counter = 0
        max_counter = max(counter, max_counter)
    return max_counter == 2

def isFour(hand):
    counter = 0
    max_counter = 0
    hand_values = [card.value for card in hand]
    hand_values.sort()
    for i, value in enumerate(hand_values[1:]):
        if value == hand_values[i]:
            counter += 1
        else:
            counter = 0
        max_counter = max(counter, max_counter)
    return max_counter == 3

def isRoyal(hand):
    hand_values = [card.value for card in hand]
    hand_values.sort()
    return hand_values == [1, 10, 11, 12, 13]

def isFlush(hand):
    hand_suits = [card.suit for card in hand]
    only_suit = hand_suits[0]
    for suit in hand_suits:
        if suit != only_suit:
            return False
    return True


def comboUtil(river, current_combo = [], n=3):
    if len(current_combo)+len(river) < n:
        return []
    if len(current_combo) == n:
        return [current_combo]
    combos = []
    for i, card in enumerate(river):
        combos.extend(comboUtil(river[i+1:], current_combo+[card]))
    return combos

def findValue(hand):
    pair = isPair(hand)
    twoPair = isTwoPair(hand)
    three = isThree(hand)
    four = isFour(hand)
    straight = isStraight(hand)
    flush = isFlush(hand)
    royal = isRoyal(hand)
    if royal and flush:
        return 9
    elif straight and flush:
        return 8
    elif four:
        return 7
    elif three and pair:
        return 6
    elif flush:
        return 5
    elif straight:
        return 4
    elif three:
        return 3
    elif twoPair:
        return 2
    elif pair:
        return 1
    else:
        return 0
    
def handStrength(hand, river):
    hand_strength = 0
    for hands in comboUtil(river):
        hand_strength = max(hand_strength, findValue(hand+hands))
    return hand_strength
