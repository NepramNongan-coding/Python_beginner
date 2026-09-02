def print_board(board):
    """Prints the current state of the game board."""
    print(f"\n {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")

def check_winner(board, player):
    """Checks if the current player has won the game."""
    # Define all 8 possible winning combinations (rows, columns, diagonals)
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Horizontal rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Vertical columns
        [0, 4, 8], [2, 4, 6]             # Diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def check_tie(board):
    """Checks if the board is completely full (a tie game)."""
    for spot in board:
        if spot != "X" and spot != "O":
            return False
    return True

def play_game():
    """Main function to control the Tic-Tac-Toe game loop."""
    # Initialize the board with position numbers 1-9
    board = [str(i) for i in range(1, 10)]
    current_player = "X"
    game_active = True

    print("Welcome to Tic-Tac-Toe!")
    print("To play, enter a number from 1 to 9 corresponding to the grid position.")

    while game_active:
        print_board(board)
        
        # Get and validate player input
        try:
            choice = int(input(f"Player {current_player}'s turn. Choose a position (1-9): "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 9.")
            continue

        # Adjust for 0-indexed list
        position = choice - 1

        # Check if the chosen move is within range and the spot isn't already taken
        if position < 0 or position > 8:
            print("Out of bounds! Choose a position from 1 to 9.")
        elif board[position] == "X" or board[position] == "O":
            print("That spot is already taken! Try another one.")
        else:
            # Place the player's marker
            board[position] = current_player

            # Check for win or tie states
            if check_winner(board, current_player):
                print_board(board)
                print(f"🎉 Congratulations! Player {current_player} wins! 🎉")
                game_active = False
            elif check_tie(board):
                print_board(board)
                print("🤝 It's a tie game!")
                game_active = False
            else:
                # Switch to the other player
                current_player = "O" if current_player == "X" else "X"

# Run the game
if __name__ == "__main__":
    play_game()