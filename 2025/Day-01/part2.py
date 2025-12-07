import time

start = time.time()
current_number = 50
zero_count = 0
with open("input.txt", "r") as f:
    for line in f.readlines():
        direction = line[:1]
        turns = int(line[1:])

        # Did a full rotation
        zero_count += turns // 100
        turns %= 100

        if direction == "L":
            turns *= -1

        past_number = current_number
        current_number = (current_number + turns) % 100 

        # Went by zero in the rotation, or stopped on zero
        if past_number != 0 and (
            direction == "L" and (current_number > past_number or current_number == 0) or
            direction == "R" and current_number < past_number):
            zero_count += 1
end = time.time()

print(f"Time taken : {end - start} s")
print(f"Answer : {zero_count}")