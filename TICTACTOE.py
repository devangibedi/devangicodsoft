import math

# Define the symbols for players
AI = 'X'
HUMAN_PLAYER = 'O'
EMPTY_CELL = ' '

def printBoard(board):
    for row in board:
        print(' | '.join(row))
        print('---------')

def isWinner(board, player):
    # Check rows, columns, and diagonals for a winner
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    return all(board[i][j] != EMPTY_CELL for i in range(3) for j in range(3))

def evaluate_board(board):
    if isWinner(board, AI):
        return 1
    if isWinner(board, HUMAN_PLAYER):
        return -1
    return 0

def minimax(board, depth, maximizing_player):
    if isWinner(board, AI):
        return 1
    if isWinner(board, HUMAN_PLAYER):
        return -1
    if is_full(board):
        return 0

    if maximizing_player:
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY_CELL:
                    board[i][j] = AI
                    eval = minimax(board, depth + 1, False)
                    board[i][j] = EMPTY_CELL
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY_CELL:
                    board[i][j] = HUMAN_PLAYER
                    eval = minimax(board, depth + 1, True)
                    board[i][j] = EMPTY_CELL
                    min_eval = min(min_eval, eval)
        return min_eval

def find_best_move(board):
    best_eval = -math.inf
    best_move = None

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY_CELL:
                board[i][j] = AI
                eval = minimax(board, 0, False)
                board[i][j] = EMPTY_CELL
                if eval > best_eval:
                    best_eval = eval
                    best_move = (i, j)

    return best_move

def main():
    board = [[EMPTY_CELL for _ in range(3)] for _ in range(3)]

    print("Tic Tac Toe - AI vs Human")
    printBoard(board)

    while True:
        # AI move
        ai_move = find_best_move(board)
        board[ai_move[0]][ai_move[1]] = AI

        print("AI's Move:")
        printBoard(board)

        if isWinner(board, AI):
            print("AI wins!")
            break

        if is_full(board):
            print("It's a draw!")
            break

        # Human move
        while True:
            row, col = map(int, input("Enter row (0-2) and column (0-2) for your move: ").split())
            if board[row][col] == EMPTY_CELL:
                board[row][col] = HUMAN_PLAYER
                break
            else:
                print("Invalid move. Try again.")

        printBoard(board)

        if isWinner(board, HUMAN_PLAYER):
            print("You win!")
            break

        if is_full(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()
