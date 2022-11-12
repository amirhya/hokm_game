import card
import random
import player
##### 314159265

#comment1
#comment2
class Game:
    def __init__(self):
        self.deck = []
        self.createDeck()
        self.players = []
        self.hakem = None


    def createDeck(self):
        #This
        SUITS = ['H', 'C', 'D', 'S']
        RANKS = ['K', 'Q', 'J', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        self.deck=[card.Card(rank, suit) for suit in SUITS for rank in RANKS]

    def joinPlayer(self, player):

        self.players.append(player)

    def show_players(self):
        for player in (self.players):
            print(str(player)) #=str(k)

    def __str__(self):
        #This means that when executing str(game) it prints cards in the deck
        for card in self.deck:
            print(card, sep=' ')

    def shuffle(self, count):

        hand = []
        for i in range(count):
            k = random.randint(0, len(self.deck)-1)
            card = self.deck.pop(k)  ## removes
            hand.append(card)
        return hand
    def shuffleDeck(self):
        ##write code to rearrange deck (shuffle the deck)
        self.createDeck() ##TODO: check for later
        random.shuffle(self.deck)



    def getCards(self, count):
        hand = [self.deck.pop(i) for i in range(count)]
        return hand



    def get_hand(self, card_list, player):
        player.hand.extend(card_list)

    def remove_card(self, card):
        self.cards.remove(card)

    def set_hokm(self, sign):
        self.hokm = sign

    def get_hokm(self):
        return self.hokm


    # for first round
    def findHakem(self):
        self.createDeck()
        self.shuffleDeck()
        while self.hakem == None:
            for player in self.players:
                card = self.shuffle(1)[0]
                if str(card).split('__')[0] == 'Ace':
                    print(str(player) + " is hakem")
                    player.set_hakem()
                    break
        dealer = hakem_inddex - 1

    def arrangePlayers(self, player):
        pass

    def giveToken(self,player):
        pass

    def getPlayers(self):
        return self.players


if __name__ == '__main__':

    game = Game()
    game.shuffleDeck()
    # for card in game.deck:
    #     print(card)
    hand=game.getCards(4)
    for card in hand:
        print(card)
    print(len(game.deck))
    # game flow

    # Do this once at the start of the game
    # housekeeping: Arrange players
    # find hakem
    # find hakem's teammate
    # find dealer's teammate
    # find dealer (is the person to the right of the Hakem, AKA, index hakem - 1)
    # datastructure to encapsulate players arrangement



    # Find Hokm
    # arrange seats

    # game = Game()  ## this will instantiate the game by creating 52 card objects of a complete deck of cards
    #
    #
    # game.joinPlayer(player.Player("ghasem"))
    # print(str(game.players[0]))
    # game.joinPlayer(player.Player("james"))
    # game.joinPlayer(player.Player("Xantia"))
    # game.joinPlayer(player.Player("Pegut"))
    # game.show_players()
    #game.players[1].giveCard(game.shuffle(1)[0])

    ##TODO: find hakem, find his teammate, and the dealer

    ##Show me the deck
   #
   # str(game.)

    ##TODO HOKM Gameflow: Dealer Rules
    # first_hand = True
    # if first_hand:
    #     for i in range(5):
    #         game.players[1].giveCard(game.shuffle(3))
    #     first_hand = False
    # game.players[1].show_hand()

    #cards_list = game.shuffle(3)
    #
    # cards_list1 = game.shuffle(5)
    #
    # game.get_hand(cards_list, game.players[1])
    # game.get_hand(cards_list1, game.players[2])
    # game.players[1].show_hand()
    # game.players[2].show_hand()

