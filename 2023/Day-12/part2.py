import sys
from functools import cache

sys.setrecursionlimit(2 ** 30 - 1)

lines = []
with open("input.txt", "r") as f:
    for line in f.readlines():
        springs, record = line.strip().split(" ")
        springs = (springs + "?") * 4 + springs
        record = tuple(map(int, record.split(','))) * 5
        lines.append((springs, record))

# Heuristic to make this faster : stop when the remaining number of ? is less than the sum of the remaining groups
def find_number(springs, record):
    @cache
    def rec_find_number(position, group_index, group_size, on_group):
        # base case
        if position == len(springs):
            if on_group:
                return int(group_index == len(record) - 1 and group_size == record[-1])
            else:
                return int(group_index == len(record))

        if springs[position] == "?":
            if on_group:
                # continue group
                if group_size < record[group_index]:
                    v = rec_find_number(position + 1, group_index, group_size + 1, True)
                # interrupt group
                else:
                    v = rec_find_number(position + 1, group_index + 1, 0, False)
            else:
                # Make a choice : start a group or not
                # if we've done all groups, there's no choice:
                if group_index == len(record):
                    v = rec_find_number(position + 1, group_index, 0, False)
                else:
                    v = (rec_find_number(position + 1, group_index, 1, True)
                        + rec_find_number(position + 1, group_index, 0, False))
        elif springs[position] == ".":
            # interrupt group
            if on_group:
                # if the group size is too low, BEEP BEEP
                if group_size < record[group_index]:
                    v = False
                else:
                    v = rec_find_number(position + 1, group_index + 1, 0, False)
            # just continue without a group
            else:
                v = rec_find_number(position + 1, group_index, 0, False)
        elif springs[position] == "#":
            if on_group:
                # continue group
                if group_size < record[group_index]:
                    v = rec_find_number(position + 1, group_index, group_size + 1, True)
                # BEEP BEEP WE ARE NOT GOOD
                else:
                    v = 0
            # start a new group
            else:
                # if we've done all groups, BEEP BEEP
                if group_index == len(record):
                    v = 0
                else:
                    v = rec_find_number(position + 1, group_index, 1, True)
        return v

    return rec_find_number(0, 0, 0, False)

total = 0
for i in range(len(lines)):
    total += find_number(*lines[i])
print(total)