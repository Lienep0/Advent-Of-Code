with open("input.txt", "r") as f:
    instructions = f.readlines()

total = 0
cycle = 1
x = 1

for instruction in instructions:
    if (cycle - 20) % 40  == 0:
        total += x * cycle

    if instruction[:4] == "addx":
        if (cycle - 19) % 40  == 0:
            total += x * (cycle + 1)
        x += int(instruction.split()[1])
        cycle += 1

    cycle += 1

print(total)