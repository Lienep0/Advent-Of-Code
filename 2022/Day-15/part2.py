import re
from tqdm import tqdm

sensors = []
distances = []
with open("input.txt", "r") as f:
    for line in f.readlines():
        sc, sr, bc, br = map(int, re.findall(r"-?\d+", line))

        sensors.append((sc, sr))
        distances.append(abs(bc - sc) + abs(br - sr))

def is_beacon(c, r):
    for d, s in zip(distances, sensors):
        sc, sr = s
        if abs(c - sc) + abs(r - sr) <= d:
            return False
    return True

def is_real(c, r):
    return (
        is_beacon(c, r) and
        not is_beacon(c + 1, r) and
        not is_beacon(c, r + 1) and
        not is_beacon(c - 1, r) and
        not is_beacon(c, r - 1)
    )

def intersect(p1, p2, p3, p4):
    x1,y1 = p1
    x2,y2 = p2
    x3,y3 = p3
    x4,y4 = p4
    denom = (y4-y3)*(x2-x1) - (x4-x3)*(y2-y1)
    if denom == 0: # parallel
        return None
    ua = ((x4-x3)*(y1-y3) - (y4-y3)*(x1-x3)) / denom
    if ua < 0 or ua > 1: # out of range
        return None
    ub = ((x2-x1)*(y1-y3) - (y2-y1)*(x1-x3)) / denom
    if ub < 0 or ub > 1: # out of range
        return None
    x = x1 + ua * (x2-x1)
    y = y1 + ua * (y2-y1)
    return (x,y)

def check_around(point):
    c, r = map(int, point)
    for i in range(c - 2, c + 2):
        for j in range(r - 2, r + 2):
            if is_real(i, j):
                print(f"Found at {i}, {j}")
                print(f"Frequency : {i * 4000000 + j}")
                exit()

# Check around diamond intersections
for i in range(len(sensors)):
    for j in range(i, len(sensors)):
        c1, r1 = sensors[i]
        c2, r2 = sensors[j]
        d1 = distances[i]
        d2 = distances[j]
        points_1 = [(c1 - d1, r1), (c1, r1 - d1), (c1 + d1, r1), (c1, r1 + d1)]
        points_2 = [(c2 - d2, r2), (c2, r2 - d2), (c2 + d2, r2), (c2, r2 + d2)]
        for k in range(4):
            for l in range(4):
                p1, p2 = points_1[k], points_1[(k + 1) % 4]
                p3, p4 = points_2[l], points_2[(l + 1) % 4]
                intersection_point = intersect(p1, p2, p3, p4)
                if intersection_point:
                    check_around(intersection_point)