dirs = {
    "U": (1, 0),
    "D": (-1, 0),
    "L": (0, -1),
    "R": (0, 1)
}

with open("input.txt", "r") as f:
    lines = f.readlines()

def distance(x1, y1, x2, y2):
    return pow(x1 - x2, 2) + pow(y1 - y2, 2)

tail_visited = set((0, 0))
t_x, t_y = 0, 0
x, y = 0, 0
for line in lines:
    direction, length = line.strip().split()
    length = int(length)

    x_d, y_d = dirs[direction]
    for i in range(length):
        n_x, n_y = x + x_d, y + y_d
        if distance(n_x, n_y, t_x, t_y) > 2:
            tail_visited.add((x, y))
            t_x, t_y = x, y
        x, y = n_x, n_y

print(len(tail_visited))