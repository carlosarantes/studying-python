game_on = True
game_board = [[7,8,9], # 0
              [4,5,6], # 1
              [1,2,3]] # 2

whos_turn = 'player_one'

## game_board = [['X',8,9], [4,'X',6], [1,2,'X']]
## -----------------------------------------------
players = {
    'player_one': { 'name': "", 'choice': "" },
    'player_two': { 'name': "", 'choice': "" }
}

def define_players():
    choice_one = ''
    players['player_one']['name'] = input("Please player one, tell me your name: ")
    
    while choice_one not in ['X', 'O']:
        choice_one = input(f'Please {players['player_one']['name']} do you want to be X or O ?')
        if choice_one not in ['X', 'O']:
            print('This choice is not valid... please choose X or O (uppercase)')

    players['player_two']['name'] = input('Please player two, tell me your name: ')
    
    players['player_one']['choice'] = choice_one
    players['player_two']['choice'] = 'X'

    if players['player_one']['choice'] == 'X':
        players['player_two']['choice'] = 'O'

    print('\n********** WELCOME TO THE TICTAC-TOE **********')
    print(f'Dear players {players['player_one']['name']} and {players['player_two']['name']}, keep in mind the positions of the game -->')

    for line in game_board:
        print(line)


def display_game():
    for line in game_board:
        print('|', end='')

        for item in line:
            value = item
            if item not in ['X', 'O']:
                value = ' '

            print(value + '|', end='')

        print('\n---------')

def end_turn(whos_turn):
    if whos_turn == 'player_one':
        whos_turn = 'player_two'
    else:
        whos_turn = 'player_one'

    return whos_turn

def play_input(game_board):
    choice = 'w'

    while choice.isdigit() not in range(1, 10):
        choice = input(f'Please {players[whos_turn]['name']}, tell me the position youwant to fill in (1 to 9): ')

    choice = int(choice)

    column = 0
    if choice % 3 == 0:
        column = 2
    else:
        column = (choice % 3) - 1
    
    row = 0
    if choice in range(1,4):
        row = 2
    elif choice in range(4,7):
        row = 1

    game_board[row][column] = players[whos_turn]['choice']
    return game_board

def game_check():
    choice_winner = ''

    if game_board[0][0] == game_board[0][1] == game_board[0][2]:
        choice_winner = game_board[0][0]

    if game_board[1][0] == game_board[1][1] == game_board[1][2]:
        choice_winner = game_board[1][0]

    if game_board[2][0] == game_board[2][1] == game_board[2][2]:
        choice_winner = game_board[2][0]
    
    ## -------------------------------------------
    if game_board[0][0] == game_board[1][0] == game_board[2][0]:
        choice_winner = game_board[0][0]

    if game_board[0][1] == game_board[1][1] == game_board[2][1]:
        choice_winner = game_board[0][1]
    
    if game_board[0][2] == game_board[1][2] == game_board[2][2]:
        choice_winner = game_board[0][2]
    ## -------------------------------------------
    if game_board[0][0] == game_board[1][1] == game_board[2][2]:
        choice_winner = game_board[0][0]
    
    if game_board[0][2] == game_board[1][1] == game_board[2][0]:
        choice_winner = game_board[0][2]

    if choice_winner != '':
        print(f'Player {players[whos_turn]['name']} WON... ')
        return False

    return True

define_players()
print('\n\n\n')

while game_on:
    display_game()
    game_board = play_input(game_board)
    game_on = game_check()
    whos_turn = end_turn(whos_turn)