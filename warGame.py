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

    #Make the cards and fill up the deck with cards.
    for num in range(4):
         for rank in ranks:
            card = Card(suits[num],ranks[num],values[rank])
            deck_fnc.take_card(card)



def main():
    #Generate players.
    player1 = Player()
    player2 = Player()

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

    while gameOn:
        #Ask each player for their choice of card.
        choice_one = player1.choose_card()
        choice_two = player2.choose_card()
        
        #1st Condition (When 1st player won)
        if(choice_one.value > choice_two.value):
            print('Player 1 takes the card', player2.cards[-1].suit,player2.cards[-1].rank,'from player 2.')
            #Not working
            player1.take_card(player2.put_card())

        #2nd Condition (When 2st player won)
        elif(choice_one.value < choice_two.value):
            print('Player 2 takes the card', player1.cards[-1].suit,player1.cards[-1].rank,'from player 1.')
            #Not working
            player2.take_card(player1.put_card())

        #3rd Condition (WAR!)
        else:
            war = True
            while war:
                for i in range(2):
                    choice_one = player1.choose_card()
                    print('Choose your',i+1,'. Card to Put on Table :')
                    deck_table.take_card(player1.put_card(choice_one))
                for i in range(2):
                    choice_one = player2.choose_card()
                    print('Choose your',i+1,'. Card to Put on Table :')
                    deck_table.take_card(player2.put_card(choice_one))

                #Get a new choices from players.
                print('\nPlayer 1 chooses\n')
                choice_one = player1.choose_card()
                print('\nPlayer 2 chooses\n')
                choice_two = player2.choose_card()
                
                #If still in war continue
                if choice_one.value == choice_two.value:
                    continue
                #Else give all the cards on the table to winning player.
                else:
                    #1st Condition (When 1st player won)
                    if(choice_one.value > choice_two.value):
                        for i in range(len(table_deck.cards)):
                            print('Player takes the card', table_deck.cards[-1].suit,table_deck.cards[-1].rank,'from the table')
                            player1.take_card(table_deck.put_card())

                    #2nd Condition (When 2st player won)
                    elif(choice_one.value < choice_two.value):
                        for i in range(len(table_deck.cards)):
                            print('Player takes the card', table_deck.cards[-1].suit,table_deck.cards[-1].rank,'from the table')
                            player2.take_card(table_deck.put_card())
                    #Either way war has ended.
                    war = False
        
        #While game is on display how many cards players have.
        print('Player 1 has', len(player1.cards),'cards!')
        print('Player 2 has', len(player1.cards),'cards!')

if __name__ == "__main__":
    main()

