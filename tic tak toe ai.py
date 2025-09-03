board = [" " for _ in range(9)]

def print_board(board):
    print("| {} | {} | {} |".format(board[0], board[1], board[2]))
    print("| {} | {} | {} |".format(board[3], board[4], board[5]))
    print("| {} | {} | {} |".format(board[6], board[7], board[8]))

def is_victory(ox):
    for i in range(3):
        if board[i*3] == ox and board[i*3+1] == ox and board[i*3+2] == ox:
            return True
    for i in range(3):
        if board[i] == ox and board[i+3] == ox and board[i+6] == ox:
            return True
    if (board[0] == board[4] == board[8] == ox) or (board[2] == board[4] == board[6] == ox):
        return True
    return False

def is_draw():
    return " " not in board

def minimax(board, is_maximizing):
    if is_victory("O"):
        return 1
    if is_victory("X"):
        return -1
    if is_draw():
        return 0

    if is_maximizing:  # AI's turn
        best_score = -999
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, False)
                board[i] = " "
                best_score = max(best_score, score)
        return best_score
    else:  # Human's turn
        best_score = 999
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, True)
                board[i] = " "
                best_score = min(best_score, score)
        return best_score

def ai_move():
    best_score = -999
    move = 0
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    board[move] = "O"

# Game loop
while True:
    print_board(board)
    move = int(input("X make a move (0-8): "))
    if board[move] != " ":
        continue
    board[move] = "X"

    if is_victory("X"):
        print_board(board)
        print("X won!")
        break
    elif is_draw():
        print_board(board)
        print("Draw!")
        break

    ai_move()

    if is_victory("O"):
        print_board(board)
        print("O won!")
        break
    elif is_draw():
        print_board(board)
        print("Draw!")
        break
