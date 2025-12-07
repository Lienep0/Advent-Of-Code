import re
from math import prod

f = open("input.txt", "r")

numbers = []
while True:
    line = f.readline()
    if line.startswith('+') or line.startswith('*'):
        operators = re.split(r' +', line.strip())
        break
    else:
        numbers.append(list(map(int, re.findall(r'[0-9]+', line))))

total = 0
l = len(numbers)
for i, op in enumerate(operators):
    match op:
        case '+':
            total += sum(numbers[k][i] for k in range(l))
        case '*':
            total += prod(numbers[k][i] for k in range(l))

print(total)