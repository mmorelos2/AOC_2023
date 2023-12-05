file = open('input.txt', 'r')
total = 0
for line in file:
    l = 0
    r = len(line) - 1
    while not line[l].isnumeric():
        l += 1
    while not line[r].isnumeric():
        r -= 1
    num = int(line[l] + line[r])
    total += num

print(total)