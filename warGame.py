'''
Main file!!
'''
from card import Card
from deck import Deck
from player import Player


gameOn = True

def fill_deck(deck_fnc):
    #Card features.
    suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
    ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
    values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

    #Make the card and fill up the deck with cards.
    for num in range(4):
         for rank in ranks:
            card = Card(suits[num],ranks[num],values[rank])
            deck_fnc.take_card(card)

#Taking choice from user.
def player_choice(player):
    #Display player cards.
    
    
    #Get the choice.
    choice = input("Enter your card choice :")

    #Validate the input.
    choice = validate_choice(player,choice)

    #Return choice
    return choice

def validate_choice(player, choice):
    #While choice is not in player cards ask again.
    
    while choice not in player.cards:
        choice = input("ERROR!!\nEnter your card choice :")
        ###
        ### Need to find a way to validate !!!
        ###
    return choice

def main():
    #Generate players.
    player1 = Player()
    player2 = Player()

    #Make the object table deck.
    deck_table = Deck()

    #fill_deck.
    fill_deck(deck_table)

    #shuffle deck.
    deck_table.shuffle_deck()

    #distribute the cards half of each to player.
    for i in range(int(deck_table.size/2)):
        player1.take_card(deck_table.put_card())
        player2.take_card(deck_table.put_card())

    while gameOn:
        #Ask each player for their choice of card.
        choice_one = player_choice(player1)
        choice_two = player_choice(player2)

        print("First choice is {0}, Second choice is : {1}".format(choice_one,choice_two))

        #1st Condition (When 1st player won)
        if():
            None

        #2nd Condition (When 2st player won)
        elif():
            None

        #3rd Condition (WAR!)
        else:
            None



if __name__ == "__main__":
    main()