class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return (f"{self.rank} __of__ {self.suit}")

    ##TODO: Understand __eg__
    def __eq__(self, other):
       return bool(other.rank == self.rank and other.suit == self.suit)


#https://docs.python.org/3/reference/datamodel.html#special-method-names