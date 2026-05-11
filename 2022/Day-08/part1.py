with open("input.txt", "r") as f:
    grid = [list(map(int, line.strip())) for line in f.readlines()]

height, width = len(grid), len(grid[0])
marked = [[False for _ in range(width)] for _ in range(height)]

for i in range(width):
    x, y = 0, i
    maximum_size_seen = -1
    while x < height:
        if grid[x][y] > maximum_size_seen:
            marked[x][y] = True
            maximum_size_seen = grid[x][y]
        x = x + 1

for i in range(width):
    x, y = height - 1, i
    maximum_size_seen = -1
    while x >= 0:
        if grid[x][y] > maximum_size_seen:
            marked[x][y] = True
            maximum_size_seen = grid[x][y]
        x = x - 1

for i in range(height):
    x, y = i, 0
    maximum_size_seen = -1
    while y < width:
        if grid[x][y] > maximum_size_seen:
            marked[x][y] = True
            maximum_size_seen = grid[x][y]
        y = y + 1

for i in range(height):
    x, y = i, width - 1
    maximum_size_seen = -1
    while y >= 0:
        if grid[x][y] > maximum_size_seen:
            marked[x][y] = True
            maximum_size_seen = grid[x][y]
        y = y - 1

total = 0
for i in range(height):
    for j in range(width):
        if marked[i][j]:
            total += 1

print(total)