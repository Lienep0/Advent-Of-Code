total = 0
with open("input.txt", "r") as f:
    ranges = [(int(x), int(y)) for x, y in [r.split('-') for r in f.readline().split(',')]]
    for r in ranges:
        s, e = r
        for i in range(s, e + 1):
            c = str(i)
            if c[:len(c)//2] == c[len(c)//2:]:
                total += i

print(total)