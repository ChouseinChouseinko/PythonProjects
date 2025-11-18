# Project 1 - Tic Tac Toe
from IPython.display import clear_output
import random
# STEP1


def display_board(board):
    clear_output()
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])

# STEP2


def player_input():
    marker = ''
    # ask from player 1 to choose X or O
    while marker != 'X' and marker != 'O':
        marker = input('Player 1, Choose X or O: ').upper()
    player1 = marker

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

# STEP3


def place_marker(board, marker, position):
    board[position] = marker

# STEP4


def win_check(board, mark):
    # 3 ways to check: rows,columns and 2 diagonals
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top\n",
            # across the middle\n",
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            # across the bottom\n",
            (board[1] == mark and board[2] == mark and board[3] == mark) or
            # down the middle\n",
            (board[7] == mark and board[4] == mark and board[1] == mark) or
            # down the middle\n",
            (board[8] == mark and board[5] == mark and board[2] == mark) or
            # down the right side\n",
            (board[9] == mark and board[6] == mark and board[3] == mark) or
            # diagonal\n",
            (board[7] == mark and board[5] == mark and board[3] == mark) or
            # diagonal"
            (board[9] == mark and board[5] == mark and board[1] == mark))

# STEP 5
# Randomly choose which player will start first


def choose_first():
    flip = random.randint(0, 1)

    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

# Step 6
# empty place


def space_check(board, position):
    return board[position] == ' '


# Step 7
# If the table is full

def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True  # board is full if we return true

# Step 8


def player_choice(board):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Choose a position: (1-9)'))
    return position

# Step9 replay


def replay():
    choice = input("Play again ? Enter Yes or No")
    return choice == 'Yes'


print('Welcome to Tic-Tac-Toe Game')
while True:

    the_board = [' ']*10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn+' will go first')

    play_game = input('Ready to play? y or n: ')

    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player1_marker, position)
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('Player 1 won')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Tie Game')
                    game_on = False
                else:
                    turn = 'Player 2'
        else:
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player2_marker, position)
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('Player 2 won')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Tie Game')
                    game_on = False
                else:
                    turn = 'Player 1'

    if not replay():
        break
