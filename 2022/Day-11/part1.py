class Monkey():
    def __init__(self, items, operationstring, test_value, success_index, fail_index):
        self.items = items
        self.operation = lambda old: eval(operationstring.replace("new = ", ""))
        self.test_value = test_value
        self.success_index = success_index
        self.fail_index = fail_index

    def analyse(self, item):
        worry = self.operation(item) // 3
        if worry % self.test_value == 0:
            return worry, self.success_index
        return worry, self.fail_index

with open("input.txt", "r") as f:
    lines = f.readlines()

monkeys = []
N = (len(lines) + 1) // 7
for i in range(N):
    lineindex = (i * 7)
    items = list(map(int, lines[lineindex + 1][18:].split(", ")))
    operationstring = lines[lineindex + 2][13:].strip()
    test_value = int(lines[lineindex + 3].strip().split()[-1])
    success_index = int(lines[lineindex + 4].strip().split()[-1])
    fail_index = int(lines[lineindex + 5].strip().split()[-1])

    monkeys.append(Monkey(items, operationstring, test_value, success_index, fail_index))

N_ROUNDS = 20

inspection_numbers = [0 for _ in range(N)]
for _ in range(N_ROUNDS):
    for i in range(N):
        inspection_numbers[i] += len(monkeys[i].items)
        for j in range(len(monkeys[i].items)):
            new_level, new_index = monkeys[i].analyse(monkeys[i].items.pop(0))
            monkeys[new_index].items.append(new_level)

a, b = inspection_numbers[0], inspection_numbers[1]
maximum = a if a > b else b
second_maximum = a if a <= b else b
for c in inspection_numbers[2:]:
    if c > maximum:
        second_maximum = maximum
        maximum = c
    elif c > second_maximum:
        second_maximum = c
print(maximum * second_maximum)