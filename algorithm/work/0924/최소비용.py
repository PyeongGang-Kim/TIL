import sys
from collections import deque
sys.stdin = open('최소비용.txt')


D = [[0, 1], [0, -1], [1, 0], [-1, 0]]
T = int(input())
for t in range(1, T+1):
    N = int(input())
    nl = [list(map(int, input().split())) for _ in range(N)]
    vl = [[1000*10000 for _ in range(N)] for _ in range(N)]
    Q = deque([[0, 0, 0]])
    vl[0][0] = 0
    while Q:
        x, y, f = Q.popleft()
        if vl[y][x] < f:
            continue
        for dx, dy in D:
            tx, ty = x + dx, y + dy
            if 0 <= tx < N and 0 <= ty < N:
                if nl[y][x] < nl[ty][tx]:
                    tmp = f + 1 + nl[ty][tx] - nl[y][x]
                    if vl[ty][tx] > tmp:
                        Q.append([tx, ty, tmp])
                        vl[ty][tx] = tmp
                else:
                    tmp = f + 1
                    if vl[ty][tx] > tmp:
                        Q.append([tx, ty, tmp])
                        vl[ty][tx] = tmp
    print('#{} {}'.format(t, vl[N-1][N-1]))