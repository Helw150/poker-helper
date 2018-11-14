from Constants import suits, named_cards, named_cards_reverse

class Card:
    def __init__(self, value, suit):
        value = value
        suit = suit
        self.print_value = value
        if value in named_cards.keys():
            value = named_cards[value]
        if value in named_cards_reverse.keys():
            self.print_value = named_cards_reverse[value]
        self.suit = suit
        self.value = int(value)

    def __str__(self):
        return str(self.print_value) +' '+ str(self.suit)

    def __repr__(self):
        return self.__str__()
    
class Deck:
    def __init__(self):
        self.deck = []
        for value in range(1,14):
            for suit in suits:
                self.deck.append(Card(str(value), str(suit)))
    
    def viewCard(self, viewedCard):
        for i, card in enumerate(self.deck):
            if card.value == viewedCard.value and card.suit == viewedCard.suit:
                self.deck.pop(i)
                break
