'''
Player will have own cards and a deck. Which will inherit the Deck class. Unlike deck player can won or lose. And have an option to choose a card.
'''
from deck import Deck
class Player(Deck):

    def take_card(self,card):
        self.cards.append(card)
        self.size += 1
    
    def put_card(self):
        self.cards.pop()
        self.size -= 1

    def choose_card(self):
        None