from sys import setrecursionlimit
setrecursionlimit(pow(2, 31) - 1)

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

board = []
with open("input.txt", "r") as f:
    for line in f.readlines():
        board.append(line.strip())

H, W = len(board), len(board[0])
visited = [[False for _ in range(W)] for _ in range(H)]

def print_board():
    for i in visited:
        print(["{:2}".format(x) if x else " 0" for x in i])

max_length = 0
def dfs(i, j, l):
    if (i, j) == (H - 1, W - 2):
        global max_length
        max_length = max(max_length, l)
        return

    visited[i][j] = True

    for di, dj in directions:
        ni, nj = i + di, j + dj
        if 0 <= ni < H and 0 <= nj < W:
            if not visited[ni][nj]:
                if (board[ni][nj] == "." 
                or (board[ni][nj] == "v" and di != -1)
                or (board[ni][nj] == ">" and dj != -1)):
                    dfs(ni, nj, l + 1)

    visited[i][j] = False

try:
    dfs(0, 1, 0)
    print(max_length)
except KeyboardInterrupt:
    print_board()