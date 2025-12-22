from collections import deque

directions = [(-1, 0), (0, -1), (0, 1), (1, 0)] # ^, <, >, v
MEGA_STEPS = 131 + 65
STEPS = 65

old_board= []
with open("input.txt", "r") as f:
    for line in f.readlines():
        line = line.strip() * 3
        old_board.append(line.replace("S", "."))

board = []
for _ in range(3):
    for i in range(len(old_board)):
        board.append(old_board[i])

MOD = MEGA_STEPS % 2

def exploration(startpos, steps):
    q = deque([(*startpos, 0)])
    explored = set()
    while q:
        i, j, n = q.popleft()

        if (i, j) in explored or n == steps + 1:
            continue
        explored.add((i, j))

        for di, dj in directions:
            ni, nj = i + di, j + dj
            if not (ni < 0 or ni >= len(board) or nj < 0 or nj >= len(board[0])) and board[ni][nj] == ".":
                q.append((ni, nj, n + 1))
    return explored

explored_ = exploration((len(board) // 2, len(board) // 2), MEGA_STEPS)
even = (exploration((len(board) // 6, len(board) // 2), STEPS) |
        exploration((5 * len(board) // 6, len(board) // 2), STEPS) |
        exploration((len(board) // 2, len(board) // 6), STEPS) |
        exploration((len(board) // 2, 5 * len(board) // 6), STEPS))
odd = exploration((len(board) // 2, len(board) // 2), STEPS)

colors = ["\033[91m", "\033[92m", "\033[93m", "\033[94m", "\033[95m"]

t = 0
Xs = [0, 0, 0, 0]
for i in range(len(board)):
    for j in range(len(board[0])):
        if (i, j) in explored_ and (i + j) % 2 == MOD:
            t += 1
            if (i, j) in even:
                #orange
                print('\033[93m', end="")
                Xs[0] += 1
            elif (i, j) in odd:
                # green
                print('\033[92m', end="")
                Xs[1] += 1
            elif (len(old_board) <= i < 2 * len(old_board) and len(old_board) <= j < 2 * len(old_board)
                or (i < len(old_board) and not(len(old_board) <= j < 2 * len(old_board)))
                or (i >= 2 * len(old_board) and not(len(old_board) <= j < 2 * len(old_board)))):
                # purple
                print('\033[95m', end="")
                Xs[2] += 1
            else:
                #blue
                print('\033[94m', end="")
                Xs[3] += 1
            print("█\033[0m", end="")
        else:
            print(board[i][j] + "\033[0m", end="")
    print()

print(Xs)
print(t)