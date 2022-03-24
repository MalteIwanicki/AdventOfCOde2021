counter = 0
lines = open("day1/input.txt", "r").readlines()

depths = [int(line) for line in lines]
queue = depths[:3]
for depth in depths[3:]:
    sum_old = sum(queue)
    queue.pop(0)
    queue.append(depth)
    if sum_old < sum(queue):
        counter += 1
print(counter)
