"""
This file



------------------------------------------
classes

"""
import cardClass
import random
import playerClass




SUITS = ['H', 'C', 'D', 'S']
RANKS = ['K', 'Q', 'J', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10']
ROLES = ["Hakem", "Hakem's teammate", "dealer's teammate", "dealer"]


class Game:
    def __init__(self, team1="Team 1", team2=" Team 2"):
        self.deck = []
        self.createDeck()

        self.players = []
        self.roles = {ROLES[0]: None, ROLES[1]: None, ROLES[2]: None, ROLES[3]: None}
        self.priorities = {ROLES[0]: 0, ROLES[1]: 2, ROLES[2]: 3, ROLES[3]: 4}
        self.scoresRound = {team1: 0, team2: 0}
        self.scoresTotal = {team1: 0, team2: 0}

    def getCardFromDeck(self, count, verbose=0):

        if verbose == 1 and count == 1:
            print("Getting " + str(count) + " number of cards from deck")
        hand = [self.deck.pop(card) for card in range(count)]
        return hand

    def findRolesTeams(self):
        ##Figures out who is Hakem, his teammate, dealer's teammate, and the dealer.
        print("Finding Roles")
        self.createDeck()
        self.shuffleDeck()
        idPlayer = 0
        idRole = 0
        pickedIds = []
        remainingIds = [0, 1, 2, 3]
        numRemainingPlayers = 4
        while not self.roles[ROLES[3]]:  # while dealer is not found
            card = self.getCardFromDeck(1, verbose=0)[0]
            if card.rank == 'A':
                player = self.players[remainingIds[idPlayer]]
                player.setRole(ROLES[idRole])
                self.roles[ROLES[idRole]] = player
                print(str(player) + " is " + ROLES[idRole])
                numRemainingPlayers = max(1, numRemainingPlayers - 1)
                idRole += 1
                remainingIds.pop(idPlayer)
            idPlayer = (idPlayer + 1) % numRemainingPlayers

    def setScores(self):
        pass

    def playRound(self):
        pass

    def playHand(self, player):
        pass
        # player.playHand()

    def createDeck(self):
        print("Creating Deck")
        self.deck = [cardClass.Card(rank, suit) for suit in SUITS for rank in RANKS]

    def joinPlayer(self, player):
        print(str(player) + "joined the game")
        self.players.append(player)

    def strPlayers(self):
        s = ""
        for player in self.players:
            s += str(player) + "\t"
        return s

    def __str__(self):
        # This means that when executing str(game) should return us a string value (we can print it later)
        s = "This is a Game of Hokm:...\n"
        s += "With the following players:\n"
        s += self.strPlayers()
        return s

    # def shuffle(self, count):
    #     hand = []
    #     for i in range(count):
    #         k = random.randint(0, len(self.deck)-1)
    #         card = self.deck.pop(k)  ## removes
    #         hand.append(card)
    #     return hand
    def shuffleDeck(self):
        ##write code to rearrange deck (shuffle the deck)
        # self.createDeck() ##TODO: check for later
        print("Shuffling deck...")
        random.shuffle(self.deck)

    def get_hand(self, card_list, player):
        player.hand.extend(card_list)

    def set_hokm(self, sign):
        self.hokm = sign

    def get_hokm(self):
        return self.hokm

    def giveCardsTo(self, player):
        pass

    # for first round

    # dealer = hakem_inddex - 1

    def arrangePlayers(self, player):
        pass

    def giveToken(self, player):
        pass

    def getPlayers(self):
        return self.players

    def roundWinner(self, ):

        return


if __name__ == '__main__':
    game = Game()
    game.joinPlayer(playerClass.Player("Amir"))
    game.joinPlayer(playerClass.Player("Sahand"))
    game.joinPlayer(playerClass.Player("David"))
    game.joinPlayer(playerClass.Player("Jamal"))

    print(str(game))
    game.findRolesTeams()
    # find hakem and team mates

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
    # game.players[1].giveCard(game.shuffle(1)[0])

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

# cards_list = game.shuffle(3)
#
# cards_list1 = game.shuffle(5)
#
# game.get_hand(cards_list, game.players[1])
# game.get_hand(cards_list1, game.players[2])
# game.players[1].show_hand()
# game.players[2].show_hand()
