import tqdm

lines = []
with open("easyinput.txt", "r") as f:
    for line in f.readlines():
        springs, record = line.strip().split(" ")
        springs = (springs + "?") * 4 + springs
        record = tuple(map(int, record.split(','))) * 5
        lines.append((springs, record))

cache = {}
def rec_find_number(springs, record, position, current_group_index):


"""total = 0
for springs, record in tqdm.tqdm(lines):
    total += smartforce(springs, record, springs.count("?"))
print(total)"""