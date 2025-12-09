def rectangle_area(t1, t2):
    x_1, y_1 = t1
    x_2, y_2 = t2
    return (abs(x_2 - x_1) + 1) * (abs(y_2 - y_1) + 1)

with open("input.txt", "r") as f:
    red_tiles = [tuple(map(int, line.strip().split(","))) for line in f.readlines()]

max_area = 0
for i in range(len(red_tiles)):
    for j in range(i + 1, len(red_tiles)):
        max_area = max(rectangle_area(red_tiles[i], red_tiles[j]), max_area)

print(max_area)