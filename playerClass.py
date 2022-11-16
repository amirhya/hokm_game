class Player:
    # hand=[]
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.role = None
        self.teamMate=None

    def setRole(self, role):
        self.role=role

    def showHand(self):
        print(self.name + " hand:\n")
        for card in self.hand:
            print(str(card))
    def giveCard(self, card):
        self.hand.extend(card)


    def __str__(self):
        return self.name
