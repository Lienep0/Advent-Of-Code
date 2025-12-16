board = []
with open("input.txt", "r") as f:
    for line in f.readlines():
        board.append([x for x in line.strip()])

def load(board):
    total = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "O":
                total += len(board) - i
    return total

def print_board(board):
    for x in board:
        print(''.join(x))
    print()

def roll_north(board):
    positions = [0 for _ in range(len(board[0]))]
    for i in range(len(board)):
        for j in range(len(board[0])):
            match board[i][j]:
                case "#":
                    positions[j] = i + 1
                case "O":
                    board[i][j] = "."
                    board[positions[j]][j] = "O"
                    positions[j] += 1

def roll_south(board):
    positions = [len(board) - 1 for _ in range(len(board[0]))]
    for i in range(len(board) - 1, -1, -1):
        for j in range(len(board[0])):
            match board[i][j]:
                case "#":
                    positions[j] = i - 1
                case "O":
                    board[i][j] = "."
                    board[positions[j]][j] = "O"
                    positions[j] -= 1

def roll_west(board):
    positions = [0 for _ in range(len(board))]
    for j in range(len(board[0])):
        for i in range(len(board)):
            match board[i][j]:
                case "#":
                    positions[i] = j + 1
                case "O":
                    board[i][j] = "."
                    board[i][positions[i]] = "O"
                    positions[i] += 1

def roll_east(board):
    h = []
    positions = [len(board[0]) - 1 for _ in range(len(board))]
    for j in range(len(board[0]) - 1, -1, -1):
        for i in range(len(board)):
            match board[i][j]:
                case "#":
                    positions[i] = j - 1
                case "O":
                    board[i][j] = "."
                    board[i][positions[i]] = "O"
                    h.append((i, positions[i]))
                    positions[i] -= 1
    return tuple(h)

def cycle(board):
    roll_north(board)
    roll_west(board)
    roll_south(board)
    return roll_east(board)

def cycles(board, n=1):
    cache = {}
    for k in range(n):
        positions = cycle(board)
        if positions in cache:
            for _ in range((n - (k + 1)) % (k - cache[positions])):
                cycle(board)
            return
        else:
            cache[positions] = k

cycles(board, 1_000_000_000)
print(load(board))