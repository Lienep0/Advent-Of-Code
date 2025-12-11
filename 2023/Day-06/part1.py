import re

def string_to_list(s):
    return list(map(int, re.findall(r"[0-9]+", s)))

def P(hold, total):
    return - (pow(hold, 2) - total * hold)

def binary_search(total, record):
    l = 0
    # Only seach the fist half of the curve 
    r = total // 2
    while l <= r:
        m = l + (r - l) // 2
        if P(m, total) <= record:
            if P(m + 1, total) > record:
                return m + 1
            else:
                l = m + 1
        else:
            r = m - 1

with open("input.txt", "r") as f:
    lines = f.readlines()
    race_times = string_to_list(lines[0])
    distance_records = string_to_list(lines[1])

# P(hold) = hold² - total * hold
# we're looking for the two points at which P(hold) > record
p = 1
for total, record in zip(race_times, distance_records):
    p *= total - 2 * binary_search(total, record) + 1
print(p)