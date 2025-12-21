import re
from collections import deque

direction_letters = ["U", "R", "D", "L"]
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)] # ^, >, v, <

# direction, number of tiles
directions_list = []

current_height, current_width = 0, 0
height_values, width_values = [0], [0]
with open("input.txt", "r") as f:
    for line in f.readlines():
        direction = direction_letters.index(line[0])
        value = int(re.search(r"\d+", line).group())

        ci, cj = directions[direction]
        current_height += ci * value
        current_width += cj * value

        height_values.append(current_height)
        width_values.append(current_width)

        directions_list.append((direction, value))

height = max(height_values) - min(height_values) + 3
width = max(width_values) - min(width_values) + 3
start_i = -min(height_values) + 1
start_j = -min(width_values) + 1

board = [[False for _ in range(width)] for _ in range(height)]

i, j = start_i, start_j
for direction, value in directions_list:
    di, dj = directions[direction]
    for k in range(value):
        i += di
        j += dj
        board[i][j] = True

filled = set()
q = deque([(0, 0)])
while q:
    i, j = q.pop()
    if not board[i][j] and not (i, j) in filled:
        filled.add((i, j))
        for i_dir, j_dir in directions:
            new_i = i + i_dir
            new_j = j + j_dir
            if not (new_i < 0 or new_i >= len(board) or new_j < 0 or new_j >= len(board[0])):
                q.append((new_i, new_j))

print(height * width - len(filled))