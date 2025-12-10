import re

def string_to_list(s):
    return list(map(int, re.findall(r"[0-9]+", s)))

total = 0
with open("input.txt", "r") as f:
    for line in f.readlines():
        winners, my_numbers = map(string_to_list, line[line.index(":") + 1:].split('|'))
        current = sum([1 if n in my_numbers else 0 for n in winners])
        if current > 0:
            total += pow(2, current - 1)

print(total)