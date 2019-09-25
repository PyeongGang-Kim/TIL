import sys
sys.stdin = open('asdf.txt')
from collections import deque


def find(i, j):
    cnt = 1
    while 1:
        chk = 0
        chk1 = 0
        for dx, dy in d:
            tx, ty = i + dx, j + dy
            if 0 <= tx < N and 0 <= ty < N and nl[j][i] + 1 == nl[ty][tx]:
                i = tx
                j = ty
                chk = 1
                break
        if not chk:
            break
    vl[j][i] = cnt
    while 1:
        chk = 0
        for dx, dy in d:
            tx, ty = i + dx, j + dy
            if 0 <= tx < N and 0 <= ty < N and nl[j][i] - 1 == nl[ty][tx]:
                i = tx
                j = ty
                chk = 1
                break
        if not chk:
            break
        cnt += 1
        vl[j][i] = cnt


d = [[0, 1], [0, -1], [1, 0], [-1, 0]]
T = int(input())
for t in range(1, T + 1):
    r = 0
    n = 0
    N = int(input())
    nl = [list(map(int, input().split())) for _ in range(N)]
    vl = [[0 for _ in range(N)] for _ in range(N)]
    for j in range(N):
        for i in range(N):
            if not vl[j][i]:
                find(i, j)

    print('#{} {} {}'.format(t, n, r))