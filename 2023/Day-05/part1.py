import re 

def string_to_list(s):
    return list(map(int, re.findall(r"[0-9]+", s)))

with open("input.txt", "r") as f:
    lines = f.readlines()
    seeds = string_to_list(lines[0])
    maps = []

    i = 3
    current_map = []
    while i < len(lines):
        line = lines[i].strip()
        if len(line) == 0:
            i += 2
            maps.append(current_map)
            current_map = []
            continue
        current_map.append(string_to_list(line))
        i += 1
    maps.append(current_map)

locations = []
for seed in seeds:
    for layer in maps:
        for m in layer:
            dest, source, size = m
            if seed >= source and seed < source + size:
                seed = seed - source + dest
                break
    locations.append(seed)
print(min(locations))