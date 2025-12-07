import re

total = 0
with open("input.txt", "r") as f:
    ranges = [(int(x), int(y)) for x, y in [r.split('-') for r in f.readline().split(',')]]
    for r in ranges:
        s, e = r
        for i in range(s, e + 1):
            if re.match(r"^(.*)\1+$", str(i)):
                total += i

print(total)