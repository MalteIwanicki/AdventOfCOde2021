counter = 0
lines = open("1/input.txt", "r").readlines()
depths = [int(line) for line in lines]

last_depth = depths[0]
for depth in depths:
    if int(depth) > int(last_depth):
        counter += 1
    last_depth = depth
print(counter)
