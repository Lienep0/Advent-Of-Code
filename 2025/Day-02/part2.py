def has_pattern(i):
    c = str(i)
    l = len(c)

    for k in range(1, l // 2 + 1):
        if c[:k] == c[k:2 * k]:
            pattern = c[:k]
            if all(c[j:k + j] == pattern for j in range(k, l, k)):
                return True
            
    return False

def calculate_total():
    total = 0
    with open("input.txt", "r") as f:
        ranges = [(int(x), int(y)) for x, y in [r.split('-') for r in f.readline().split(',')]]
        for r in ranges:
            s, e = r
            for i in range(s, e + 1):
                if has_pattern(i):
                    print(i)
                    total += i
    return total

if __name__ == "__main__":
    print(calculate_total())