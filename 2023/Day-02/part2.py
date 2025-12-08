from math import prod

colors = ["red", "green", "blue"]

def max_values(dics):
    max_values = [0, 0, 0]
    for dic in dics:
            for i, color in enumerate(colors):
                value = dic.get(color)
                if value != None and value > max_values[i]:
                    max_values[i] = value
    return max_values

total = 0
with open("input.txt", "r") as f:
    valid_line = True
    for line in f.readlines():
        id = int(line[:line.index(':')].split(' ')[-1])
        games_dics = [{k: int(v) for item in game.split(', ') for v, k in [item.split()]} for game in line[line.index(':') + 1:].strip().split('; ')]
        total += prod(max_values(games_dics))
print(total)