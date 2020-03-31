import sys
input = sys.stdin.readline


def findset(i):
    if cl[i] == -1:
        return i
    cl[i] = findset(cl[i])
    return cl[i]

r = []
m, n = map(int, input().split())
while m and n:
    ml = []
    s = 0
    while n:
        n -= 1
        a, b, c = map(int, input().split())
        ml.append([c, a, b])
        s += c
    ml.sort()
    cl = [-1] * m
    for c, a, b in ml:
        t1, t2 = findset(a), findset(b)
        if t1 != t2:
            cl[t2] = t1
            s -= c
    m, n = map(int, input().split())
    r.append(str(s))
print('\n'.join(r))