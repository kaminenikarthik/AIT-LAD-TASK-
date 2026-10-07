def is_safe(board, row, col, n):
    # Check column
    for i in range(row):
        if board[i] == col:
            return False

    # Check diagonals
    for i in range(row):
        if abs(board[i] - col) == abs(i - row):
            return False

    return True

def solve_n_queens(board, row, n):
    if row == n:
        print(board)
        return True

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col

            if solve_n_queens(board, row + 1, n):
                return True

            board[row] = -1

    return False

n = 4
board = [-1] * n

solve_n_queens(board, 0, n)
