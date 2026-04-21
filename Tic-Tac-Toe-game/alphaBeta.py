
board = [' ' for _ in range(9)]

# Print board
def print_board():
    for i in range(0, 9, 3):
        print(board[i], '|', board[i+1], '|', board[i+2])
        print('--+---+--')


def check_winner(b, player):
    win_positions = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for combo in win_positions:
        if b[combo[0]] == player and b[combo[1]] == player and b[combo[2]] == player:
            return True
    return False

def is_draw():
    return ' ' not in board

def minimax_alpha_beta(is_maximizing, alpha, beta):
    if check_winner(board, 'O'):
        return 1
    if check_winner(board, 'X'):
        return -1
    if is_draw():
        return 0

    if is_maximizing:
        best_score = -1000
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax_alpha_beta(False, alpha, beta)
                board[i] = ' '

                if score > best_score:
                    best_score = score

                if best_score > alpha:
                    alpha = best_score

                if beta <= alpha:
                    break   

        return best_score

    else:
        best_score = 1000
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax_alpha_beta(True, alpha, beta)
                board[i] = ' '

                if score < best_score:
                    best_score = score

                if best_score < beta:
                    beta = best_score

                if beta <= alpha:
                    break   

        return best_score


def best_move():
    best_score = -1000
    move = -1

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax_alpha_beta(False, -1000, 1000)
            board[i] = ' '

            if score > best_score:
                best_score = score
                move = i

    return move


def play_game():
    while True:
        print_board()

        # Player move
        move = int(input("Enter position (0-8): "))
        if board[move] != ' ':
            print("Invalid move!")
            continue

        board[move] = 'X'

        if check_winner(board, 'X'):
            print_board()
            print("You win!")
            break

        if is_draw():
            print_board()
            print("Draw!")
            break

        
        comp_move = best_move()
        board[comp_move] = 'O'

        if check_winner(board, 'O'):
            print_board()
            print("Computer wins!")
            break

        if is_draw():
            print_board()
            print("Draw!")
            break


play_game()