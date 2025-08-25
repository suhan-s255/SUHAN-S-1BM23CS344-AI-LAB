board = [['-', '-', '-'],
         ['-', '-', '-'],
         ['-', '-', '-']]

def print_board():
    for row in board:
        print(row)

def check_winner(player):
    for row in board:
        if all(spot == player for spot in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def play_game():
    print_board()
    for turn in range(9):
        player = 'X' if turn % 2 == 0 else 'O'
        print(f"enter position to place {player}:")
        row = int(input()) - 1
        col = int(input()) - 1
        if board[row][col] == '-':
            board[row][col] = player
            print_board()
            if check_winner(player):
                print(f"{player} wins")
                print("Game Over")
                return
        else:
            print("Invalid move, try again")
            continue
    print("It's a draw")
    print("Game Over")

play_game()
