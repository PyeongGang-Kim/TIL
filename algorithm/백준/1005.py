from collections import deque
import sys

input = sys.stdin.readline


def to():
    Q = deque([])
    for i in range(1, N + 1):
        if not cntl[i][0]:
            Q.append([i, cntl[i][1]])
    while Q:
        idx, dis = Q.popleft()
        for nidx in ml[idx]:
            cntl[nidx][0] -= 1
            cntl[nidx][2] = max(cntl[nidx][2], dis)
            if not cntl[nidx][0]:
                if nidx == W:
                    cntl[nidx][1] += cntl[nidx][2]
                    return
                Q.append([nidx, cntl[nidx][1] + cntl[nidx][2]])


T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    cntl = [[]] + [[0, i, 0] for i in map(int, input().split())]
    ml = [[] for _ in range(N + 1)]
    while K:
        K -= 1
        a, b = map(int, input().split())
        cntl[b][0] += 1
        ml[a].append(b)
    W = int(input())
    to()
    print(cntl[W][1])