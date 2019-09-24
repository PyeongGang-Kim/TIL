import sys
from collections import deque
sys.stdin = open('최소이동거리.txt')


T = int(input())
for t in range(1, T+1):
    N, E = map(int, input().split())
    nl = {i: [] for i in range(N+1)}
    for _ in range(E):
        s, g, d = map(int, input().split())
        nl[s].append([g, d])
    vl = [10000000 for _ in range(N+1)]
    Q = deque([[0, 0]])
    vl[0] = 0
    while Q:
        p, d = Q.popleft()
        if vl[p] < d:
            continue
        for i, d2 in nl[p]:
            if vl[i] > d + d2:
                vl[i] = d + d2
                Q.append([i, d+d2])
    print('#{} {}'.format(t, vl[N]))