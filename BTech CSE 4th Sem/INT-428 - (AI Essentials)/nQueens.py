# very simple N-Queens (4 Queens)

N = 4
board = [-1] * N # board[row] = column of queen

def is_safe(row, col) :
    for i in range(row):
        # Same column
        if board[i] == col:
            return False
        # Diagonal check
        if abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve(row):
    if row == N:
        return True
    for col in range(N):
        if is_safe(row, col):
            board[row] = col
            if solve(row + 1):
                return True
            board[row] = -1 # BackTrack
    return False

solve(0)

# Print solution
for i in range(N):
    for j in range(N):
        if board[i] == j:
            print("Q", end = " ")
        else:
            print(".", end=" ")
    print()