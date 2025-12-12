import tqdm

lines = []
with open("input.txt", "r") as f:
    for line in f.readlines():
        springs, record = line.strip().split(" ")
        record = list(map(int, record.split(',')))
        lines.append((springs, record))

def full_solution(springs, record):
    i = 0
    group_index = 0
    on_group = False
    while i < len(springs):
        if springs[i] == "#" and not on_group:
            start = i
            on_group = True
            if group_index >= len(record):
                return False
        elif not springs[i] == "#" and on_group:
            on_group = False
            group_size = i - start
            if record[group_index] != group_size:
                return False
            group_index += 1
        i += 1
    
    # Check end group
    if on_group:
        group_size = i - start
        if record[group_index] != group_size:
            return False
        group_index += 1

    return group_index == len(record)

def bruteforce(springs, record, unkown_count, position=0):
    if unkown_count == 0:
        return full_solution(springs, record)

    while springs[position] != "?":
        position += 1
    
    return (bruteforce(springs[:position] + "." + springs[position + 1:], record, unkown_count - 1, position + 1) 
            + bruteforce(springs[:position] + "#" + springs[position + 1:], record, unkown_count - 1, position + 1))

total = 0
for springs, record in tqdm.tqdm(lines):
    total += bruteforce(springs, record, springs.count("?"))
print(total)