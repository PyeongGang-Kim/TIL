import sys
sys.stdin = open('최소합.txt')
from collections import deque


def bfs():
    x, y = 0, 0
    Q = deque([[x, y]])
    vl[y][x] = nl[y][x]
    while Q:
        x, y = Q.popleft()
        for dx, dy in d:
            tx = x + dx
            ty = y + dy
            if 0 <= tx < N and 0 <= ty < N:
                if vl[ty][tx] > vl[y][x] + nl[ty][tx]:
                    vl[ty][tx] = vl[y][x] + nl[ty][tx]
                    Q.append([tx, ty])


d = [[1, 0], [0, 1]]
T = int(input())
for t in range(1, T+1):
    N = int(input())
    nl = [list(map(int, input().split())) for _ in range(N)]
    vl = [[0xfffffffff for _ in range(N)] for _ in range(N)]
    bfs()
    print('#{} {}'.format(t, vl[N-1][N-1]))