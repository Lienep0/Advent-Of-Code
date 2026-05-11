from collections import deque

with open("input.txt", "r") as file:
    line = next(file)
    buffer = deque(line[:13])

    for i, char in enumerate(line[13:]):
        buffer.append(char)
        if len(set(buffer)) == 14:
            print(i + 14)
            break
        buffer.popleft()