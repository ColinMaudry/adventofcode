moves = [line.strip('\n').split(" ") for line in open("data", 'r').readlines()]

horizontal = 0
vertical = 0

for move in moves:
    distance = int(move[1])
    if move[0] == 'forward':
        horizontal += distance
    elif move[0] == 'up':
        vertical -= distance
    else:
        vertical += distance

print("""
horizontal = {}
vertical = {}
product = {}
""".format(horizontal, vertical, horizontal * vertical))
