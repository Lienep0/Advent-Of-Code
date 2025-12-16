with open("input.txt", "r") as f:
    words = f.readline().strip().split(',')

def hash(s):
    total = 0
    for char in s:
        total += ord(char)
        total *= 17
        total %= 256
    return total

total = 0
for w in words:
    total += hash(w)
print(total)