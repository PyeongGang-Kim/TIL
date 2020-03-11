

numbers = []
opers = []
tmp = ''
for s in '1T2D3D#':
    if s.isnumeric():
        tmp += s
    else:
        if tmp:
            numbers.append(int(tmp))
            tmp = ''
        opers.append(s)
print(numbers)
print(opers)
idx = -1
for oper in opers:
    if oper in 'SDT':
        idx += 1
        if oper == 'D':
            numbers[idx] **= 2
        elif oper == 'T':
            numbers[idx] **= 3
    if oper == '*':
        numbers[idx] *= 2
        if idx:
            numbers[idx-1] *= 2
    if oper == '#':
        numbers[idx] *= -1
print(sum(numbers))