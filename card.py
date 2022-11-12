class Card:
    def __init__(self, value, sign):
        self.value = value
        self.sign = sign

    def __str__(self):
        return (f"{self.value} __of__ {self.sign}")

    ##TODO: Understand __eg__
    def __eq__(self, other):
        bool(other.value == self.value and other.sign == self.sign)


