board, startpos = [], None
with open("input.txt", "r") as f:
    for i, line in enumerate(f):
        line = line.strip()
        for j, char in enumerate(line):
            if not startpos and char == "S":
                startpos = (i, j)
        board.append(line.replace("S", "."))

print(26501365 // len(board), 26501365 % len(board))

print((2 * (26501365 // len(board)) + 1) ** 2)