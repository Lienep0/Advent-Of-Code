import re

sensors = []
distances = []
with open("input.txt", "r") as f:
    for line in f.readlines():
        sc, sr, bc, br = map(int, re.findall(r"-?\d+", line))

        sensors.append((sc, sr))
        distances.append(abs(bc - sc) + abs(br - sr))

def is_not_beacon(c, r):
    for d, s in zip(distances, sensors):
        sc, sr = s
        if abs(c - sc) + abs(r - sr) <= d:
            return True
    return False

# Dichotomy
r = 2_000_000
N = 100_000_000

def find_dichotomy(lo, hi, upper_bound):
    while True:
        m = (lo + hi) // 2
        if upper_bound and is_not_beacon(m, r) and not is_not_beacon(m + 1, r):
            return m
        elif not upper_bound and is_not_beacon(m, r) and not is_not_beacon(m - 1, r):
            return m
        else:
            if is_not_beacon(m, r):
                if upper_bound: lo = m
                else: hi = m
            else:
                if upper_bound: hi = m
                else: lo = m

hi = find_dichotomy(0, N, upper_bound=True)
lo = find_dichotomy(-N, 0, upper_bound=False)

print(hi - lo)
