from collections import deque

def bfs(i, j):
    global r, r2
    Q = deque([[2, i, j]])
    vl[j][i] = 1
    while Q:
        dis, x, y = Q.popleft()
        for dx, dy in D:
            tx, ty = x + dx, y + dy
            if 0 <= tx < N and 0 <= ty < N and dis > vl[ty][tx] and nl[y][x] - 1 == nl[ty][tx]:
                vl[ty][tx] = dis
                if dis > r:
                    r = dis
                    r2 = nl[ty][tx]
                elif dis == r:
                    if r2 > nl[ty][tx]:
                        r2 = nl[ty][tx]
                Q.append([dis+1, tx, ty])



D = [[0, 1], [0, -1], [1, 0], [-1, 0]]
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nl = [list(map(int, input().split())) for _ in range(N)]
    vl = [[0 for _ in range(N)] for _ in range(N)]
    r = 0
    r2 = 0xfffffff
    for j in range(N):
        for i in range(N):
            if not vl[j][i]:
                bfs(i, j)
    print('#{} {} {}'.format(tc, r2, r))