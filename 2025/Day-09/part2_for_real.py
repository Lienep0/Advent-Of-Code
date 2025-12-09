# To check a rectangle, check if evry corner is inside the structure
# To check if a tile is inside, check intersection between the line from that tile to the border wall, and every other horizontal/vertical line depending

def rectangle_area(t1, t2):
    x1, y1 = t1
    x_2, y_2 = t2
    return (abs(x_2 - x1) + 1) * (abs(y_2 - y1) + 1)

vertical_lines = []
horizontal_lines = []

def add_line(t1, t2):
    x1, y1 = t1
    x2, y2 = t2

    if x1 == x2:
        if y1 > y2: 
            y1, y2 = y2, y1
        vertical_lines.append((x1, y1, y2))
    else:
        if x1 > x2: 
            x1, x2 = x2, x1
        horizontal_lines.append((y1, x1, x2))

def horizontal_ray_intersects_vertical(px, py, vx, vy1, vy2):
    # Check if the horizontal ray at y=py intersects the vertical segment
    # Segment is at x=vx and spans vy1..vy2 (with vy1 < vy2)
    
    # 1. Ray crosses only if point's y is within [vy1, vy2)
    if not (vy1 <= py < vy2):
        return False

    # 2. The ray is to the right, so we need px <= vx
    if px > vx:
        return False

    return True

def is_inside_contour(p):
    px, py = p

    if p in boundary:
        return True

    cnt = 0
    # Count intersections with vertical edges
    for vx, vy1, vy2 in vertical_lines:
        if horizontal_ray_intersects_vertical(px, py, vx, vy1, vy2):
            cnt += 1

    return (cnt % 2) == 1

def is_valid_rectangle(c1, c2):
    y1, x1 = c1
    y2, x2 = c2

    corners = [(y1, x2), (y2, x1)]
    for corner in corners:
        if corner not in red_tiles and not is_inside_contour(corner):
            return False
        
    return True

boundary = set()
def fill_boundary(old, new):
        x1, y1 = old
        x2, y2 = new

        dx = 0 if x1 == x2 else (1 if x2 > x1 else -1)
        dy = 0 if y1 == y2 else (1 if y2 > y1 else -1)

        x, y = x1, y1
        boundary.add((x, y))
        while (x, y) != (x2, y2):
            x += dx
            y += dy
            boundary.add((x, y))

red_tiles = []
with open("input.txt", "r") as f:
    for line in f.readlines():
        tile_coordinates = tuple(map(int, line.strip().split(",")))
        if len(red_tiles) > 0:
            add_line(red_tiles[-1], tile_coordinates)
            fill_boundary(red_tiles[-1], tile_coordinates)
        red_tiles.append(tile_coordinates)
    add_line(red_tiles[-1], red_tiles[0])
    fill_boundary(red_tiles[-1], red_tiles[0])

def print_board():
    height = max([t[1] for t in red_tiles]) + 2
    width = max([t[0] for t in red_tiles]) + 2

    for j in range(height):
        for i in range(width):
            if (i, j) in red_tiles:
                print("#", end="")
            elif is_inside_contour((i, j)):
                print("X", end="")
            else:
                print(".", end="")
        print()

#print_board()

max_area = 0
for i in range(len(red_tiles)):
    for j in range(i + 1, len(red_tiles)):
        if is_valid_rectangle(red_tiles[i], red_tiles[j]):
            #print(red_tiles[i], red_tiles[j], rectangle_area(red_tiles[i], red_tiles[j]))
            max_area = max(max_area, rectangle_area(red_tiles[i], red_tiles[j]))

print(max_area)

# Bad apprach. I assumed the rectangle would be fully inside if evry corner was inside but this is definitely not the case
# Need to check, for each rectangle vertex, if it intersects with any line at any point. If it does, discard the rectangle