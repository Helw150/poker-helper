suits = ["clubs", "spades", "hearts", "diamonds", "c", "s", "h", "d"]
named_cards = {"a": "1", "k": "13", "q": "12", "j": "11",  "t":"10"}
named_cards_reverse = {"1": "a", "13": "k", "12": "q", "11": "j", "10":"t"}
valid_values = list(named_cards.keys()) + [str(i) for i in range(2,11)]
