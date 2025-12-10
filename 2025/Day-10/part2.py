import re
from ortools.sat.python import cp_model

joltages = []
vectors_lists = []

with open("input.txt", "r") as f:
    for line in f.readlines():
        joltage = eval("(" + re.search(r"\{(.*)\}", line).group(1) + ")")
        joltages.append(joltage)
        vectors_lists.append([tuple(0 if i not in map(int, s.replace(',', '')) else 1 for i in range(len(joltage))) for s in re.findall(r"\((.*?)\)", line)])

total = 0
for i, target in enumerate(joltages):
    vectors = vectors_lists[i]
    m, n = len(vectors), len(target)

    # Calculate Upper Bounds
    ubs = [min(target[i] for i in [i for i in range(n) if vectors[j][i] == 1]) for j in range(m)]

    # Set Up the Model
    model = cp_model.CpModel()
    x = [model.NewIntVar(0, ubs[j], f"x{j}") for j in range(m)]
    for i in range(n):
        model.Add(sum(vectors[j][i] * x[j] for j in range(m)) == target[i])
    model.Minimize(sum(x))

    # Solve
    solver = cp_model.CpSolver()
    result = solver.Solve(model)
    total += sum([solver.Value(var) for var in x])
    
print(total)