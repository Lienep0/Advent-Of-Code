from math import lcm

with open("input.txt", "r") as f:
    lines = f.readlines()
    directions = lines[0].strip()
    dic = {x[0].strip(): tuple(x[1][2:-2].split(', ')) for x in [line.split('=') for line in lines[2:]]}

starts = [key for key in dic.keys() if key[-1] == "A"]
start_z_indexes = []
for start in starts:
    seen = {}
    i = 0
    current = start
    while True:
        direction_index = i % len(directions)
        if (current, direction_index) in seen:
            break
        seen[(current, direction_index)] = i

        if directions[direction_index] == "R":
            current = dic[current][1]
        else:
            current = dic[current][0]
        i += 1
    z_nodes = [v for k, v in seen.items() if k[0][-1] == 'Z']
    assert len(z_nodes) == 1
    start_z_indexes.append(*z_nodes)

print(lcm(*start_z_indexes))