class Card:  # inherits from 'object'
    color = "blue"

    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit
    
    @property
    def rank(self):  # getter property
        return self._rank
    # rank = property(rank)

    @rank.setter
    def rank(self, value):
        # validate the value
        self._rank = value    

    @property
    def suit(self):
        return self._suit.title()
    
    def __str__(self):
        return f"{self.rank}-{self.suit}"
    
    def __repr__(self):
        return f"Card('{self.rank}', '{self.suit}')"

if __name__ == "__main__":
    c = Card("8", "clubs")  # call Card.__init__(...)
    print(c)
    print(repr(c))
    print(f"{c = }")
    print(f"{c.rank = }") # NOT c.rank()
    print(f"{c.suit = }")
    print(f"{Card.color = }")
    c.rank = "A"

    # x = c.get_rank()
    # x = c.rank
    # c.set_rank('9')
    # c.rank = '9'