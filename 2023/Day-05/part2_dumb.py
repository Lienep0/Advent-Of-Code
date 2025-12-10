import re 
import time

def string_to_list(s):
    return list(map(int, re.findall(r"[0-9]+", s)))

with open("input.txt", "r") as f:
    lines = f.readlines()
    seed_ranges = string_to_list(lines[0])
    seed_ranges = [(seed_ranges[i], seed_ranges[i] + seed_ranges[i + 1] - 1) for i in range(0, len(seed_ranges), 2)]
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

maps = maps[::-1]

def get_seed(value):
    for layer in maps:
        for rule in layer:
            source, dest, size = rule
            if source <= value and value < source + size:
                value = value + dest - source
                break
    return value

def find_min_seed():
    i = 0
    while True:
        s = get_seed(i)
        for a, b in seed_ranges:
            if a <= s and s < b:
                return i
        i += 1

start = time.time()
found = find_min_seed()
end = time.time()

print(f"Found {found} in {end - start :.5} seconds")