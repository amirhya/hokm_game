import card
import random
import player


class Game:
    def __init__(self):
        self.deck = []
        self.players = {}
        self.hakem = None
        SIGNS = ['heart', 'club', 'diamond', 'spade']
        VALUES = ['King', 'Queen', 'jack', 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10']

        for i in range(len(SIGNS)):
            for j in range(len(VALUES)):
                self.deck.append(card.Card(VALUES[j], SIGNS[i]))
    #def createDeck

    def joinPlayer(self, player):
        ##function
        if not self.players:
            self.players[1] = player
        else:
            self.players[max(list(self.players.keys())) + 1] = player

    def show_players(self):
        for k in (self.players):
            print(k.__str__())

    def __str__(self):
        for obj in self.cards:
            print(obj, sep=' ')

    def shuffle(self, count):
        sh_hand = []
        for i in range(count):
            k = random.randint(1, len(self.deck) - 1)
            q = self.deck.pop(k)  ## removes
            sh_hand.append(q)
        return sh_hand

    # def get_hand(self,card_list,player):
    #     for card in card_list:
    #         player.hand.append(card)

    def get_hand(self, card_list, player):
        player.hand.extend(card_list)

    def remove_card(self, card):
        self.cards.remove(card)

    def set_hokm(self, sign):
        self.hokm = sign

    def get_hokm(self):
        return self.hokm

    # for first round

    def findhakem(self):
        while self.hakem == None:
            for _, player in self.players.items():
                card = self.shuffle(1)[0]
                if card.__str__().split('__')[0] == 'Ace':
                    print(player.__str__() + " is hakem")
                    player.set_hakem()
                    break


if __name__ == '__main__':
    game = Game()  ## this will instantiate the game by creating 52 card objects of a complete deck of cards


    game.joinPlayer(player.Player("ghasem"))
    # game.joinPlayer(player.Player("james"))
    # game.joinPlayer(player.Player("Xantia"))
    # game.joinPlayer(player.Player("Pegut"))
    #game.players[1].giveCard(game.shuffle(1)[0])

    ##TODO: find hakem, find his teammate, and the dealer

    ##TODO HOKM Gameflow: Dealer Rules
    first_hand = True
    if first_hand:
        for i in range(5):
            game.players[1].giveCard(game.shuffle(3))
        first_hand = False
    game.players[1].show_hand()

    #cards_list = game.shuffle(3)
    #
    # cards_list1 = game.shuffle(5)
    #
    # game.get_hand(cards_list, game.players[1])
    # game.get_hand(cards_list1, game.players[2])
    # game.players[1].show_hand()
    # game.players[2].show_hand()

