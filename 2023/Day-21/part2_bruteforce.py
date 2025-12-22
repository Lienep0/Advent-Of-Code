from collections import deque

directions = [(-1, 0), (0, -1), (0, 1), (1, 0)] # ^, <, >, v

board, startpos = [], None
with open("input.txt", "r") as f:
    for i, line in enumerate(f):
        line = line.strip()
        for j, char in enumerate(line):
            if not startpos and char == "S":
                startpos = (i, j)
        board.append(line.replace("S", "."))

STEPS = 131 + 65
MOD = (startpos[0] + startpos[1] + STEPS) % 2

total = 0
q = deque([(*startpos, 0, 0, 0)])
explored = set()
while q:
    i, j, mi, mj, n = q.popleft()

    if (i, j, mi, mj) in explored or n == STEPS + 1:
        continue
    explored.add((i, j, mi, mj))

    if n % 2 == MOD:
        total += 1

    for di, dj in directions:
        ni = (i + di) % len(board)
        nj = (j + dj) % len(board[0])
        nmi = mi + ((i + di) // len(board))
        nmj = mj + ((j + dj) // len(board[0]))
        if board[ni][nj] == ".":
            q.append((ni, nj, nmi, nmj, n + 1))
print(total)