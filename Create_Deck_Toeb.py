# creating the deck, Toeb's version

import itertools
import random

deck = list(itertools.product(range(1, 14), ["Spades", "Diamonds", "Hearts", "Clubs"]))
random.shuffle(deck)

# range(13) because each player gets 13 cards at the start of their turn
for i in range(13):
    print(deck[i][0], "of", deck[i][1])
