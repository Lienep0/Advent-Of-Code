from functools import cache

neighbors = {}
with open("input.txt", "r") as f:
    for line in f.readlines():
        node, node_neighbors = line.split(":")
        node_neighbors = node_neighbors.strip().split(' ')
        neighbors[node] = node_neighbors
neighbors["out"] = []

@cache
def dfs_number_paths(start, end):
    if start == end:
        return 1
    s = 0
    for neighbor in neighbors[start]:
        s += dfs_number_paths(neighbor, end)
    return s

print(dfs_number_paths("svr", "fft") * 
      dfs_number_paths("fft", "dac") * 
      dfs_number_paths("dac", "out") + 
      dfs_number_paths("svr", "dac") * 
      dfs_number_paths("dac", "fft") * 
      dfs_number_paths("fft", "out"))