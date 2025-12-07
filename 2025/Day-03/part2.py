with open("input.txt", "r") as f:
    banks = f.readlines()

n = 12

total = 0
for k, bank in enumerate(banks):
    current = bank[:n]
    for i in range(n, len(bank)):
        candidate = current + str(bank[i])
        current = str(max(*(int(candidate[:k] + candidate[k + 1:]) for k in range(n + 1))))
    total += int(current)

print(total)