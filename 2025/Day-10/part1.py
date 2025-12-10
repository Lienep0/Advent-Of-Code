import re
from collections import deque

targets_list = []
values_list = []

with open("input.txt", "r") as f:
    for line in f.readlines():
        lights = [x == "#" for x in re.search(r"\[(.*)\]", line).group(1)]
        int_light = int(''.join('1' if x else '0' for x in lights), 2)
        targets_list.append(int_light)
        buttons = [tuple(map(int, s.replace(',', ''))) for s in re.findall(r"\((.*?)\)", line)]
        values_list.append([sum(2 ** (len(lights) - value - 1) for value in button_values) for button_values in buttons])

def min_xor_path(values, target):
    queue = deque([(0, 0)])  # (value, depth)
    seen = {0: 0}

    while queue:
        x, d = queue.popleft()

        if x == target:
            return d

        for v in values:
            new = x ^ v
            if new not in seen or seen[new] > d + 1:
                seen[new] = d + 1
                queue.append((new, d + 1))

    return None

total = 0
for i, target in enumerate(targets_list):
    values = values_list[i]
    total += min_xor_path(values, target)
print(total)