numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

total = 0
with open("input.txt", "r") as f:
    for line in f.readlines():
        found1, found2 = False, False
        i = 0
        while not (found1 and found2):
            for k, number in enumerate(numbers):
                if line[i:].startswith(number) and not found1:
                    total += (k + 1) * 10
                    found1 = True
                if line[-(i + 1):].startswith(number) and not found2:
                    total += (k + 1)
                    found2 = True
            if line[i].isdigit() and not found1:
                total += int(line[i]) * 10
                found1 = True
            if line[-(i + 1)].isdigit() and not found2:
                total += int(line[-(i + 1)])
                found2 = True
            i += 1

print(total)