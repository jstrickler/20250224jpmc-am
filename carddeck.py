import random
from card import Card

class CardDeck:
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    SUITS = 'Clubs Diamonds Hearts Spades'.split()

    def __init__(self):
        self._cards = None  # optional
        self._make_deck()

    def _make_deck(self):
        self._cards = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = Card(rank, suit)
                self._cards.append(card)
    
    @property
    def cards(self):
        return self._cards
    
    def shuffle(self):
        random.shuffle(self._cards)
    
    # instance
    def draw(self):
        return self._cards.pop()
    
    @classmethod
    def get_ranks(cls):
        return cls .RANKS
    
    @staticmethod
    def bark(bark_type):
        print(f"{bark_type}! {bark_type}!")

    def __add__(self, other):
        new_obj = type(self)()
        new_obj._cards = self._cards + other._cards
        return new_obj
    
    def __mul__(self, value):
        new_obj = type(self)()
        new_obj._cards = self._cards * value
        return new_obj
    
    def __len__(self):
        return len(self._cards)

if __name__ == "__main__":
    d1 = CardDeck()
    d1.shuffle()
    print(d1.cards)
    print()
    for i in range(5):
        print(d1.draw())
    print()
    print(d1.get_ranks())
    print(CardDeck.get_ranks())
    CardDeck.bark("woof")
    CardDeck.bark("yip")
    d2 = CardDeck()
    x = d1 + d2
    print(x)
    print(x.cards)
    print(len(d1))
    print(len(d2))
    print(len(x))
    y = x * 3
    print(len(y))

    #  p1 = Path("foo")
    #  p2 = Path("bar")
    #  p3 = p1 / p2   # foo/bar

