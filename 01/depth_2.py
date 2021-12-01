depths = [int(line.strip('\n')) for line in open("data", 'r').readlines()]
previous_triple_sum = 0
count = 0
triple = []

for i in range(len(depths)):
    try:
        triple = depths[i:i+3]
    except IndexError:
        print('Not enough values to make a triple')
        exit(0)
    triple_sum = sum(triple)
    if 0 < previous_triple_sum < triple_sum:
        count += 1
    previous_triple_sum = triple_sum

print(count)
