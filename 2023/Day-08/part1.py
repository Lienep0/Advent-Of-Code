with open("input.txt", "r") as f:
    lines = f.readlines()
    directions = lines[0].strip()
    dic = {x[0].strip(): tuple(x[1][2:-2].split(', ')) for x in [line.split('=') for line in lines[2:]]}

i = 0
current = "AAA"
while True:
    if directions[i % len(directions)] == "R":
        current = dic[current][1]
    else:
        current = dic[current][0]

    if current == "ZZZ":
        print(i + 1)
        exit()

    i += 1