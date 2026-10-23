import re

sensors = []
distances = []
with open("input.txt", "r") as f:
    for line in f.readlines():
        sc, sr, bc, br = map(int, re.findall(r"-?\d+", line))

        sensors.append((sc, sr))
        distances.append(abs(bc - sc) + abs(br - sr))


s = 0
ranges = [(0, 4_000_000) for _ in range(4_000_000)]
