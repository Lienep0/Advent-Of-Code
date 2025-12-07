elfmoves = ("A", "B", "C")
yourmoves = ("X", "Y", "Z")
roundscores = (3, 0, 6)

score = 0
with open("input.txt", "r") as f:
    for line in f:
        elf, you = line.strip().split(" ")
        score += yourmoves.index(you) + 1 + roundscores[(elfmoves.index(elf) - yourmoves.index(you)) % 3]
print(score)