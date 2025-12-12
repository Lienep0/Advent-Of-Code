import re

def string_to_list(s):
    return list(map(int, re.findall(r"-?\d+", s)))

def diff(sequence):
    return [sequence[i + 1] - sequence[i] for i in range(len(sequence) - 1)]

def extrapolate(sequence):
    differences = []
    current_difference = sequence
    while not all([current_difference[i] == 0 for i in range(len(current_difference))]):
        differences.append(current_difference)
        current_difference = diff(current_difference)
    return sum(pow(-1, i) * differences[i][0] for i in range(len(differences)))

with open("input.txt", "r") as f:
    sequences = [string_to_list(line) for line in f.readlines()]

print(sum(extrapolate(sequence) for sequence in sequences))