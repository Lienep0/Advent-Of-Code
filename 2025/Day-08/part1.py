import heapq
from networkx.utils import UnionFind
from functools import reduce
import operator

def d(a, b):
    x_0, y_0, z_0 = a
    x_1, y_1, z_1 = b
    return (x_1 - x_0) ** 2 + (y_1 - y_0) ** 2 + (z_1 - z_0) ** 2

nodes_coordinates = []
distances = []
with open("input.txt", "r") as f:
    for i, line in enumerate(f.readlines()):
        current_coordinates = list(map(int, line.strip().split(',')))
        for coordinates, j in nodes_coordinates:
            heapq.heappush(distances, (d(current_coordinates, coordinates), i, j))
        nodes_coordinates.append((current_coordinates, i))

uf = UnionFind()

n = 1000
while n > 0:
    dist, i, j = heapq.heappop(distances)
    uf.union(i, j)
    n -= 1

print(reduce(operator.mul, sorted(map(len,uf.to_sets()))[-3:], 1))