total = 0

class Node():
    def __init__(self, parent, name, is_folder=True, size=0):
        self.parent = parent
        self.name = name
        self.is_folder = is_folder
        self.size = size
        self.children = []

    def create_child(self, name, is_folder=True, size=0):
        new_node = Node(self, name, is_folder, size)
        self.children.append(new_node)
        return new_node
    
    def print(self, depth = 0):
        if depth == 0:
            print(self.name + " " + str(self.size))
        else:
            print((depth - 5) * " " + "└----" + self.name + " " + str(self.size))
        for child in self.children:
            child.print(depth + 5)

    def solve(self):
        # call on root to return the answer
        for child in self.children:
            child.solve()
            self.size += child.size
        if self.is_folder and self.size < 100_000:
            global total
            total += self.size

root = Node(None, "root")
cursor = root

with open("input.txt", "r") as f:
    lines = f.readlines()

i = 0
while i < len(lines):
    line = lines[i]

    match line[:4]:
        case "$ cd":
            folder_name = line[4:].strip()
            if folder_name == "..":
                cursor = cursor.parent
            else:
                cursor = cursor.create_child(folder_name)
            i += 1

        case "$ ls":
            i += 1
            while i < len(lines) and not lines[i].startswith("$"):
                line = lines[i]
                if line.startswith("dir"):
                    cursor.create_child(line[4:].strip())
                else:
                    size, name = line.strip().split()
                    size = int(size)
                    cursor.create_child(name, False, size)
                i += 1

root.solve()
root.print()
print(total)