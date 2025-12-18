from collections import deque
from tqdm import tqdm

with open("input.txt", "r") as f:
    board = [line.strip() for line in f.readlines()]

directions = [(-1, 0), (0, -1), (0, 1), (1, 0)] # ^, <, >, v

height = len(board)
width = len(board[0])

def find_energized_tiles(s_i, s_j, s_d):
    visited = set()
    energized = set()
    queue = deque([(s_i, s_j, s_d)])

    while queue:
        i, j, d = queue.pop()
        if not (i < 0 or i >= height or j < 0 or j >= width) and not (i, j, d) in visited:
            visited.add((i, j, d))
            energized.add((i, j))

            i_dir, j_dir = directions[d]
            normal_new_i = i + i_dir
            normal_new_j = j + j_dir
            match board[i][j]:
                case ".":
                    queue.append((normal_new_i, normal_new_j, d))
                case "/":
                    new_d = [2, 3, 0, 1][d]
                    i_dir, j_dir = directions[new_d]
                    new_i = i + i_dir
                    new_j = j + j_dir

                    queue.append((new_i, new_j, new_d))
                case "\\":
                    new_d = [1, 0, 3, 2][d]
                    i_dir, j_dir = directions[new_d]
                    new_i = i + i_dir
                    new_j = j + j_dir

                    queue.append((new_i, new_j, new_d))
                case "|":
                    if d in [0, 3]:
                        queue.append((normal_new_i, normal_new_j, d))
                    else:
                        queue.append((i - 1, j, 0)) 
                        queue.append((i, j, 3))
                case "-":
                    if d in [1, 2]:
                        queue.append((normal_new_i, normal_new_j, d))
                    else:
                        queue.append((i, j - 1, 1))
                        queue.append((i, j, 2))

    return energized

max_total = 0
for i in tqdm(range(height)):
    # ->
    max_total = max(max_total, len(find_energized_tiles(i, 0, 2)))
    # <-
    max_total = max(max_total, len(find_energized_tiles(i, width - 1, 1)))
for j in tqdm(range(width)):
    # v
    max_total = max(max_total, len(find_energized_tiles(0, j, 3)))
    # ^
    max_total = max(max_total, len(find_energized_tiles(height - 1, j, 0)))
print(max_total)