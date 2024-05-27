'''
A deck have cards in it. And can give shuffle put cards.
'''
import random
class Deck():
    #Deck will have its size, and carries cards.
    def __init__(self,cards =[]):
        self.cards = cards
        self.size = 0
    
    def display_deck(self):
        acc = 0
        for i in range(len(self.cards)):
            print('[',acc+1,']', self.cards[acc].suit , self.cards[acc].rank,'Value :',self.cards[acc].value)
            acc +=1

    #To shuffle the deck
    def shuffle_deck(self):
        random.shuffle(self.cards)

    #Give a card from deck
    def put_card(self,card = None):
        #if no card specified take from back.
        if card == None:
            index = -1
        #else find the index and pop from there.
        else:
            index = self.cards.index(card)
        
        self.size -= 1
        return self.cards.pop(index)
    
    #Put card into deck.
    def take_card(self,card):
        self.cards.append(card)
        self.size +=1
    

