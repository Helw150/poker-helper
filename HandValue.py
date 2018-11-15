from deuces import evaluator
evaluator = evaluator.Evaluator()

def handStrength(hand, board):
    board_internal = [card.internal for card in board]
    hand_internal = [card.internal for card in hand]
    score = evaluator.evaluate(board_internal, hand_internal)
    return score

def boardRecurse():
    get all possible boards

def winProbability(hand, board, deck):
    boards = boardRecurse(board, deck)
    prob = 0
    for board in boards:
        prob += getScenarioWinProbability(board, hand, deck)
    return prob/len(boards)

def handRecurse():
    get all possible hands
    
def getScenarioWinProbability(hand, board, deck):
    hands = handRecurse(deck)
    wins = 0
    for oppHand in hands:
        myStrength = handStrength(hand, board)
        opponentStrength = handStrength(oppHand, board)
        if myStrength > opponentStrength:
            wins += 1
    return wins/len(hands)
