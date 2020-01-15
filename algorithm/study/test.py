def cal(i, j):
    if i == j:
        if i > 0:
            return (2 * i + 1) ** 2
        if i < 0:
            return (- 2 * i + 1) ** 2 + 4 * i
        else:
            return 1
    elif i > j:
        tmp = max(abs(j), abs(i))
        return (2 * tmp + 1) ** 2 - 6 * tmp - i - j
    else:
        tmp = max(abs(j), abs(i))
        return (2 * tmp + 1) ** 2 - (tmp - i + tmp - j)

r1, c1, r2, c2 = map(int, input().split())

r = []
tmp2 = c1
maxNum = max(cal(c1, r1), cal(c1, r2), cal(c2, r2), cal(c2, r1))
maxNum = len(str(maxNum))
while r1 <= r2:
    tmp = []
    c1 = tmp2
    while c1 <= c2:
        t = str(cal(c1, r1))
        t = (maxNum - len(t)) * ' ' + t
        tmp.append(t)
        c1 += 1
    r.append(' '.join(tmp))
    r1 += 1
print('\n'.join(r))