boards = []
with open("input.txt", "r") as f:
    board = []
    line = next(f)
    while True:
        if line == "\n":
            boards.append(board)
            board = []
        else:
            board.append([x == "#" for x in line.strip()])
        try:
            line = next(f)
        except StopIteration:
            boards.append(board)
            break

def symetry(line, position):
    length = min(position, len(line) - position)
    return line[position - length:position] == line[position:position + length][::-1]

def analysis(board, smudge=(True, -1)):
    # Returns 0 if the symetry is on a line, and the position of the line, else 1 and the position of the column
    # Check all rows for all positions
    for j in range(1, len(board[0])):
        if all([symetry(board[k], j) for k in range(len(board))]):
            if not(smudge == (0, j)):
                return (0, j)
    # Check all columns at all positions
    for i in range(1, len(board)):
        if all([symetry([board[k][l] for k in range(len(board))], i) for l in range(len(board[0]))]):
            if not(smudge == (1, i)):
                return (1, i)

total = 0
for board in boards:
    smudge = analysis(board)
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] = not board[i][j]
            a = analysis(board, smudge)
            if not a == None:
                coeff, value = a
                total += 100 ** coeff * value
                break
            board[i][j] = not board[i][j]
        else:
            continue
        break
print(total)