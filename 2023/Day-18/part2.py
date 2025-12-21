import re

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] # >, v, <, ^

instructions = []
with open("input.txt", "r") as f:
    for line in f.readlines():
        direction = int(line[-3])
        value = int(re.search(r"\(.*\)", line).group()[2:-2], 16)
        instructions.append((direction, value))

i, j = 0, 0
coordinates = []
for k, (direction, value) in enumerate(instructions):
    di, dj = directions[direction]
    i += di * value
    j += dj * value
    coordinates.append((i, j))

def shoelace(points):
    n = len(points)
    area = 0

    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % n]
        area += (x1 * y2) - (y1 * x2)

    return abs(area) // 2

# Why +1 instead of -1 like normal Pick's formula ?? Idk lol
print(shoelace(coordinates) + sum([i[1] for i in instructions]) // 2 + 1)