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
        direction = directions[i % len(directions)]
        if (current, direction) in seen:
            break
        seen[(current, direction)] = i

        if direction == "R":
            current = dic[current][1]
        else:
            current = dic[current][0]
        i += 1
    print(seen)
    start_z_indexes.append([v for k, v in seen.items() if k[0][-1] == 'Z'])

print(start_z_indexes)