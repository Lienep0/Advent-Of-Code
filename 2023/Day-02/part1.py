colors = ["red", "green", "blue"]
max_values = [12, 13, 14]

def check_dics(dics):
    for dic in dics:
            for i, color in enumerate(colors):
                value = dic.get(color)
                if value != None and value > max_values[i]:
                    return False
    return True

total = 0
with open("input.txt", "r") as f:
    valid_line = True
    for line in f.readlines():
        id = int(line[:line.index(':')].split(' ')[-1])
        games_dics = [{k: int(v) for item in game.split(', ') for v, k in [item.split()]} for game in line[line.index(':') + 1:].strip().split('; ')]
        if check_dics(games_dics):
            total += id
print(total)