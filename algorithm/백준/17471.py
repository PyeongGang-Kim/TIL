import sys
from collections import deque


N = 6
chk = False
N = int(sys.stdin.readline())
nl = list(map(int, sys.stdin.readline().split()))
ml = {i: set() for i in range(N)}
r = sum(nl)
for n in range(N):
    tmp = list(map(int, sys.stdin.readline().split()))
    for k in range(1, len(tmp)):
        ml[n].add(tmp[k]-1)
for i in range(1, 1 << (N-1)):
    le, ri = set(), set()
    for j in range(N):
        if i & (1 << j):
            le.add(j)
        else:
            ri.add(j)
    vl = [False for _ in range(N)]
    tmpp = le.pop()
    vl[tmpp] = True
    Q = deque([tmpp])
    cnt = 0
    s1 = nl[tmpp]
    while Q:
        p = Q.popleft()
        for k in ml[p].intersection(le):
            if not vl[k]:
                Q.append(k)
                vl[k] = True
                cnt += 1
                s1 += nl[k]
    if cnt == len(le):
        tmpp = ri.pop()
        Q = deque([tmpp])
        vl[tmpp] = True
        cnt = 0
        s2 = nl[tmpp]
        while Q:
            p = Q.popleft()
            for k in ml[p].intersection(ri):
                if not vl[k]:
                    Q.append(k)
                    vl[k] = True
                    cnt += 1
                    s2 += nl[k]
        if cnt == len(ri):
            r = min(abs(s1-s2), r)
            chk = True

if chk:
    print(r)
else:
    print(-1)


