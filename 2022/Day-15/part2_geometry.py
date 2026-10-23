import re
import shapely.plotting
import matplotlib.pyplot as plt
from shapely.geometry import Polygon

sensors = []
distances = []
with open("input.txt", "r") as f:
    for line in f.readlines():
        sc, sr, bc, br = map(int, re.findall(r"-?\d+", line))

        sensors.append((sc, sr))
        distances.append(abs(bc - sc) + abs(br - sr))

polygons = []
for i in range(len(sensors)):
    c, r = sensors[i]
    d = distances[i]
    polygons.append(Polygon([(c - d, r), (c, r + d), (c + d, r), (c, r - d)]))

fig, ax = plt.subplots() 
for polygon in polygons:
    shapely.plotting.plot_polygon(polygon, ax=ax) 
plt.axis([
    0, 4e6,
    0, 4e6,
])
plt.show()