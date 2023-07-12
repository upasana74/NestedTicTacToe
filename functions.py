import random

# CONSTANTS
PLAYER_NAMES = ["Nobody", "X", "O"] 

# FUNCTIONS
def player_name(player_id):
    '''return the name of a player given their ID. (ID for X = 1, ID for O = 2)
    
    Parameters
    ----------
    player_id: int
        player's id, which is an index into PLAYER_NAMES list
        
    Returns
    -------
    string
        the player's name (eg, X, O)
    '''
    return PLAYER_NAMES[player_id]

def display_board(board):
    '''displays the current state layout of the individual tic tac toe instances/boards
    1 | 2 | 3
    4 | 5 | 6
    7 | 8 | 9
    Numbers are replaced by players' names once they move. 
    Iterate through the board and choose the right thing
    to display for each cell.
    
    Parameters
    ----------
    board: list
        The list representing the current state of the board. Each item in the list corresponds
        to a space on the board.
        
    Returns
    -------
    None
    '''
    board_to_show = "" # string that will display the board, starts empty
    for i in range(len(board)):
        if board[i] == 0: # 0 means unoccupied
            # displayed numbers are one greater than the board index
            board_to_show += str(i + 1) # display cell number
        else:
            board_to_show += player_name(board[i]) # display player's mark
        if (i + 1) % 3 == 0: # every 3 cells, start a new row
            board_to_show += "\n"
        else:
            board_to_show += " | " # within a row, divide the cells
    print()
    print(board_to_show)
    
def check_win_horizontal(board):
    '''checks a board to see if there is any horizontal row being
    fully occupied by the same player
    checks if all the 3 spaces of any row of the board is occupied 
    by the same player.
    
    Parameters
    ----------        
    board: list
        The list representing the current state of the board.
        
    Returns
    -------
    int
        the player ID corresponding to the player that fully 
        occupies a row, i.e 1 for Player 'X', 2 for player 'O'
        and 0 when nobody has fully occupied a row.
    '''
    if (board[0] != 0 and 
        board[0] == board[1] and 
        board[0] == board[2]):
        return board[0]
    if (board[3] != 0 and
        board[3] == board[4] and 
        board[3] == board[5]):
        return board[3]
    if (board[6] != 0 and
        board[6] == board[7] and 
        board[6] == board[8]):
        return board[6]
    return 0

def check_win_vertical(board):
    '''checks a board to see if there is any vertical column being
    fully occupied by the same player
    checks if all the 3 spaces of any column of the board is occupied 
    by the same player.
    
    Parameters
    ----------        
    board: list
        The list representing the current state of the board.
        
    Returns
    -------
    int
        the player ID corresponding to the player that fully 
        occupies a column, i.e 1 for Player 'X', 2 for player 'O'
        and 0 when nobody has fully occupied a column.
    '''
    if (board[0] != 0 and
        board[0] == board[3] and
        board[0] == board[6]):
        return board[0]
    if (board[1] != 0 and 
        board[1] == board[4] and 
        board[1] == board[7]):
        return board[1]
    if (board[2] != 0 and 
        board[2] == board[5] and 
        board[2] == board[8]):
        return board[2]
    return 0

def check_win_diagonal(board):
    '''checks a board to see if any of the 2 diagonals is being
    fully occupied by the same player
    checks if all the 3 spaces of any diagonal of the board is occupied 
    by the same player.
    
    Parameters
    ----------        
    board: list
        The list representing the current state of the board.
        
    Returns
    -------
    int
        the player ID corresponding to the player that fully 
        occupies a diagonal, i.e 1 for Player 'X', 2 for player 'O'
        and 0 when nobody has fully occupied a diagonal.
    '''
    if (board[0] != 0 and
        board[0] == board[4] and
        board[0] == board[8]):
        return board[0]
    if (board[2] != 0 and
        board[2] == board[4] and
        board[2] == board[6]):
        return board[2]
    return 0

def check_win(board):
    '''checks a board to see if there's a winner
    delegates to functions that check horizontally, vertically, and 
    diagonally to see if there is a winner. Returns the first winner
    found in the case of multiple winners.
    
    Parameters
    ----------        
    board: list
        The list representing the current state of the board.
        
    Returns
    -------
    int
        the player ID of the winner. 0 means no winner found.
    '''
    winner = check_win_horizontal(board)
    if (winner != 0):
        return winner
    
    winner = check_win_vertical(board)
    if (winner != 0):
        return winner
    
    return check_win_diagonal(board)

def next_player(current_player):
    '''determines who goes next
    given the current player ID, returns the ID of the next player.
    
    Parameters
    ----------        
    current_player: int
        The ID of the current player.
        
    Returns
    -------
    int
        the id of the player to go next
    '''
    return 2 if current_player == 1 else 1

def display_meta_board(meta_board):
    '''display the current state of the meta-board
    1 | 2 | 3    | |    1 | 2 | 3    | |    1 | 2 | 3
    4 | 5 | 6    | |    4 | 5 | 6    | |    4 | 5 | 6
    7 | 8 | 9    | |    7 | 8 | 9    | |    7 | 8 | 9
    --------------------------------------------------
    --------------------------------------------------
    1 | 2 | 3    | |    1 | 2 | 3    | |    1 | 2 | 3
    4 | 5 | 6    | |    4 | 5 | 6    | |    4 | 5 | 6
    7 | 8 | 9    | |    7 | 8 | 9    | |    7 | 8 | 9
    --------------------------------------------------
    --------------------------------------------------
    1 | 2 | 3    | |    1 | 2 | 3    | |    1 | 2 | 3
    4 | 5 | 6    | |    4 | 5 | 6    | |    4 | 5 | 6
    7 | 8 | 9    | |    7 | 8 | 9    | |    7 | 8 | 9
    The function iterates over each row and column of the meta-board and
    prints out the current state of each individual board in the meta-board.
    
    Parameters
    ----------
    meta_board: list
        the meta-board to display
        
    Returns
    -------
    None
    '''
    for i in range(0, 9, 3):
        # For each row of meta boards
        for row in range(3):
            # Print one row from each meta board
            row_to_print = ""
            for j in range(i, i + 3):
                row_to_print += ' | '.join(str(row * 3 + k + 1) if meta_board[j][row * 3 + k] == 0 else player_name(meta_board[j][row * 3 + k]) for k in range(3))
                if j != i + 2:  # If it's not the last board in the row
                    row_to_print += "    | |    "
            print(row_to_print)
        if i < 6:  # Don't print a line after the last row
            print('--------------------------------------------------')
            print('--------------------------------------------------')
            
def display_which_board_to_play():
    '''displays the board numbers of the meta-board
    board 1   ||   board 2   ||   board 3
    ==========||=============||==========
    board 4   ||   board 5   ||   board 6
    ==========||=============||==========
    board 7   ||   board 8   ||   board 9
    This function displays the board numbers of the meta-board to guide the
    players about the board layout for playing their moves.
    
    Parameters
    ----------
    None
    
    Returns
    -------
    None
    '''
    board_nums = [f'board {i+1}' for i in range(9)]
    print('\n==========||=============||==========\n'.join(['   ||   '.join(board_nums[i:i+3]) for i in range(0, 9, 3)]))

def get_valid_position(board, player, player_dict):
    '''returns a valid position for a player on the given board
    This function asks the player for a position on the board. If the player is a computer,
    the function selects a random position from the empty cells. For a human player, the function
    continues asking for a position until a valid one is provided.
    
    Parameters
    ----------
    board: list
        the board on which to play
    player: int
        the id of the player (1 = X, 2 = O)
    player_dict: dict
        a dictionary mapping player names to their types ('y' for human, 'n' for computer)
        
    Returns
    -------
    int
        the valid position selected by the player
    '''
    # Start an infinite loop to keep asking for valid position until one is found.
    while True:
        #if computer option  selected, computer randomly selects from the unfilled positions, it does not consider the filled positions
        if player_dict[player_name(player)] == "n": 
            # Get a list of empty cells.
            empty_cells = [i for i in range(1, 10) if board[i-1] == 0]
            if not empty_cells:  # if the list is empty, break the loop.
                break
            # Select a random position from the list of empty cells.
            pos = int(random.choice(empty_cells))
            print(f"{player_name(player)}'s chosen position (played by computer) is: {pos}")
            print("\n")
            return pos
        # If the player is a human, they will be asked to provide a position till a valid position is entered
        else:
            while True:
                pos = input(f"Player {player_name(player)}, enter the position you want to play at (1-9): ")
                if pos.isnumeric() and 1 <= int(pos) <= 9:
                    pos = int(pos)
                    print('\n')
                    break
                else:
                    print('\n')
                    print("Invalid position. Please enter a position between 1 and 9.")
            # Check if the selected position on the board is empty, if empty go ahead, otherwise inform the user to choose a different position.
            if board[pos-1] == 0:
                return pos
            else:
                print("This position is already filled. Please choose a different position.")

def check_draw(board):
    '''checks a board to see if all positions have been filled
    
    Parameters
    ----------        
    board: list
        the board to check
        
    Returns
    -------
    bool
        True if the board is filled. False if there are still open spots.
    '''
    return all(space != 0 for space in board)
