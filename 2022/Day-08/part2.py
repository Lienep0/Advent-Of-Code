# up left down right
dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]

with open("input.txt", "r") as f:
    grid = [list(map(int, line.strip())) for line in f.readlines()]

height, width = len(grid), len(grid[0])

def explore(x, y):
    total = 1
    for x_d, y_d in dirs:
        c_x, c_y = x, y
        current = 0
        minimum_height = -1
        maximum_height = grid[x][y]

        while True:
            n_x, n_y = c_x + x_d, c_y + y_d
            if not(0 <= n_x < height and 0 <= n_y < width):
                break
            current += 1
            if not(minimum_height < grid[n_x][n_y] < maximum_height):
                break
            c_x, c_y = n_x, n_y

        total *= current
    return total

best = 0
for i in range(height):
    for j in range(width):
            best = max(best, explore(i, j))

print(best)