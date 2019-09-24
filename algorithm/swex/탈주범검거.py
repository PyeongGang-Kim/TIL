import sys
sys.stdin = open('탈주범검거.txt')
from collections import deque


def bfs():
    cnt = 0
    Q = deque([[sx, sy, 1]])
    vl[sy][sx] = 1
    cnt += 1
    while Q:
        x, y, tim = Q.popleft()
        if tim == L:
            return cnt
        for d in D[nl[y][x]]:
            tx, ty = x + dr[d][0], y + dr[d][1]
            if 0 <= tx < M and 0 <= ty < N and not vl[ty][tx] and (d + 2) % 4 in D[nl[ty][tx]]:
                vl[ty][tx] = 1
                cnt += 1
                Q.append([tx, ty, tim + 1])
    return cnt


D = [
    [],
    [0, 1, 2, 3],
    [0, 2],
    [1, 3],
    [0, 1],
    [1, 2],
    [2, 3],
    [0, 3]
]
dr = [[0, -1], [1, 0], [0, 1], [-1, 0]]


T = int(input())
for t in range(1, T + 1):
    N, M, sy, sx, L = map(int, input().split())
    nl = [list(map(int, input().split())) for _ in range(N)]
    vl = [[0 for _ in range(M)] for _ in range(N)]
    print('#{} {}'.format(t, bfs()))