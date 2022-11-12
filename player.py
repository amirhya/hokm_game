class Player:
    # hand=[]
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.is_hakem = False
        self.teamMate=None

    def show_hand(self):
        # return self.hand
        print("Hands of " + self.name + "*****")
        for card in self.hand:
            print(card.__str__())
    def giveCard(self, card):
        self.hand.extend(card)

    def set_hakem(self):
        self.is_hakem = True

    def __str__(self):
        return self.name
