import time

start = time.time()
current_number = 50
zero_count = 0
with open("input.txt", "r") as f:
    for line in f.readlines():
        direction = line[:1]
        turns = int(line[1:])

        step = 1
        if direction == "L":
            step *= -1

        for _ in range(turns):
            current_number = (current_number + step) % 100
            if current_number == 0:
                zero_count += 1
end = time.time()

print(f"Time taken : {end - start} s")
print(f"Answer : {zero_count}")