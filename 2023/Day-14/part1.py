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

roll_north(board)
print(load(board))