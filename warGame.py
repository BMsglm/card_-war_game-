'''
Main file!!
'''
from card import Card
from deck import Deck
from player import Player

def fill_deck(deck_obj):
    '''
    Fills up the empty list with cards in a deck object.

    Args:
        deck_obj(obj) : Any object (instance) from deck class.

    Returns:
        None (By default functions with no return value will return None)

    '''
    #Card features.
    suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
    ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
    values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

    #Make the cards and fill up the deck with cards.
    for num in range(4):
         for rank in ranks:
            card = Card(suits[num],ranks[num],values[rank])
            deck_obj.take_card(card)

def winner_check(player1,player2):
    '''
    Checks if there is any winner. And displays who won!

    Args:
        player1: Any player object.
        player2: Any player object.

    Returns:
        int: 1 if someone has won, 0 if no one has won yet.
    '''
    #if player 1 or 2 have the amount of cards that goes to zero or negative there is a winner! 
    if len(player1.cards) <=0 or len(player2.cards) <=0:
        winner_who(player1)
        return 1
    else:
        return 0
    
def winner_who(player1):
    '''
    Displays who is the winner.

    Args:
        player1: Any player object.

    Returns:
        None
    '''
    #If player 1 has negative amount of cards, player 1 has won, else player 2 has won.
    if len(player1.cards) <=0:
        print('Player 1 wins!!')
    else:
        print('Player 2 wins!!')


def card_selection(player):
    '''
    Displays the options, and asks for selection.

    Args:
        player(obj): Any player object.
    
    Returns:
        card(obj): Player's chosen card.
    '''

    print('Player 1 has',len(player.cards),'cards. They include :')
    player.display_deck()
    return player.choose_card()
    

def main():
    #Generate players.
    player1 = Player([])
    player2 = Player([])

    #Make the object table deck.
    deck_table = Deck()

    #Make an additional table deck, where in war this deck will store the cards.
    table_deck = Deck()

    #fill_deck.
    fill_deck(deck_table)

    #shuffle deck.
    deck_table.shuffle_deck()

    #distribute the cards half of each to player.
    for i in range(int(deck_table.size/2)):
        player1.take_card(deck_table.put_card())
        player2.take_card(deck_table.put_card())

    gameOn = True

    while gameOn:
        #check if someone win.
        if(winner_check(player1,player2)):
            gameOn = False
            break

        #Ask each player for selection.
        print("Player 1's Turn\n\n")
        choice_first = card_selection(player1)
        print("Player 2's Turn\n\n")
        choice_second = card_selection(player2)
        
        #When 1st player won
        if(choice_first.value > choice_second.value):
            print('\nPlayer 1 takes the card', choice_second.suit,choice_second.rank,'from player 2.')
            player1.take_card(player2.put_card())
        #When 2st player won
        elif(choice_first.value < choice_second.value):
            print('\nPlayer 2 takes the card', choice_first.suit,choice_second.rank,'from player 1.')
            player2.take_card(player1.put_card())
        #WAR!
        else:
            print('\n\nWAR!!\n\n')
            #Take cards from users to put on table
            print('Player 1 choose your cards to put on Table :')
            for i in range(2):
                choice_first = card_selection(player1)
                if(winner_check(player1,player2)):
                    gameOn=False
                    break
                deck_table.take_card(player1.put_card(choice_first))
            print('Player 2 choose your card to Put on Table :')
            for i in range(2):
                choice_second = card_selection(player2)
                if(winner_check(player1,player2)):
                    gameOn=False
                    break
                deck_table.take_card(player2.put_card(choice_second))
            #Go into war!
            war = True
            while war:
                if(winner_check(player1,player2)):
                    gameOn=False
                    break

                #Ask each player for selection.
                print('Player 1 choose your card to win those card on the table.')
                choice_first = card_selection(player1)
                print('Player 2 choose your card to win those card on the table.')
                choice_second = card_selection(player2)
                
                #If still in war continue to take new cards from each player.
                if choice_first.value == choice_second.value:
                    continue

                #Else give all the cards on the table to winning player.
                else:
                    #When 1st player won
                    if(choice_first.value > choice_second.value):
                        #Give all the cards to winning player
                        for i in range(len(table_deck.cards)):
                            print('Player takes the card', table_deck.cards[-1].suit,table_deck.cards[-1].rank,'from the table')
                            player1.take_card(table_deck.put_card())

                    #When 2st player won
                    else:
                        #Give all the cards to winning player
                        for i in range(len(table_deck.cards)):
                            print('Player takes the card', table_deck.cards[-1].suit,table_deck.cards[-1].rank,'from the table')
                            player2.take_card(table_deck.put_card())
                    #The war has ended.
                    war = False

if __name__ == "__main__":
    main()

