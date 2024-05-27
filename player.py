'''
Player will have own cards and a deck. Which will inherit the Deck class. Unlike deck player can won or lose. And have an option to choose a card.
'''
from deck import Deck
class Player(Deck):

    def __init__(self,cards):
        self.cards = cards
        self.size = 0
 
    def choice_validate(self,id):
        '''
        Validates if the chosen id meet the requirement of the player's deck.

        Args:
            id(int): Input integer from user.
        Returns:
            id(int): Returns the id that met the requirements.
        '''
        while id < 1 or id > len(self.cards):
          id = int(input("\n !!INPUT ERROR!! \nYour choice must be an integer from your deck!\nFor example: 4\n\nEnter your card choice :"))
        #Return choice.
        return id
        
    #Taking choice from user.
    def choose_card(self):
        '''
        Takes an input for a card choice.

        Args:
            ...
        Returns
            card(obj): The card that user selected.
        '''
        #Get the choice.
        card_id = int(input("\nEnter your card choice :"))
        #Validate the input.
        choice = self.choice_validate(card_id)
        #Card choice. (Choice -1 because of indexing rules.)
        return self.cards[choice-1]
    