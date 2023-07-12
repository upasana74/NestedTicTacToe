import random
from functions import *



def main():
    
    # Display the layouts of the meta Tic tac toe board and individual instances for the user
    print("This is the layout for each instance/board within the meta Tic Tac Toe board!")
    print("Make your selections of which board to play accordingly!\n")
    display_which_board_to_play()
    print('\n')
    print("This is the layout of each individual board, choose the positions you want to play accordingly! \n")
    display_board([0,0,0,0,0,0,0,0,0])
    print('\n')
    
    # CONSTANTS
    
    # Defining player names
    PLAYER_NAMES = ["Nobody", "X", "O"] 

    # Requesting user for inputs (whether X, O should be played by human or computer) until it is a valid input 'y', 'n'
    valid_responses = ['y', 'n']
    player_x = input(str(f"Do you want {player_name(1)} to be played by user(human) or computer(random)? Type 'y' for human and 'n' for computer: "))
    while player_x not in valid_responses:
        print('\n')
        print("Invalid input. Please type 'y' for human and 'n' for computer.")
        player_x = input(f"Do you want {player_name(1)} to be played by user(human) or computer(random)? Type 'y' for human and 'n' for computer: ")

    player_o = input(f"Do you want {player_name(2)} to be played by user(human) or computer(random)? Type 'y' for human and 'n' for computer: ")
    while player_o not in valid_responses:
        print('\n')
        print("Invalid input. Please type 'y' for human and 'n' for computer.")
        player_o = input(f"Do you want {player_name(2)} to be played by user(human) or computer(random)? Type 'y' for human and 'n' for computer: ")

    # maintain a dict to save whether X, O should be played by humans or computer{"X": y/n, "O": y/n}, y->human, n->computer
    player_dict = {"X": player_x, "O": player_o}

    # Initialize the individual boards and the meta board
    board = [0] * 9 #individual instance(eg. board1) = [0,0,0,0,0,0,0,0,0]
    boards = [board.copy() for _ in range(9)] #board = [[board1], [board2], ..., [board9]]
    meta_board = board.copy()
    
    # Player X always starts a meta game, meta winner is always nobody as default at the start
    player = 1
    meta_winner = 0

    # Main game loop
    while meta_winner == 0:
        display_meta_board(boards)
        while True:
            # Player chooses which board to play on
            if player_dict[player_name(player)] == "n":
                # If the player chooses 'n' option (computer control), choose a board randomly
                which_board = random.choice([i for i in range(9) if check_win(boards[i]) == 0])
                print(f"Player {player_name(player)}'s chosen board(played by computer) is: {which_board + 1}")
            else:
                # If the player chose 'y' option(human play), ask for input
                while True:
                    board_int_or_not = input(f"Player {player_name(player)}, which board do you want to play on? (1-9): ")
                    if board_int_or_not.isnumeric() and 1 <= int(board_int_or_not) <= 9:
                        board_int_or_not = int(board_int_or_not)
                        break
                    else:
                        print('\n')
                        print("Invalid position. Please enter a position between 1 and 9.")
                which_board = board_int_or_not - 1


            # Check if the chosen board is already won/tied, ask the player to choose again
            if check_win(boards[which_board]) != 0:
                print("This board has already been won. Please choose a different board.")
                print('\n')
            else:
                break

        # Player chooses which position to play on the selected board
        position = get_valid_position(boards[which_board], player, player_dict)
        boards[which_board][position-1] = player

        # Check if the game has been won and update the boards accordingly
        winner = check_win(boards[which_board])
        if winner != 0:  # If the game has been won
            boards[which_board] = [winner] * 9  # Update the winning board with the winner's sign
            meta_board[which_board] = winner  # Update the meta board with the winner
            display_meta_board(boards)
            print(f'Player {player_name(winner)} has won the board {which_board + 1}!')
            print('\n')
        elif not any(move == 0 for move in boards[which_board]):  # If the board is a draw
            boards[which_board] = [0] * 9  # Reset the board for the next round
            print("The board is a draw. It will be reset for the next round.")
        
        # Check the status of the meta game
        meta_winner = check_win(meta_board)
        if meta_winner != 0:
            print('Meta game over!', player_name(meta_winner), 'wins the meta game!')
        elif check_draw(meta_board):
            print('Meta game over! It\'s a draw.')
            break
        else:
            player = next_player(player)


if __name__ == "__main__":
    main()
