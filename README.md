# Gambling Python Package
####A project to create the necessary tools for gambling, such as cards and dice

| Author | CJ Stein |
| ------ | ------- |
| Version | 1.0.0.dev2 |
|Python Version| Only Tested on Python 3|

Currently supports creation of:

- Dice
- Cards
##Installation
    pip install gambling
##Usage
###Dice

Input for Dice:
Numbers shown are the default
- num=1         # This is the number of dice to use
- sides=6       # This is the number of sides on each dice

For 5 6-sided dice for something such as Yahtzee here would be the command:

    from gambling import Dice
    dice = Dice(num=5)

For one 20 sided dice for something like D&D:

    from gambling import Dice
    dice = Dice(sides=20)
For 3 20 sided dice:

    from gambling import Dice
    dice = Dice(num=3, sides=20)

Methods for Dice:

    dice.roll()   # This causes the list under the Dice.values to simulate a new roll.
    dice.values  # This will show the list of the values on the dice. The list is equal in length to the number of dice
    # ouput example: [1, 2, 3, 4, 5]

###Cards

There are two objects in the Cards package:

- Card
- Deck

A Deck builds a list of Card objects.  Cards rank and suits can be called, along with value if needed for arithmetic needs such as blackjack or war.
The input needed for a card is a single letter rank as a string and a single letter suit.

Some things you can get from card:

    from gambling import Card, Deck
    AceOfSpades = Card('A','S')
    TenOfHearts = Card('10','H')
    TenOfHearts.rank  # This will return 10
    TenOfHearts.suit  # This will return 'H'
    AceOfSpades.rank  # This will return 'A'
    AceOfSpades.value # This will return 14, 'J' : 11, 'Q':12, 'K':13, 'A':14

Making cards by themselves isn't very useful, but making decks will be useful and you can use the Card object to get a value
There is one optional input for Deck:

- num = 1  #  It defaults to using one deck, but you can change that to multiple decks if needed for something like blackjack


    PokerDeck = Deck()
    PokerDeck.order  # This returns a new deck with the cards in order
    PokerDeck.shuffle()  # This shuffles the deck to randomize the order
    next(PokerDeck)  # This calls the next card in the deck, the deck can be used as an iterator as such


