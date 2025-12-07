from collections import deque

directions = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)] 
board = [list([0 if x == '@' else -1 for x in line.strip()]) for line in open("input.txt").readlines()]
height = len(board)
width = len(board[0])

to_remove = deque()

def neighbors(i, j):
    neighbor_list = []
    for direction in directions:
        i_dir, j_dir = direction
        new_i = i + i_dir
        new_j = j + j_dir

        if ((new_i >= 0 and new_i < height and new_j >= 0 and new_j < width) 
            and board[new_i][new_j] >= 0):
            neighbor_list.append((new_i, new_j))
    return neighbor_list

for i in range(height):
    for j in range(width):
        if board[i][j] >= 0:
            n = len(neighbors(i, j))
            board[i][j] = n
            if n < 4:
                to_remove.append((i, j))

total = 0
while len(to_remove) > 0:
    i, j = to_remove.popleft()

    if board[i][j] == -1:
        continue
    else:
        board[i][j] = -1
        total += 1

        for n_i, n_j in neighbors(i, j):
            board[n_i][n_j] -= 1
            if board[n_i][n_j] < 4:
                to_remove.append((n_i, n_j))

print(total)