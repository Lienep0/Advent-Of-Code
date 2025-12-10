import re

def string_to_list(s):
    return list(map(int, re.findall(r"[0-9]+", s)))

with open("input.txt", "r") as f:
    lines = f.readlines()
    card_numbers = [1 for _ in range(len(lines))]

    for i, line in enumerate(lines):
        winners, my_numbers = map(string_to_list, line[line.index(":") + 1:].split('|'))
        current = sum([1 if n in my_numbers else 0 for n in winners])
        for k in range(i + 1, i + current + 1):
            card_numbers[k] += card_numbers[i]

print(sum(card_numbers))