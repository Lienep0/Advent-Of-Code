with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

beams = [lines[0].index("S")]

total = 0
for i in range(1, len(lines)):
    new_beams = set()
    for beam in beams:
        if lines[i][beam] == '^':
            total += 1
            new_beams.add(beam + 1)
            new_beams.add(beam - 1)
        else:
            new_beams.add(beam)
    beams = new_beams
print(total)