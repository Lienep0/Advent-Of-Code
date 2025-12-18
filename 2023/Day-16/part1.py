import sys

sys.setrecursionlimit(pow(2, 30) - 1)

with open("input.txt", "r") as f:
    board = [line.strip() for line in f.readlines()]

directions = [(-1, 0), (0, -1), (0, 1), (1, 0)] # ^, <, >, v
marked = [[[False for _ in range(len(directions))] for _ in range(len(board[0]))] for _ in range(len(board))]

height = len(board)
width = len(board[0])

def rec_generate_laser(i, j, direction):
    if not (i < 0 or i >= height or j < 0 or j >= width) and not marked[i][j][direction]:
        marked[i][j][direction] = True

        i_dir, j_dir = directions[direction]
        normal_new_i = i + i_dir
        normal_new_j = j + j_dir
        match board[i][j]:
            case ".":
                rec_generate_laser(normal_new_i, normal_new_j, direction)
            case "/":
                new_direction = [2, 3, 0, 1][direction]
                i_dir, j_dir = directions[new_direction]
                new_i = i + i_dir
                new_j = j + j_dir

                rec_generate_laser(new_i, new_j, new_direction)
            case "\\":
                new_direction = [1, 0, 3, 2][direction]
                i_dir, j_dir = directions[new_direction]
                new_i = i + i_dir
                new_j = j + j_dir

                rec_generate_laser(new_i, new_j, new_direction)
            case "|":
                if direction in [0, 3]:
                    rec_generate_laser(normal_new_i, normal_new_j, direction)
                else:
                    rec_generate_laser(i - 1, j, 0)
                    rec_generate_laser(i, j, 3)
            case "-":
                if direction in [1, 2]:
                    rec_generate_laser(normal_new_i, normal_new_j, direction)
                else:
                    rec_generate_laser(i, j - 1, 1)
                    rec_generate_laser(i, j, 2)

rec_generate_laser(0, 0, 2)

total = 0
for i in range(len(board)):
    for j in range(len(board[0])):
        if any(marked[i][j][k] for k in range(4)):
            total += 1
            print("#", end='')
        else:
            print(".", end='')
    print()

print(total)