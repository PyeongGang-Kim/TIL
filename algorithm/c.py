def mkt(i = 1):
    i2 = 2 * i
    if i2 + 1 < len(nl):
        nl[i] = mkt(i2).union(mkt(i2+1))
    elif i2 * 2 < len(nl):
        nl[i] = mkt(i2)
    else:
        return nl[i]
    return nl[i]

def inst(i, s):
    i = i + n - 1
    nl[i] = set(s)
    while i>1:
        i //= 2
        if i * 2 + 1 < len(nl):
            nl[i] = nl[i*2+1].union(nl[i*2])
        elif i * 2 < len(nl):
            nl[i] = nl[i*2]

def fnd(l, r, L, R, i = 1):
    if i >= len(nl):
        return set()
    m = (L + R) // 2
    if l <= L and r >= R:
        return nl[i]
    elif L <= r <= R:
        return fnd(l, r, L, m, i*2).union(fnd(l, r, m+1, R, i*2+1))
    elif L <= l <= R:
        return fnd(l, r, L, m, i*2).union(fnd(l, r, m+1, R, i*2+1))
    else:
        return set()




A = input()
B = [set(i) for i in A]
N = int(input())
n = 1

while n < N:
    n *= 2
nl = [set() for _ in range(n)] + B
mkt()
for i in range(N):
    o, idx, c = input().split()
    if o == '1':
        inst(int(idx), c)
    else:
        l = int(idx)
        r = int(c)
        print(len(fnd(l, r, 1, n)))