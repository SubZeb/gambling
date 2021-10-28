import random
from itertools import product


class Card(object):
    """
    A card object. requires a suit and a rank(A, K, Q, J, 10, 9, etc.).  The Card.value is the value of the card
    for comparison purposes, but the property bj_value can be used to get the value of the card for blackjack.
    """
    def __init__(self, rank, suit):
        ranks = {'K': 13,
                 'Q': 12,
                 'J': 11,
                 'T': 10,
                 'A': 14
                 }
        self.rank = rank
        self.suit = suit.upper()
        self.value = int(rank) if rank.isdigit() else ranks[rank]

    def bj_value(self, ace_11=True):
        """
        Return the value of the card for blackjack
        :return: value of card for blackjack
        """
        value = self.value
        if value == 14 and ace_11:
            value = 11
        elif value == 14:
            value = 1
        elif value > 10:
            value = 10
        return value

    def __repr__(self):
        return '{}{}'.format(self.rank, self.suit)


class Deck(object):
    def __init__(self, num=1):
        self.suits = 'CDHS'
        self.ranks = '23456789TJQKA'
        self.order = [
            Card(card[0], card[1]) for card in product(self.ranks, self.suits)
        ]

        self.order *= num
        self.index = 0

    def shuffle(self):
        random.shuffle(self.order)
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.order):
            raise StopIteration
        card = self.order[self.index]
        self.index += 1
        return card
