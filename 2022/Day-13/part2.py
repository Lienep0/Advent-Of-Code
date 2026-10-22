from functools import cmp_to_key

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

def real_compare(a, b):
    if compare(a, b)[0]:
        return -1
    return 1

packets = []
for i in range(0, len(lines) + 1, 3):
    packets.append(eval(lines[i]))
    packets.append(eval(lines[i + 1]))
packets.append([[2]])
packets.append([[6]])

sorted_packets = sorted(packets, key=cmp_to_key(real_compare))
d1 = sorted_packets.index([[2]]) + 1
d2 = sorted_packets.index([[6]]) + 1
print(d1 * d2)