DIRECTIONS = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)] 
board = [list([x == '@' for x in line.strip()]) for line in open("input.txt").readlines()]
height = len(board)
width = len(board[0])

total = 0
for i in range(height):
    for j in range(width):
        if board[i][j]:
            count = 0
            for direction in DIRECTIONS:
                i_dir, j_dir = direction
                new_i = i + i_dir
                new_j = j + j_dir

                if not (new_i >= 0 and new_i < height and new_j >= 0 and new_j < width):
                    continue

                count += board[new_i][new_j]

            if count < 4:
                total += 1

print(total)