commands = open("input.txt", "r").readline().strip()
boxes = [[] for _ in range(256)]

def hash(s):
    total = 0
    for char in s:
        total += ord(char)
        total *= 17
        total %= 256
    return total

#run the hash on the label to calculate the box
#   if the opsign is -:
#       - remove the lens from the box if it's present 
#   if the opsign is =:
#       the number after is the focal length
#       if the lens is present in the box:
#           get that lens a new focal length
#       else:
#           add the lens with that focal length to the box

for command in commands.split(','):
    if "=" in command:
        command_label, command_focal_length = command.split("=")
        h = hash(command_label)
        for i in range(len(boxes[h])):
            if command_label == boxes[h][i][0]:
                boxes[h][i][1] = int(command_focal_length)
                break
        else:
            boxes[h].append([command_label, int(command_focal_length)])
    else:
        command_label = command[:-1]
        h = hash(command_label)
        for i in range(len(boxes[h])):
            if command_label == boxes[h][i][0]:
                boxes[h] = boxes[h][:i] + boxes[h][i + 1:]
                break

total = 0
for i in range(len(boxes)):
    for j in range(len(boxes[i])):
        total += (i + 1) * (j + 1) * boxes[i][j][1]
print(total)