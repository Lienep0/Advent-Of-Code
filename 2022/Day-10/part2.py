with open("input.txt", "r") as f:
    instructions = f.readlines()

cycle = 0
x = 1
line = ""

for instruction in instructions:
    line += "█" if abs(x - (cycle % 40)) < 2 else "."

    if instruction[:4] == "addx":
        cycle += 1
        line += "█" if abs(x - (cycle % 40)) < 2 else "."
        x += int(instruction.split()[1])
    cycle += 1

for i, c in enumerate(line):
    print(c, end="")
    if i % 40 == 39:
        print()