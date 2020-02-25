import sys
input = sys.stdin.readline


def findset(i):
    if cl[i]:
        cl[i] = findset(cl[i])
        return cl[i]
    return i


n, m = map(int, input().split())
cl = [0] * (n+1)
s = 0
cnt = n-2
cnt2 = 0
r = []
while m:
    m -= 1
    a, b = map(int, input().split())
    t1, t2 = findset(a), findset(b)
    if t1 != t2:
        cl[t2] = t1
        cnt -= 1
if cnt:
    input()
    k = 1
    ml = []
    while k < n:
        k += 1
        tmp = list(map(int, input().split()))
        for i in range(k, n):
            ml.append([tmp[i], k, i+1])
    ml.sort()
    for dis, idx1, idx2 in ml:
        t1, t2 = findset(idx1), findset(idx2)
        if t1 != t2:
            cl[t2] = t1
            cnt -= 1
            s += dis
            cnt2 += 1
            r.append('{} {}'.format(idx1, idx2))
        if not cnt:
            break

else:
    tmp2 = n
    while tmp2:
        tmp2 -= 1
        input()
print(s, cnt2)
print('\n'.join(r))