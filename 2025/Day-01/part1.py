current_number = 50
zero_count = 0
with open("input.txt", "r") as f:
    for line in f.readlines():
        direction = line[:1]
        turns = int(line[1:])
        if direction == "L":
            turns *= -1

        current_number = (current_number + turns) % 100
        
        zero_count += current_number == 0

print(zero_count)