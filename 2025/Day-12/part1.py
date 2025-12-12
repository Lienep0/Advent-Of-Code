total = 0
with open("input.txt", "r") as f:
    line = next(f)
    while "x" not in line:
        line = next(f)
    while True:
        size_part, presents_part = line.split(":")
        w, h = map(int, size_part.split("x"))
        size = w * h
        presents = sum(map(int, presents_part.strip().split()))
        total += size > presents * 8
        try:
            line = next(f)
        except StopIteration:
            break
print(total)