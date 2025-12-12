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

seen = set()
def bfs(i, j):
    if not (i, j) in seen:
        seen.add((i, j))
        piece_directions = [directions[i] for i in pipe_map[board[i][j]]]
        for i_dir, j_dir in piece_directions:
            new_i = i + i_dir
            new_j = j + j_dir
            bfs(new_i, new_j)

bfs(*startpos)

big_map = {"-": "...\n###\n...", "|": ".#.\n.#.\n.#.", "F": "...\n.##\n.#.", "7": "...\n##.\n.#.", "J": ".#.\n##.\n...", "L": ".#.\n.##\n..."}
big_board = []
for i in range(len(board)):
    bb_rows = [[], [], []]
    for j in range(len(board[0])):
        shape = (big_map[board[i][j]] if (i, j) in seen else "...\n...\n...").split('\n')
        for k in range(3):
            bb_rows[k].append(shape[k])
    for r in bb_rows:
        big_board.append(''.join(r))

is_outside = [[False for _ in range(len(big_board[0]))] for _ in range(len(big_board))]
def fill(i, j):
    if not big_board[i][j] == "#" and not is_outside[i][j]:
        is_outside[i][j] = True
        for i_dir, j_dir in directions:
            new_i = i + i_dir
            new_j = j + j_dir
            if not (new_i < 0 or new_i >= len(big_board) or new_j < 0 or new_j >= len(big_board[0])):
                fill(new_i, new_j)
fill(0, 0)

total = 0
for i in range(1, len(big_board), 3):
    for j in range(1, len(big_board[0]), 3):
        if not is_outside[i][j]:
            total += 1
print(total - len(seen))