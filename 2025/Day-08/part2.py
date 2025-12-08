import heapq
from networkx.utils import UnionFind

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

uf = UnionFind([i for i in range(len(nodes_coordinates))])

while True:
    dist, i, j = heapq.heappop(distances)
    uf.union(i, j)
    if len(list(uf.to_sets())) == 1:
        print(nodes_coordinates[i][0][0] * nodes_coordinates[j][0][0])
        break
