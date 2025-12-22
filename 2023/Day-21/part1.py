from collections import deque

directions = [(-1, 0), (0, -1), (0, 1), (1, 0)] # ^, <, >, v
STEPS = 200
STEPS = 65
MOD = 0

board, startpos = [], None
with open("input.txt", "r") as f:
    for i, line in enumerate(f):
        line = line.strip()
        for j, char in enumerate(line):
            if not startpos and char == "S":
                startpos = (i, j)
        board.append(line.replace("S", "."))

total = 0
q = deque([(*startpos, 0)])
explored = set()
while q:
    i, j, n = q.popleft()

    if (i, j) in explored or n == STEPS + 1:
        continue
    explored.add((i, j))

    if n % 2 == MOD:
        total += 1

    for di, dj in directions:
        ni, nj = i + di, j + dj
        if not (ni < 0 or ni >= len(board) or nj < 0 or nj >= len(board[0])) and board[ni][nj] == ".":
            q.append((ni, nj, n + 1))
print(total)

t = 0
for i in range(len(board)):
    for j in range(len(board)):
        if (i, j) in explored and (i + j) % 2 == MOD:
            t += 1
            print("X", end="")
        else:
            print(board[i][j], end="")
    print()
print(t)