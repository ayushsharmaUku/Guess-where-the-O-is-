def display_game(game_list):
    print('|' + (game_list[1] + '|' + game_list[2] + '|' + game_list[
        3] + '|') + '-----Position list: ' + '1' + '|' + '2' + '|' + '3')

    print('-----' + '-----')

    print('|' + (game_list[4] + '|' + game_list[5] + '|' + game_list[
        6] + '|') + '--------------------' + '4' + '|' + '5' + '|' + '6')

    print('-----' + '-----')

    print('|' + (game_list[7] + '|' + game_list[8] + '|' + game_list[
        9] + '|') + '--------------------' + '7' + '|' + '8' + '|' + '9')


def player_sym():
    player1 = ''
    player2 = ''
    while player1 not in ['X', 'O']:
        player1 = input('Player1 do you want to be "X" or "O":').upper()
        if player1 not in ['X', 'O']:
            print('Please choose a valid input!! ')
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    return player1, player2


def choose_posi1():
    position = ''
    position_range = range(1, 10)
    within_range = False

    while position.isdigit() == False or within_range == False:

        position = input('Player 1, Choose a position from 1 to 9:')

        if position.isdigit() == False:
            print('Please enter a number only')

        if position.isdigit() == True:
            if int(position) in position_range:

                within_range = True
            else:
                within_range = False

                print('Please choose a number within range')
    return int(position)


def choose_posi2():
    position = ''
    position_range = range(1, 10)
    within_range = False

    while position.isdigit() == False or within_range == False:

        position = input('Player 2, Choose a position from 1 to 9:')

        if position.isdigit() == False:
            print('Please enter a number only')

        if position.isdigit() == True:
            if int(position) in position_range:

                within_range = True
            else:
                within_range = False

                print('Please choose a number within range')
    return int(position)

def cont():
    choice = ''
    while choice not in ['Y','N']:
        choice  = input('Would you like to continue: ').upper()
        if choice not in ['Y','N']:
            print('Please enter answer only in "Y" or "N"!!!')
        else:
            pass
    return choice

def correct_row(game_list,player):
    if (game_list[1]==player and game_list[2]==player and game_list[3]==player) or (game_list[4]==player and game_list[5]==player and game_list[6]==player) or (game_list[7]==player and game_list[8]==player and game_list[9]==player) or (game_list[1]==player and game_list[4]==player and game_list[7]==player) or (game_list[2]==player and game_list[5]==player and game_list[8]==player) or (game_list[3]==player and game_list[6]==player and game_list[9]==player) or (game_list[1]==player and game_list[5]==player and game_list[9]==player) or (game_list[3]==player and game_list[5]==player and game_list[7]==player):
        return player


gameon = True
game = ['', '1', '2', '3', '4', '5', '6', '7', '8', '9']
while gameon == True:
    # display initial game
    display_game(game)
    print('\n', '\n')

    player1, player2 = player_sym()
    print(f'Player 1 is : {player1}')
    print(f'Player 2 is : {player2}')
    print('\n')

    while player1 == 'X' or player1 == 'O':

        # ask player 1 to position

        player1_position = choose_posi1()
        game[player1_position] = player1

        print('\n')

        display_game(game)
        print('\n')
        print(f'Player 1 is : {player1}')
        print(f'Player 2 is : {player2}')
        print('\n', '\n')

        winner = correct_row(game, player1)

        if winner == player1:
            print('PLAYER 1 is the winner!!')

            continue_playing = cont()
            if continue_playing == 'Y':
                gameon = True
            else:

                gameon = False
                break

        player2_position = choose_posi2()
        game[player2_position] = player2
        display_game(game)
        print(f'Player 1 is : {player1}')
        print(f'Player 2 is : {player2}')
        print('\n')

        winner = correct_row(game, player2)
        if winner == player2:
            print('PLAYER 1 is the winner!!')

            display_game(game)

            continue_playing = cont()
            if continue_playing == 'Y':
                gameon = True

            else:
                gameon = False
                break

gameon = False

