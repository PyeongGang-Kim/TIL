def bfs(i, j):
    global maxcnt
    vl[j][i] = True
    Q = [[i, j, 0]]
    idx = 0
    idx2 = 1
    if nl[j][i] and M:
        cnt = 1
    else:
        cnt = 0
    while idx < idx2:
        while idx < idx2:
            x, y, d = Q[idx]
            for dx, dy in dr:
                tx, ty = x + dx, y + dy
                if d < N and 0 <= tx < N and 0 <= ty < N and not vl[ty][tx]:
                    vl[ty][tx] = True
                    Q.append([tx, ty, d+1])
                    if nl[ty][tx]:
                        cnt += 1
            idx += 1
        if M*cnt >= 2*d**2 + 6*d + 5:
            maxcnt = max(maxcnt, cnt)
        idx2 = len(Q)


dr = [[0, 1], [0, -1], [1, 0], [-1, 0]]
T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    nl = [list(map(int, input().split())) for _ in range(N)]
    maxcnt = 1
    for j in range(N):
        for i in range(N):
            vl = [[False for _ in range(N)] for _ in range(N)]
            bfs(i, j)
    print('#{} {}'.format(t, maxcnt))