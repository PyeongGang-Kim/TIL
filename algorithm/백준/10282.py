import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
while T:
    T -= 1
    n, d, c = map(int, input().split())
    vl = [0x7fffffff] * (n+1)
    vl[c] = 0

    D = {i: [] for i in range(1, n+1)}

    while d:
        d -= 1
        a, b, s = map(int, input().split())
        D[b].append([a, s])
    Q = deque([[0, c]])
    while Q:
        dis, pos = Q.popleft()
        if vl[pos] < dis:
            continue
        for npos, tdis in D[pos]:
            tmp = dis + tdis
            if tmp < vl[npos]:
                vl[npos] = tmp
                Q.append([tmp, npos])

    r = 0
    cnt = 0
    for i in range(1, n+1):
        if not vl[i] == 0x7fffffff:
            cnt += 1
            r = max(r, vl[i])

    print(cnt, r)