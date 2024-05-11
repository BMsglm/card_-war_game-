'''
A deck will have cards in it.
'''
import random
class Deck():
    #Deck will have its size, and carries cards.
    def __init__(self,cards =[]):
        self.cards = cards
        self.size = 0
    
    #To shuffle the deck
    def shuffle_deck(self):
        random.shuffle(self.cards)

    #Put card into deck
    def take_card(self,card):
        self.cards.append(card)
        self.size +=1
    
    #Give a card from deck
    def put_card(self):
        self.cards.pop()
   
