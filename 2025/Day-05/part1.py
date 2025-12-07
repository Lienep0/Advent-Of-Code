import bisect

ranges = []
f =  open("input.txt", "r")

while True:
    l = f.readline()
    if l == '\n': 
        break
    bisect.insort(ranges, tuple(map(int, l.strip().split('-'))))

total = 0
for line in f.readlines():
    i = int(line.strip())
    for s, e in ranges:
        if i < s:
            break
        if i <= e:
            total += 1
            break

print(total)