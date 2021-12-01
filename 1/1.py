counter = 0
lines = open("input.txt", "r").readlines()
last = lines[0]
for line in lines:
    if int(line) > int(last):
        counter += 1
    last = line
print(counter)
