'''
Player will have own cards and a deck. Which will inherit the Deck class. Unlike deck player can won or lose. And have an option to choose a card.
'''
from deck import Deck
class Player(Deck):

    #Not working
    def take_card(self,card):
        self.cards.append(card)
        self.size += 1
    
    #Not working
    def put_card(self,card = None):
        #if no card specified take from back.
        if card == None:
            index = -1
        #else find the index and pop from there.
        else:
            index = self.cards.index(card)
        
        self.size -= 1
        return self.cards.pop(index)

    def display_deck(self):
        acc = 0
        for i in range(len(self.cards)-1):
            print('[',acc+1,']', self.cards[acc].suit , self.cards[acc].rank)
            acc +=1
    
    def choice_validate(self,id):
        while id < 1 or id > len(self.cards):
          id = int(input("ERROR!!\nEnter your card choice (suit & rank)\nFor example 5 :"))
       
        #Return choice.
        return id
        
    #Taking choice from user.
    def choose_card(self):
        #Display player cards.
        self.display_deck()
        #Get the choice.
        card_id = int(input("Enter your card choice (index)\nFor example 2 :"))
        #Arranging the id for list.
        card_id -= 1
        #Validate the input.
        choice = self.choice_validate(card_id)
        #Card choice
        c_card = self.cards[choice]
        #Return choice card.
        return c_card
 
    
   
