elfmoves = ("A", "B", "C")
outcomes = ("Y", "Z", "X")
roundscores = (3, 6, 0)

score = 0
with open("input.txt", "r") as f:
    for line in f:
        elf, outcome = line.strip().split(" ")
        score += ((elfmoves.index(elf) + outcomes.index(outcome)) % 3) + 1 + roundscores[outcomes.index(outcome)]
print(score)