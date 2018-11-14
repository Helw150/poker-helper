from AbstractGame import Game
from Constants import suits, valid_values

def getValuesFromInput(str_card):
    while True:
        r_input = input(str_card +" as VALUE, SUIT: ")
        split_array = r_input.split(", ")
        if len(split_array) != 2:
            continue
        value, suit = split_array
        value = value.lower()
        suit = suit.lower()
        if value in valid_values and suit in suits:
            return value, suit
        else:
            print("Malformed Input - try again")
while True:
    num_players = int(input("How many players? "))
    game = Game(num_players)
    first_value, first_suit = getValuesFromInput("First Pocket")
    second_value, second_suit = getValuesFromInput("Second Pocket")
    game.dealPockets(first_value, first_suit, second_value, second_suit)
    print(game)
    while not game.isDone():
        next_value, next_suit =  getValuesFromInput("Next Dealt Card")
        game.placeToBoard(next_value, next_suit)
        print(game)
        
