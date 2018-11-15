from deuces import evaluator
evaluator = evaluator.Evaluator()

def handStrength(hand, board):
    board_internal = [card.internal for card in board]
    hand_internal = [card.internal for card in hand]
    score = evaluator.evaluate(board_internal, hand_internal)
    return score

def handStrengthInternal(hand, board_internal):
    hand_internal = [card.internal for card in hand]
    score = evaluator.evaluate(board_internal, hand_internal)
    return score

def boardRecurse(board, deck):
    if len(board) == 5:
        return [board]
    if len(deck) == 0:
        return []
    boards = []
    for i, card in enumerate(deck):
        boards.extend(boardRecurse(board+[card], deck[i+1:]))
    return boards

def winProbability(hand, board, deck):
    boards = boardRecurse(board, deck)
    print(len(boards))
    prob = 0
    counter = 0
    for board in boards:
        counter += 1
        prob += getScenarioWinProbability(hand, board, deck)
    return prob/len(boards)

def handRecurse(hand, deck, board_internal):
    if len(hand) == 2:
        return [hand]
    if len(deck) == 0:
        return []
    hands = []
    for i, card in enumerate(deck):
        if card.internal not in board_internal:
            hands.extend(handRecurse(hand+[card], deck[i+1:], board_internal))
    return hands
    
def getScenarioWinProbability(hand, board, deck):
    board_internal = [card.internal for card in board]
    hands = handRecurse([], deck, board_internal)
    wins = 0
    myStrength = handStrength(hand, board)
    for oppHand in hands:
        opponentStrength = handStrengthInternal(oppHand, board_internal)
        if myStrength < opponentStrength:
            wins += 1
    return wins/len(hands)
