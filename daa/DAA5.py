
def safe(board, row, col, n):

    # Check column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve(board, row, n):

    if row == n:
        return True

    for col in range(n):

        if safe(board, row, col, n):

            board[row][col] = 1

            if solve(board, row + 1, n):
                return True

            board[row][col] = 0

    return False


n = 4
board = [[0] * n for _ in range(n)]

# First queen at row 0, column 1
board[0][1] = 1

if solve(board, 1, n):
    print("Solution:")
    for row in board:
        print(row)
else:
    print("Solution does not exist")
