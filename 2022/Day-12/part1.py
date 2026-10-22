import heapq
from string import ascii_lowercase
from time import sleep

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

grid = []
with open("input.txt", "r") as f:
    for line in f.readlines():
        grid.append([ascii_lowercase.index(c) if c in ascii_lowercase else c for c in line.strip()])

height = len(grid)
width = len(grid[0])

marked = [[False for _ in range(width)] for _ in range(height)]
f = [[float('inf') for _ in range(width)] for _ in range(height)]
g = [[float('inf') for _ in range(width)] for _ in range(height)]
h = [[0 for _ in range(width)] for _ in range(height)]

for i, line in enumerate(grid):
    for j, c in enumerate(line):
        if c == "S":
            line[j] = 0
            start = (i, j)
        if c == "E":
            line[j] = 25
            dest = (i, j)

f[start[0]][start[1]] = 0
g[start[0]][start[1]] = 0
h[start[0]][start[1]] = 0

def print_marked():
    for line in marked:
        for b in line:
            if b:
                print("#", end="")
            else:
                print(".", end="")
        print()

def a_star():
    hq = [(0, *start)]
    k = 0
    while hq:
        k += 1
        _, i, j = heapq.heappop(hq)

        if marked[i][j]:
            continue
        marked[i][j] = True

        for di, dj in directions:
            ni, nj = i + di, j + dj

            if not(0 <= ni < height and 0 <= nj < width):
                continue

            if grid[ni][nj] - grid[i][j] > 1:
                continue

            if marked[ni][nj]:
                continue

            if (ni, nj) == dest:
                return g[i][j] + 1

            new_g = g[i][j] + 1
            new_h = abs(ni - dest[0]) + abs(nj - dest[1])
            new_f = new_g + new_h
            if new_f < f[ni][nj]:
                f[ni][nj] = new_f
                g[ni][nj] = new_g
                h[ni][nj] = new_h

                heapq.heappush(hq, (new_f, ni, nj))
    return -1

print(a_star())