from math import inf
import sys

sys.setrecursionlimit(pow(2, 31) - 1)

start_piece = "|"
directions = [(-1, 0), (0, -1), (0, 1), (1, 0)] # ^, <, >, v
pipe_map = {"-": (1, 2), "|": (0, 3), "F": (2, 3), "7": (1, 3), "J": (0, 1), "L": (0, 2)}

board, startpos = [], None
with open("input.txt", "r") as f:
    for i, line in enumerate(f):
        line = line.strip()
        for j, char in enumerate(line):
            if not startpos and char == "S":
                startpos = (i, j)
        board.append(line.replace("S", start_piece))

distances = [[inf for _ in range(len(board[0]))] for _ in range(len(board))]
def bfs(i, j, d):
    if distances[i][j] > d:
        distances[i][j] = d
        piece_directions = [directions[i] for i in pipe_map[board[i][j]]]
        for i_dir, j_dir in piece_directions:
            new_i = i + i_dir
            new_j = j + j_dir
            bfs(new_i, new_j, d + 1)
bfs(*startpos, 0)

print(max(max([x for x in row if x != inf] + [0]) for row in distances))