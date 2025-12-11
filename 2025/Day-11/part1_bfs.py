from collections import deque

neighbors = {}
with open("input.txt", "r") as f:
    for line in f.readlines():
        node, node_neighbors = line.split(":")
        node_neighbors = node_neighbors.strip().split(' ')
        neighbors[node] = node_neighbors

total_paths = 0
to_explore = deque(["you"])
while to_explore: 
    current = to_explore.popleft()
    if current == "out":
        total_paths += 1
    else:
        for neighbor in neighbors[current]:
            to_explore.append(neighbor)
print(total_paths)