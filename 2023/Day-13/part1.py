boards = []
with open("input.txt", "r") as f:
    board = []
    line = next(f)
    while True:
        if line == "\n":
            boards.append(board)
            board = []
        else:
            board.append(line.strip())
        try:
            line = next(f)
        except StopIteration:
            boards.append(board)
            break

def symetry(line, position):
    length = min(position, len(line) - position)
    return line[position - length:position] == line[position:position + length][::-1]

def analysis(board):
    # Returns 0 if the symetry is on a line, and the position of the line, else 1 and the position of the column
    # Check all rows for all positions
    for j in range(1, len(board[0])):
        if all([symetry(board[k], j) for k in range(len(board))]):
            return 0, j
    # Check all columns at all positions
    for i in range(1, len(board)):
        if all([symetry([board[k][l] for k in range(len(board))], i) for l in range(len(board[0]))]):
                return 1, i

total = 0
for board in boards:
    coeff, value = analysis(board)
    total += 100 ** coeff * value
print(total)