from CorePoker import Deck
from CorePoker import HelperCard as Card
from HandValue import handStrength
import pandas

class Game:
    def __init__(self, num_players = 5):
        self.num_players = num_players
        preflop = pandas.read_csv("preflop.csv")
        self.preflop = preflop[preflop.num_plyrs == num_players]
        del preflop
        self.win_prob = 0.0
        self.myHand = []
        self.board = []
        self.hand_strength = "Not Yet Set"
        self.newHand()
        
    def newHand(self):
        self.deck = Deck()

    def getInitialWinProbs(self):
        bigger = self.myHand[0]
        smaller = self.myHand[1]
        if bigger.value < smaller.value:
            tmp = bigger
            bigger = smaller
            smaller = tmp
        suit_string = 'o'
        if bigger.suit == smaller.suit:
            suit_string = 's'
        lookup_string = str(bigger.value) + '-' + str(smaller.value) + '-' + suit_string
        self.win_prob = self.preflop[lookup_string].iloc[0]

    def dealPockets(self, value1, suit1, value2, suit2):
        card1 = Card(value1, suit1)
        card2 = Card(value2, suit2)
        self.deck.viewCard(card1)
        self.deck.viewCard(card2)
        self.myHand = [card1, card2]
        self.getInitialWinProbs()

    def placeToBoard(self, value, suit):
        if len(self.board) == 5:
            print("Board is full, need new hand")
            return
        card = Card(value, suit)
        self.deck.viewCard(card)
        self.board.append(card)
        if len(self.board) >= 3:
            self.hand_strength = handStrength(self.myHand, self.board)
            self.win_prob = winProbability(self.myHand, self.board, self.deck.deck)

        
    def isDone(self):
        return len(self.board) == 5

    def computerState(self):
        return {"hand":self.myHand, "board": self.board, "win_prob":self.win_prob, "hand_strength":self.hand_strength}
    
    def __str__(self):
        stringified = []
        stringified.append("Your Hand\n")
        [stringified.append(str(card)+"-") for card in self.myHand]
        stringified.append("\nThe Board\n")
        [stringified.append(str(card)+"-") for card in self.board]
        stringified.append("\nProbability of Win\n")
        stringified.append(str(self.win_prob)+"\n")
        stringified.append("\nHand Strength\n")
        stringified.append(str(self.hand_strength)+"\n")
        return ' '.join(stringified)
