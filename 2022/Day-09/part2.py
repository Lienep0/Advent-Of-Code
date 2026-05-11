dirs = {
    "U": (1, 0),
    "D": (-1, 0),
    "L": (0, -1),
    "R": (0, 1)
}

with open("input.txt", "r") as f:
    lines = f.readlines()

def print_coords(coords):
    coords = [(abs(x), abs(y)) for x, y in coords]
    for i in range(50)[::-1]:
        for j in range(50):
            if (i, j) in coords:
                x = coords.index((i, j))
                print("H" if x == 0 else x, end="")
            else:
                print(".", end="")
        print()
    print()

def distance(x1, y1, x2, y2):
    return pow(x1 - x2, 2) + pow(y1 - y2, 2)

def best_neighbor_coords(x, y, t_x, t_y):
    best_coords = (x, y)
    best_d = distance(x, y, t_x, t_y)
    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            candidate_d = distance(x + i, y + j, t_x, t_y)
            if candidate_d < best_d:
                best_d = candidate_d
                best_coords = (x + i, y + j)
    return best_coords

n = 10
tail_visited = set()
coords = [[0, 0] for _ in range(n)]

def move_body(direction):
    x_d, y_d = dirs[direction]

    # move head
    x, y = coords[0]
    coords[0] = x + x_d, y + y_d

    # last position from which a cell moved
    l_x, l_y = x, y

    # move body according to what's in front
    for i in range(n - 1):
        d = distance(*coords[i], *coords[i + 1])

        if d > 2:
            coords[i + 1] = best_neighbor_coords(*coords[i + 1], *coords[i])

        if i == (n - 2):
            tail_visited.add(tuple(coords[i + 1]))

"""for line in lines:
    direction, movement_length = line.strip().split()
    movement_length = int(movement_length)

    for _ in range(movement_length):
        move_body(direction)
print(len(tail_visited))"""

# manual mode
from pynput import keyboard
import sys
import os

def on_press(key):
    try:
        match key.char:
            case "z":
                move_body("U")
            case "q":
                move_body("L")
            case "s":
                move_body("D")
            case "d":
                move_body("R")
        os.system('clear')
        print_coords(coords)
    except AttributeError:
        pass
    if key == keyboard.Key.esc:
        return False

print_coords(coords)
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()