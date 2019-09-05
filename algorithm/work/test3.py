import sys
sys.stdin = open('asdf.txt')


def bfs():
    Q = [(0, 0)]
    while Q:
        x, y = Q.pop(0)
        h = tl[y][x]
        if x == N-1 and y == N-1:
            continue
        for dx, dy in dr:
            tx, ty = x+dx, y+dy
            if 0 <= tx < N and 0 <= ty < N:
                if tl[ty][tx] > h + nl[ty][tx]:
                    Q.append((tx, ty))
                    tl[ty][tx] = h + nl[ty][tx]


dr = [[0, 1], [1, 0], [-1, 0], [0, -1]]
T = int(input())
for t in range(1, T+1):
    N = int(input())
    nl = [[int(i) for i in list(input())] for _ in range(N)]
    tmp = 0
    for i in range(N):
        for j in range(N):
            tmp += nl[j][i]
    tl = [[tmp for _ in range(N)] for _ in range(N)]
    tl[0][0] = 0
    bfs()
    print('#{} {}'.format(t, tl[N-1][N-1]))