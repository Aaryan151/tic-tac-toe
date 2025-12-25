# Tic Tac Toe Game (Python)

board = [' ' for _ in range(9)]

def print_board():
    print()
    print(board[0], '|', board[1], '|', board[2])
    print('--+---+--')
    print(board[3], '|', board[4], '|', board[5])
    print('--+---+--')
    print(board[6], '|', board[7], '|', board[8])
    print()

def check_win(player):
    win_conditions = [
        (0,1,2), (3,4,5), (6,7,8),  # rows
        (0,3,6), (1,4,7), (2,5,8),  # columns
        (0,4,8), (2,4,6)            # diagonals
    ]
    for a, b, c in win_conditions:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

def is_board_full():
    for cell in board:
        if cell == ' ':
            return False
    return True

current_player = 'X'

print("=== TIC TAC TOE GAME ===")

while True:
    print_board()
    move = input(f"Player {current_player}, enter position (1-9): ")

    if not move.isdigit():
        print("Invalid input! Enter a number.")
        continue

    position = int(move) - 1

    if position < 0 or position > 8 or board[position] != ' ':
        print("Invalid move! Try again.")
        continue

    board[position] = current_player

    if check_win(current_player):
        print_board()
        print(f"Player {current_player} wins!")
        break

    if is_board_full():
        print_board()
        print("It's a tie!")
        break

    current_player = 'O' if current_player == 'X' else 'X'
