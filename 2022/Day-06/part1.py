from collections import deque

with open("input.txt", "r") as file:
    line = next(file)
    buffer = deque(line[:3])

    for i, char in enumerate(line[3:]):
        buffer.append(char)
        if len(set(buffer)) == 4:
            print(i + 4)
            break
        buffer.popleft()