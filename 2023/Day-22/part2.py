from heapq import *
from collections import defaultdict, deque
from copy import deepcopy

class Brick():
    def __init__(self, id, pos1 : tuple[int], pos2 : tuple[int]):
        self.id = id
        for k in range(3):
            if pos1[k] != pos2[k]:
                self.direction = k
                break
        else:
            self.direction = -1

        self.lowest_z = pos1[2]
        self.highest_z = pos2[2]
        
        if self.direction == -1:
            self.blocks = [pos1]
        else:
            self.blocks = []
            for i in range(pos2[self.direction] + 1 - pos1[self.direction]):
                new_block = list(pos1)
                new_block[self.direction] += i
                self.blocks.append(tuple(new_block))
    
    def __lt__(self, other):
        return self.lowest_z < other.lowest_z

bricks = []
with open("input.txt", "r") as f:
    for i, line in enumerate(f.readlines()):
        pos1, pos2 = (tuple(map(int, x.split(","))) for x in line.strip().split("~"))
        if i == 0:
            max_coords = list(pos2)
        else:
            for j in range(3):
                max_coords[j] = max(max_coords[j], pos2[j])
        heappush(bricks, Brick(i, pos1, pos2))
    number_of_bricks = i
    valid_targets = set(range(i + 1))

highest_z_positions = [[[0, -1] for _ in range(max_coords[1] + 1)] for _ in range(max_coords[0] + 1)]
bricks_supported = defaultdict(set)
bricks_that_support_you = defaultdict(set)

while bricks:
    brick = heappop(bricks)
    if brick.direction in [2, -1]:
        bottom = brick.blocks[0]
        support_id = highest_z_positions[bottom[0]][bottom[1]][1]

        valid_targets -= {support_id}
        bricks_supported[support_id] |= {brick.id}
        bricks_that_support_you[brick.id] |= {support_id}

        # that vertical brick becomes the new vertical
        highest_z_positions[bottom[0]][bottom[1]][0] += brick.highest_z - brick.lowest_z + 1
        highest_z_positions[bottom[0]][bottom[1]][1] = brick.id
    else:
        # calculate fall
        max_z, supports = 0, set()
        for block in brick.blocks:
            support_z, support_id = highest_z_positions[block[0]][block[1]]
            if support_z > max_z:
                max_z = support_z
                supports = {support_id}
            elif support_z == max_z:
                supports |= {support_id}

        if len(supports) == 1:
            valid_targets -= supports
    
        # rebuild stack
        for block in brick.blocks:
            highest_z_positions[block[0]][block[1]] = [max_z + 1, brick.id]
        # add supports
        for support in supports:
            bricks_supported[support] |= {brick.id}
        bricks_that_support_you[brick.id] |= supports

total = 0
for i in set(range(i + 1)) - valid_targets:
    number_of_fallen_bricks = 0
    copy_that_support = deepcopy(bricks_that_support_you)

    to_check = deque([(i, bricks_supported[i])])
    while to_check:
        fallen, targets = to_check.popleft()
        for target in targets:
            copy_that_support[target] -= {fallen}
            if len(copy_that_support[target]) == 0:
                copy_that_support[target] = {-1}
                number_of_fallen_bricks += 1
                to_check.append((target, bricks_supported[target]))

    total += number_of_fallen_bricks

print(total)