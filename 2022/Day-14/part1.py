min_x, max_x, min_y, max_y = 500, 500, 0, 0

rocks = []
with open("input.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        coords = []
        for pair in line.split(" -> "):
            x, y = map(int, pair.split(","))
            min_x = min(min_x, x)
            max_x = max(max_x, x)
            min_y = min(min_y, y)
            max_y = max(max_y, y)
            coords.append((x, y))
        rocks.append(coords)

grid = [[0 for _ in range(min_x, max_x + 1)] for _ in range(min_y, max_y + 1)]

def print_grid():
    for i, row in enumerate(grid):
        print(f"{min_y + i: 3} " + "".join([".", "#", "o"][x] for x in row))

for rock in rocks:
    for i in range(len(rock) - 1):
        x, y = rock[i]
        nx, ny = rock[i + 1]
        grid[y - min_y][x - min_x] = 1
        if x == nx:
            step = 1 if ny > y else -1
            for k in range(y, ny, step):
                grid[k - min_y][x - min_x] = 1
        else:
            step = 1 if nx > x else -1
            for k in range(x, nx, step):
                grid[y - min_y][k - min_x] = 1
    lx, ly = rock[-1]
    grid[ly - min_y][lx - min_x] = 1

def move_sand(y, x):
    # Moves the sand until it can't anymore
    # Returns 0 and places the sand if the sand stopped moving, 1 if it moved, 2 if it fell
    if y == len(grid) - 1:
        return False

    if grid[y + 1][x] == 0:
        return move_sand(y + 1, x)
    if grid[y + 1][x - 1] == 0:
        return move_sand(y + 1, x - 1)
    if grid[y + 1][x + 1] == 0:
        return move_sand(y + 1, x + 1)
    
    grid[y][x] = 2
    return True

s = 0
while move_sand(0, 500 - min_x):
    s += 1
print_grid()
print(f"Number of fallen grains: {s}")