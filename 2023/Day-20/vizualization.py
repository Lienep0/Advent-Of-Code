import networkx as nx
import matplotlib.pyplot as plt

graph = {}
with open("input.txt", "r") as f:
    for line in f.readlines():
        module_type = "Conjunction" if line[0] == "&" else "FlipFlop" if line[0] == "%" else "Broadcaster"
        start = 0 if module_type == "Broadcaster" else 1
        name = line.strip()[start:].split(" -> ")[0]
        name_neighbors = line.strip().split(" -> ")[1].split(", ")
        graph[name] = (module_type, name_neighbors)

# Create a graph
G = nx.Graph()

for node, p in graph.items():
    G.add_node(node, type=p[0])

G.add_node("rx", type="rx")

# Add nodes and edges
for node, p in graph.items():
    for neighbor in p[1]:
        G.add_edge(node, neighbor)

# Set colors
color_map = {
    "Conjunction": "green",
    "Broadcaster": "red",
    "FlipFlop": "blue",
    "rx": "yellow"
}

node_colors = [
    color_map[G.nodes[n]["type"]]
    for n in G.nodes()
]

# Draw the graph
pos = nx.kamada_kawai_layout(G)

nx.draw(
    G,
    pos,
    with_labels=True,
    node_color=node_colors,
    node_size=2000
)

plt.show()