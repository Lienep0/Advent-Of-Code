with open("input.txt", "r") as f:
    lines = f.readlines()

def compare(a, b):
    ta, tb = type(a), type(b)
    if ta == int and tb == int:
        if a == b:
            return None, False
        return a < b, True
    elif ta == int:
        return compare([a], b)
    elif tb == int:
        return compare(a, [b])

    # Both lists
    else:
        la = len(a)
        lb = len(b)

        for i in range(min(la, lb)):
            res, finished = compare(a[i], b[i])
            if finished:
                return res, True
        
        if la == lb:
            return None, False
        return la < lb, True

s = 0
for i in range(0, len(lines) + 1, 3):
    res, _ = compare(eval(lines[i]), eval(lines[i + 1]))
    if res:
        s += i // 3 + 1
print(s)