from collections import deque

with open("input.txt", "r") as f:
    crate_layers = []
    while True:
        line = next(f)
        if line == "\n": break
        crate_layers.append(line[1::4])

    stacks = [deque() for _ in range(len(crate_layers[0]))]
    for layer in list(reversed(crate_layers[:-1])):
        for i, crate in enumerate(layer):
            if crate != " ": stacks[i].append(crate)
    
    for line in f:
        iterations, origin, destination = map(int, line.strip().split()[1::2])
        buffer = deque()

        for _ in range(iterations):
            buffer.append(stacks[origin - 1].pop())
        for _ in range(iterations):
            stacks[destination - 1].append(buffer.pop())

print(''.join([stack.pop() for stack in stacks]))