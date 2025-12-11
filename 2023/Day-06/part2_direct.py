import re

def distance_between_integer_roots(total, record):
    return pow(total ** 2 - 4 * record, .5) # sqrt(delta = b² - 4ac)

with open("input.txt", "r") as f:
    lines = f.readlines()
    race_time = int(''.join(re.findall(r"[0-9]+", lines[0])))
    distance_record = int(''.join(re.findall(r"[0-9]+", lines[1])))

print(distance_between_integer_roots(race_time, distance_record))