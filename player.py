'''
Player will have own cards and a deck.
'''
from deck import Deck
class Player(Deck):

    def take_card(self,card):
        self.cards.append(card)
        self.size += 1
    
    def put_card(self):
        self.cards.pop()
        self.size -= 1