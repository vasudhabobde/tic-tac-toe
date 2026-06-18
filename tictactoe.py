import random

def print_board(board):
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:
            print("---------")

def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

def computer_move(board):
    empty_cells = get_empty_cells(board)
    return random.choice(empty_cells)

def is_valid_move(board, row, col):
    return 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " "

def play_tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"  # Human

    print("Welcome to Tic-Tac-Toe (You = X, Computer = O)!")
    print_board(board)

    while True:
        if current_player == "X":
            # Human player
            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter column (0-2): "))
            except ValueError:
                print("Please enter valid integers (0-2).")
                continue

            if not is_valid_move(board, row, col):
                print("Invalid move! Try again.")
                continue

        else:
            # Computer player
            row, col = computer_move(board)
            print(f"Computer plays at ({row}, {col})")

        # Make the move
        board[row][col] = current_player
        print_board(board)

        # Check for winner
        if check_winner(board, current_player):
            if current_player == "X":
                print("🎉 You won!")
            else:
                print("🤖 Computer won!")
            break

        # Check for draw
        if is_board_full(board):
            print("🤝 It's a draw!")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    play_tic_tac_toe()