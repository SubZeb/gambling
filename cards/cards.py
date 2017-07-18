import random
from itertools import product


class Card(object):
    def __init__(self, rank, suit):
        ranks = {'K': 13,
                 'Q': 12,
                 'J': 11,
                 'T': 10,
                 'A': 14
                 }
        self.rank = rank
        self.suit = suit
        self.value = int(rank) if rank.isdigit() else ranks[rank]

    def __repr__(self):
        return '{}{}'.format(self.rank, self.suit)


class Deck(object):
    def __init__(self, num=1):
        self.suits = 'CDHS'
        self.ranks = '23456789TJQKA'
        self.order = list(Card(card[0], card[1]) for card in product(self.ranks, self.suits))
        self.order = self.order*num

    def shuffle(self):
        random.shuffle(self.order)
