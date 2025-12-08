from itertools import product
import re

l = [-1, 0, 1]
directions = list(product(l, repeat=2))
directions.remove((0, 0))

with open("input.txt", "r") as f:
    board = [line.strip() for line in f.readlines()]

numbers = [[-1 for _ in range(len(board[0]))] for _ in range(len(board))]

symbols = set()
for i, line in enumerate(board):
    for j in range(len(line)):
        if not board[i][j].isdigit():
            if not board[i][j] == '.':
                symbols.add(board[i][j])
        elif numbers[i][j] == -1:
            number = int(re.search(r"[0-9]+", line[j:]).group(0))
            for k in range(len(str(number))):
                numbers[i][j + k] = number

total = 0
for i, line in enumerate(board):
    for j, symbol in enumerate(line):
        if symbol in symbols:
            found = []
            for dir in directions:
                new_i = i + dir[0]
                new_j = j + dir[1]
                
                number = numbers[new_i][new_j]
                if number >= 0 and not number in found:
                    found.append(number)
                    total += number
print(total)