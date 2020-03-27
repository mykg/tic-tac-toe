import os
import random

# to create a board
def display_board(board):
    os.system("clear") #clear the screen
    #print('\n' * 100) #on other IDE
    print(board[9]+"|"+board[8]+"|"+board[7])
    print(board[6]+"|"+board[5]+"|"+board[4])
    print(board[1]+"|"+board[2]+"|"+board[3])


def player_turn():
    random


# assignment of markers
def player_input():
        marker = ''
        while not (marker == 'X' or marker == 'O'):
            marker = input("Player 1 X or O? ").upper()

        if marker == 'X':
            return ('X','O') #player1marker = 'X' n player2marker = 'O'
        else:
            return ('O','X') #player2marker = 'O' n player1marker = 'X'


# a random function to choose random player to go first
def choose_player():
    if random.randint(1,2) == 1:
        return 'Player 1'
    else:
        return 'Player 2'


# a fun that check free space
def space_check(board,position):
    return board[position] == ' '


# a function that asks position
def ask_position(board):
    position = 0
    if position not in range(1,10) or not space_check(board,position):
        position = int(input("choose a position(1-9) : "))

    return position


# a fun to place marker 
def place_marker(board,position,marker):
    board[position] = marker


# to check if a player has won
def win(board,mark):

    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[1] == mark and board[5] == mark and board[9] == mark) or
            (board[7] == mark and board[5] == mark and board[3] == mark) or
            (board[7] == mark and board[4] == mark and board[1] == mark) or
            (board[8] == mark and board[5] == mark and board[2] == mark) or
            (board[9] == mark and board[6] == mark and board[3] == mark))


# a fun to check tie
def tie(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True 


# a fun to ask for replay
def replay():
    return input("Play again (y/n)").lower().startswith('y')


# the real game starts here
while True:

    theboard = [' ']*10 # reset the board
    (player1_marker,player2_marker) = player_input() # assign the marker to players
    turn = choose_player()
    print(turn + ' will go first')

    play_game = input("Ready to play (y/n)")
    if play_game.lower() == 'y':
        game = True
    else:
        game = False


    while game:

        if turn == 'Player 1':

            #display the board
            display_board(theboard)
            #ask position and also check free space at that position
            position = ask_position(theboard)
            #place marker at above position
            place_marker(theboard,position,player1_marker)

            if win(theboard,player1_marker):
                display_board(theboard)
                print("Player 1 has won")
                game = False
            else:
                if tie(theboard):
                    display_board(theboard)
                    print("TIE")
                else:
                    turn = "Player 2"

        else:

            #display the board
            display_board(theboard)
            #ask position and also check free space at that position
            position = ask_position(theboard)
            #place marker at above position
            place_marker(theboard,position,player2_marker)

            if win(theboard,player1_marker):
                display_board(theboard)
                print("Player 2 has won")
                game = False
            else:
                if tie(theboard):
                    display_board(theboard)
                    print("TIE")
                else:
                    turn = "Player 1"

            

    if not replay():
        break
