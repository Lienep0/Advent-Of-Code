from heapq import *

board = [list(map(int, line.strip())) for line in open("input.txt", "r").readlines()]
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)] # ^, >, v, <

def djkstra(si, sj, ei, ej):
    best_distances = {}
    prevs = {}

    # distance, i, j, direction, t
    min_heap = [(0, si, sj, -1, 0)]

    while min_heap:
        distance, i, j, d, t = heappop(min_heap)

        # Can't move more than 10 blocks in the same drection
        if t > 10: 
            continue

        for nd, (di, dj) in enumerate(directions):
            if d != -1:
                # Don't allow reversing
                if (d + 2) % 4 == nd:
                    continue

                # Can't turn unless t >= 4
                if t < 4 and d != nd:
                    continue

            ni, nj = i + di, j + dj
            if 0 <= ni < len(board) and 0 <= nj < len(board[0]):
                nt = 1 if nd != d else t + 1
                new_distance = distance + board[ni][nj]

                if best_distances.get((ni, nj, nd, nt), float('inf')) > new_distance:
                    best_distances[(ni, nj, nd, nt)] = new_distance
                    prevs[(ni, nj, nd, nt)] = (i, j, d, t)
                    heappush(min_heap, (new_distance, ni, nj, nd, nt))

    best = float('inf')
    for t in range(4, 11):
        for d in range(4):
            candidate = best_distances.get((ei, ej, d, t), float('inf'))
            if candidate < best:
                best = candidate
                candidate_stats = (ei, ej, d, t)
    
    path = {(ei, ej): candidate_stats[3]}
    current = prevs[candidate_stats]
    while current:
        path[(current[0], current[1])] = current[3]
        current = prevs.get(current)

    return best, path

answer, path = djkstra(0, 0, len(board)-1, len(board[0])-1)

for i in range(len(board)):
    for j in range(len(board[0])):
        if (i, j) in path:
            print('\033[92m', end="")
        print(str(board[i][j]) + '\033[0m', end="")
    print()
print(answer)
