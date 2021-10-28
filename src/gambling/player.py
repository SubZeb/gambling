from cards import Card


class CardPlayer(object):
    def __init__(self, name=None):
        self.hand = []
        self.name = name

    def new_card(self, card: Card):
        self.hand.append(card)

    def new_hand(self):
        self.hand = []
