from functools import cache

with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

@cache
def rec(i, j):
    if i == len(lines) - 1:
        return 1
    if lines[i + 1][j] == '^':
        return rec(i + 1, j + 1) + rec(i + 1, j - 1)
    return rec(i + 1, j)

print(rec(0, lines[0].index("S")))