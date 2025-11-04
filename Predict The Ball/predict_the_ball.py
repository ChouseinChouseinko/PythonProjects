from random import shuffle


def shuffle_list(mylist):
    shuffle(mylist)
    return mylist


def player_bet():
    bet_amount = input("How much you will bet? ")
    return int(bet_amount)


def player_guess():
    guess = ''
    while guess not in ['0', '1', '2']:
        guess = input("Pick a number from 0 to 2: ")
    return int(guess)


def check_guess(mylist, guess, bet_amount):
    if mylist[guess] == 'O':
        print("Correct, you are lucky")
        print(f"You won: {bet_amount * 2}$")
    else:
        print("Good luck in next round ")
        print(mylist)


while True:
    print("\n--- 🎲 Welcome to 'Find the Ball' Game! 🎲 ---")

    # INITIAL LIST
    mylist = ['', 'O', '']

    # SHUFFLE LIST
    mixedup_list = shuffle_list(mylist)

    # USER STAKE
    bet_amount = player_bet()

    # USER GUESS
    guess = player_guess()

    # CHECK GUESS
    check_guess(mixedup_list, guess, bet_amount)

    # ASK IF PLAYER WANTS TO PLAY AGAIN
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again not in ['yes', 'y']:
        print("Thanks for playing! 👋")
        break
