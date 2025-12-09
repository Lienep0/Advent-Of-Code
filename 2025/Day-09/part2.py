def rectangle_area(t1, t2):
    x_1, y_1 = t1
    x_2, y_2 = t2
    return (abs(x_2 - x_1) + 1) * (abs(y_2 - y_1) + 1)
    
def print_board(red_tiles, green_tiles):
    height = max([t[1] for t in red_tiles]) + 2
    width = max([t[0] for t in red_tiles]) + 2

    for j in range(height):
        for i in range(width):
            if (i, j) in red_tiles:
                print("#", end="")
            elif (i, j) in green_tiles:
                print("X", end="")
            else:
                print(".", end="")
        print()

def fill(green_tiles, old, new):
        x1, y1 = old
        x2, y2 = new

        dx = 0 if x1 == x2 else (1 if x2 > x1 else -1)
        dy = 0 if y1 == y2 else (1 if y2 > y1 else -1)

        x, y = x1, y1
        green_tiles.add((x, y))
        while (x, y) != (x2, y2):
            x += dx
            y += dy
            green_tiles.add((x, y))

red_tiles = []
green_tiles = set()
with open("easyinput.txt", "r") as f:
    for line in f.readlines():
        tile_coordinates = tuple(map(int, line.strip().split(",")))
        if len(red_tiles) > 0:
            fill(green_tiles, red_tiles[-1], tile_coordinates)
        red_tiles.append(tile_coordinates)
    fill(green_tiles, red_tiles[-1], red_tiles[0])

print_board(red_tiles, green_tiles)
exit(0)
max_area = 0
for i in range(len(red_tiles)):
    for j in range(i, len(red_tiles)):
        new_area = rectangle_area(red_tiles[i], red_tiles[j])
        if new_area > max_area and check(red_tiles[i], red_tiles[j]):
            max_area = new_area

print(max_area)