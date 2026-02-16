board = [" "] * 9


def print_board():
    print()
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-+-+-")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-+-+-")
    print(board[6] + "|" + board[7] + "|" + board[8])
    print()


def check_winner(player):
    win_positions = [
        [0,1,2], [3,4,5], [6,7,8],   # rows
        [0,3,6], [1,4,7], [2,5,8],   # columns
        [0,4,8], [2,4,6]             # diagonals
    ]

    for pos in win_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] == player:
            return True
    return False


def is_draw():
    return " " not in board


current_player = "X"

while True:
    print_board()
    move = int(input(f"Player {current_player}, choose position (1-9): ")) - 1

    if board[move] == " ":
        board[move] = current_player
    else:
        print("Position taken! Try again.")
        continue

    if check_winner(current_player):
        print_board()
        print(f"🎉 Player {current_player} wins!")
        break

    if is_draw():
        print_board()
        print("It's a draw!")
        break

    current_player = "O" if current_player == "X" else "X"