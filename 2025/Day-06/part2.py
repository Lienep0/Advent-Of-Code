import operator

file_matrix = [line.removesuffix('\n') for line in open("input.txt","r")]

file_matrix = file_matrix[:-1] + [' ' * len(file_matrix[0])] + [file_matrix[-1]]

transposed = [[line[i] for line in file_matrix] for i in range(len(file_matrix[0]))]
transposed = [''.join(line) for line in transposed]
transposed.append('')

total = 0
current = 0
op = None
for line in transposed:
    elements = line.strip().split(' ')
    match len(elements):
        case 1:
            try:
                current = op(current, int(elements[0]))
            except ValueError:
                total += current
        case _:
            match elements[-1]:
                case '+':
                    op = operator.add
                    current = 0
                case '*':
                    op = operator.mul
                    current = 1
            current = op(current, int(elements[0]))
print(total)