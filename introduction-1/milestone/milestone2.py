game_on = True
game_list = [0, 1, 2]

test_board = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X']

def clear_outpu():
    print('\n'*100)

def display_game(game_list):
    print('Here is the current list: ')
    print(game_list)

def position_choice():
    choice = 'wrong'

    while choice not in ['0', '1', '2']:
        choice = input('Pick a position (0,1,2): ')

        if choice not in ['0', '1', '2']:
            print('Sorry, invalid choice!')

    return int(choice)

def replacement_choice(game_list, position):
    user_placement = input("Type a string to place at position: ")
    game_list[position] = user_placement
    return game_list

def gameon_choice():
    choice = 'wrong'

    while choice not in ['Y', 'N']:
        choice = input('Keep playing? (Y or N) ')

        if choice not in ['Y', 'N']:
            print("Sorry, invalid choice!")

    if choice == 'Y':
        return True
    else:
        return False
    
while game_on == True:
    display_game(game_list)
    position = position_choice()
    game_list = replacement_choice(game_list, position)
    display_game(game_list)
    game_on = gameon_choice()

clea

## 7,8,9
## 4,5,6
## 1,2,3