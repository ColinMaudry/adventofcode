depths = [line.strip('\n') for line in open("data", 'r').readlines()]
previous_depth = 0
count = 0

for depth in depths:
    depth = int(depth)
    if 0 < previous_depth < depth:
        count += 1
    previous_depth = depth


print(count)
