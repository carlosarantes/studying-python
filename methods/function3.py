example = [1,2,3,4,5]

from random import shuffle

result = shuffle(example)

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

print( shuffle_list(example) )

my_list = [' ', 'o', ' ']

shuffle_list(my_list)

def player_guess():
    guess =  ''

    while guess not in ['0', '1', '2']:
        guess = input('Choose a number between 0,1,2:')
    return int(guess)


def check_guess(list, player_guess):
    if list[player_guess] == 'o':
        print('GREAT, YOU WON')
    else:
        print('LOSEEER, YOU OWN ME 20 EUROS :) ')
        print(list)

check_guess(my_list, player_guess())