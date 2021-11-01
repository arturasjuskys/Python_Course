


#	================================================================================================
#	================================================================================================
#	================================================================================================



#	Section 25: Deck of Cards Exercise


#	248. Deck of Cards Intro Video
#	249. Deck of Cards Exercise Introduction Text
#	251. Deck of Cards Solution: Card Class
#	252. Deck of Cards Solution: Deck Class



#	Coding Exercise 80: Deck of Cards Test



#	================================================================================================
#	================================================================================================
#	================================================================================================



from random import shuffle
class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return "{} of {}".format(self.value, self.suit)

class Deck:
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = [Card(value, suit) for suit in suits for value in values]

    def count(self):
        return len(self.cards)

    def __repr__(self):
        return "Deck of {} cards".format(self.count())

    def _deal(self, num):
        count = self.count()
        actual = min([count, num])
        if count == 0:
            raise ValueError("All cards have been dealt")
        cards = self.cards[-actual:]
        self.cards = self.cards[:-actual]
        return cards

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, hand_size):
        return self._deal(hand_size)

    def shuffle(self):
        if self.count() < 52:
            raise ValueError("Only full deck can be shuffled")
        shuffle(self.cards)
        return self



#	================================================================================================
#	================================================================================================
#	================================================================================================

