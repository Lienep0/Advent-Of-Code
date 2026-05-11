from itertools import batched

print(sum([".abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ".index(next(iter(set.intersection(*map(set, test))))) for test in batched((line.strip() for line in open("input.txt", "r")), 3)]))