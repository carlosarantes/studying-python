import random

suits = ( "Hearts", "Diamonds", "Spades", "Clubs" )
ranks = ( "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",  "Jack", "Queen", "King", "Ace" )
values = {'Two':2, 'Three':3, 'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':11,'Queen':12,'King':13,'Ace':14}

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit
    
class Deck:
    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

class Player:
    def __init__(self, name):
        self.name = name
        self.all_cards = []
    
    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards) 

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards'
    

# GAME SETUP
player_one = Player('One')   
player_two = Player('Two')

new_deck = Deck()
new_deck.shuffle()

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on = True
round_num = 0
    # while at_war

while game_on:
    round_num += 1
    print(f'Round: {round_num}')

    if len(player_one.all_cards) == 0:
        print('Player 1, out of cards! Player 2 Wins!')
        game_on = False
        break

    if len(player_two.all_cards) == 0:
        print('Player 2, out of cards! Player 1 Wins!')
        game_on = False
        break

    player_one_cards = []
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    at_war = True

    while at_war:
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)

            at_war = False

        elif  player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)

            at_war = False

        else:
            print("WAAR!")

            if len(player_one.all_cards) < 3:
                print("Player one unable to declare war")
                print("PLAYER TWO WINS")
                game_on = False
                break

            elif len(player_two.all_cards) < 3:
                print("Player two unable to declare war")
                print("PLAYER ONE WINS")
                game_on = False
                break

            else:
                for num in range(3):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())