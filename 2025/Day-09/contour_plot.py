import matplotlib.pyplot as plt

with open("input.txt", "r") as f:
    red_tiles = [tuple(map(int, line.strip().split(","))) for line in f.readlines()]

red_tiles += [red_tiles[0]]

x, y = zip(*red_tiles)

plt.fill(x, y)
plt.show()