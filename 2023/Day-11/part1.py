import bisect

galaxies = []
universe = []
with open("input.txt", "r") as f:
    for i, line in enumerate(f.readlines()):
        line = line.strip()
        galaxies.extend([(i, j) for j in range(len(line)) if line[j] == "#"])
        universe.append(line)

vertical_extensions = []
for j in range(len(universe[0])):
    if all([universe[i][j] == '.' for i in range(len(universe))]):
        vertical_extensions.append(j)
    
horizontal_extensions = []
for i in range(len(universe)):
    if all([universe[i][j] == '.' for j in range(len(universe[0]))]):
        horizontal_extensions.append(i)

for k in range(len(galaxies)):
    i, j = galaxies[k]
    new_i = i + bisect.bisect_left(horizontal_extensions, i)
    new_j = j + bisect.bisect_left(vertical_extensions, j)
    galaxies[k] = (new_i, new_j)

total = 0
for i in range(len(galaxies)):
    for j in range(i + 1, len(galaxies)):
        i_1, j_1 = galaxies[i]
        i_2, j_2 = galaxies[j]
        total += abs(i_1 - i_2) + abs(j_1 - j_2)
print(total)