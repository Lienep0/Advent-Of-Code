with open("input.txt", "r") as f:
    banks = f.readlines()

total = 0
for bank in banks:
    batteries = [int(x) for x in bank.strip()]

    best_first_choice = max(batteries[:-1])
    best_first_choice_index = batteries.index(best_first_choice)

    total += best_first_choice * 10
    total += max(batteries[best_first_choice_index + 1:])

print(total)