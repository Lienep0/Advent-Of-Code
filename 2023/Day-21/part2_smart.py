directions = [(-1, 0), (0, -1), (0, 1), (1, 0)] # ^, <, >, v

board, startpos = [], None
with open("input.txt", "r") as f:
    for i, line in enumerate(f):
        line = line.strip()
        for j, char in enumerate(line):
            if not startpos and char == "S":
                startpos = (i, j)
        board.append(line.replace("S", "."))

STEPS = len(board) * 3 + len(board) // 2 #26501365
MOD = (startpos[0] + startpos[1] + STEPS) % 2

full_plot_odd_tiles = 7082 # (precomputed using part 1)
print(STEPS // len(board), STEPS % len(board))

full_squares_completed = ((2*((STEPS // len(board)) - 1) + 1)**2 + 1) // 2
border_squares = (4 * (STEPS // len(board)))

# 590_309_300_938_806 : too high