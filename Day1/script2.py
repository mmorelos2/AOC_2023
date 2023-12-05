def get_num(s):
    if s[0].isnumeric():
        return int(s[0])
    if len(s) >= 3:
        s_check = s[:3]
        if s_check == 'one':
            return 1
        if s_check == 'two':
            return 2
        if s_check == 'six':
            return 6
    if len(s) >= 4:
        s_check = s[:4]
        if s_check == 'four':
            return 4
        if s_check == 'five':
            return 5
        if s_check == 'nine':
            return 9
    if len(s) >= 5:
        s_check = s[:5]
        if s_check == 'three':
            return 3
        if s_check == 'seven':
            return 7
        if s_check == 'eight':
            return 8
    return None

file = open('input.txt', 'r')
total = 0
for line in file:
    l = 0
    l_num = None
    r = len(line) - 1
    r_num = None

    while not l_num:
        l_num = get_num(line[l:])
        l += 1
    
    while not r_num:
        r_num = get_num(line[r:])
        r -= 1

    total += int(str(l_num) + str(r_num))

print(total)