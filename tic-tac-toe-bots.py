import random

def print_board(board):
    """Prints the current state of the board."""
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def check_winner(board, player):
    """Checks if the specified player has won."""
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontal
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Vertical
        (0, 4, 8), (2, 4, 6)              # Diagonal
    ]
    
    for combo in winning_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

def is_board_full(board):
    """Checks if the board is full."""
    return " " not in board

def get_available_moves(board):
    """Returns a list of available moves."""
    return [i for i in range(9) if board[i] == " "]

def bot_move(player, board):
    """Randomly selects an available move for the bot."""
    available_moves = get_available_moves(board)
    move = random.choice(available_moves) if available_moves else None
    return move

def play_game():
    """Main function to play the Tic Tac Toe game between two bots."""
    board = [" "] * 9
    current_player = "X"  # Bot X starts first

    while True:
        print_board(board)
        print(f"Player {current_player} is making a move...")
        
        move = bot_move(current_player, board)
        if move is not None:
            board[move] = current_player
        
            # Check for a winner
            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            
            # Check for a tie
            if is_board_full(board):
                print_board(board)
                print("It's a tie!")
                break
            
            # Switch players
            current_player = "O" if current_player == "X" else "X"
        else:
            print_board(board)
            print("No more moves available. It's a tie!")
            break

# Start the game
if __name__ == "__main__":
    play_game()