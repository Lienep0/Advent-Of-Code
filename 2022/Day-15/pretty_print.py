import re

colors = [
    '\033[31m',
    '\033[32m',
    '\033[33m',
    '\033[34m',
    '\033[35m',
    '\033[36m',
    '\033[37m'
]

sensors = []
beacons = []
distances = []
min_c = 0
max_c = 0
min_r = 0
max_r = 0
with open("easyinput.txt", "r") as f:
    for line in f.readlines():
        sc, sr, bc, br = map(int, re.findall(r"-?\d+", line))

        max_c = max(max_c, sc, bc)
        min_c = min(min_c, sc, bc)
        max_r = max(max_r, sr, br)
        min_r = min(min_r, sr, br)

        sensors.append((sc, sr))
        beacons.append((bc, br))
        distances.append(abs(bc - sc) + abs(br - sr))

def is_not_beacon(c, r):
    i = 0
    for d, s in zip(distances, sensors):
        sc, sr = s
        if abs(c - sc) + abs(r - sr) <= d:
            return True, i
        i += 1
    return False, 0

def print_map():
    for r in range(min_r-20, max_r+20):
        print(f"{r: 3} ", end="")
        for c in range(min_c-20, max_c+20):
            if (c, r) in beacons:
                print("B", end="")
            elif (c, r) in sensors:
                print("S", end="")
            else:
                res, n = is_not_beacon(c, r)
                if res:
                    print(colors[n % len(colors)], end="")
                    print("#", end="")
                    print('\033[0m', end="")
                else:
                    print(".", end="")
        print()

print_map()