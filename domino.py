#DOMINO
from random import random, randint, choice
from itertools import combinations
class Player:
    ALL_PIECES = sorted(list(combinations(range(7), 2))+[(i,i) for i in range(7)])
    DRAWN_PIECES = []
    def __init__(self, NAME):
        self.name = NAME
        self.score = 0

    def getDeck(self, ALL_PIECES, DRAWN_PIECES):
        deck = sample([piece for piece in ALL_PIECES if piece not in DRAWN_PIECES], 7)
        DRAWN_PIECES += deck
        return deck




0123456
