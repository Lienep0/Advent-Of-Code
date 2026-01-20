from heapq import *

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_"

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
    valid_targets = set(range(i + 1))

highest_z_positions = [[(0, -1) for _ in range(max_coords[1] + 1)] for _ in range(max_coords[0] + 1)]
def print_board():
    print("positions, ids")
    for i in range(len(highest_z_positions)):
        for k in [highest_z_positions[i][l][0] for l in range(len(highest_z_positions[i]))]:
            print(k, end=" ")
        print(end=" ")
        for k in [highest_z_positions[i][l][1] for l in range(len(highest_z_positions[i]))]:
            print(letters[k], end=" ")
        print()
    print()
    
while bricks:
    brick = heappop(bricks)
    if brick.direction in [2, -1]:
        bottom = brick.blocks[0]
        landing_pos = highest_z_positions[bottom[0]][bottom[1]]
        # only one bricks supports vertical bricks so they can't be disintegrated
        # print(f"removed {letters[highest_z_positions[bottom[0]][bottom[1]][1]]} because of {letters[brick.id]}")
        valid_targets -= {landing_pos[1]}
        # that vertical brick becomes the new vertical
        highest_z_positions[bottom[0]][bottom[1]] = (landing_pos[0] + brick.highest_z - brick.lowest_z + 1, brick.id)
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
        # rebuild stack
        for block in brick.blocks:
            highest_z_positions[block[0]][block[1]] = (max_z + 1, brick.id)
        # eliminate invalid targets
        if len(supports) == 1:
            # print(f"removed {letters[supports[0]]} because of {letters[brick.id]}")
            valid_targets -= {supports.pop()}
    #print_board()

print(len(valid_targets))

# get all bricks as a set of positions, order the bricks by lowest z
# get a board of all the highest z brick positions, starting at all zeroes
# make the bricks fall using the brick's "bottom side"
# for each brick, get the list of bricks that can make it fall. if there is only one, that brick cannot be disintegrated