def findstart():
    for j in range(M):
        for i in range(N):
            if nl[j][i] == 2:
                return i, j


def dfs(x, y, dep = 0, pos = 0):
    if vl2[pos][y][x]<= dep:
        return
    vl2[pos][y][x] = dep
    if nl[y][x] == 3:
        if not pos:
            global cnt
            cnt = min(cnt, dep)
        return
    for i in range(4):
        tx, ty = x + D[i][0], y + D[i][1]
        if 0<=tx<N and 0<=ty<M and nl[ty][tx] and not vl[ty][tx]:
            vl[ty][tx] = 1
            dfs(tx, ty, dep+1, tr[pos][i])
            vl[ty][tx] = 0


tr = [
    [3, 4, 1, 2],
    [0, 1, 5, 1],
    [2, 0, 2, 5],
    [5, 3, 0, 3],
    [4, 5, 4, 0],
    [1, 2, 3, 4],
]
D = [[0, -1], [-1, 0], [0, 1], [1, 0]]
inf = 0xfffffff
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    nl = [list(map(int, input().split())) for _ in range(M)]
    vl = [[0 for _ in range(N)] for _ in range(M)]
    vl2 = [[[inf for _ in range(N)] for _ in range(M)] for _ in range(6)]
    S = findstart()
    vl[S[1]][S[0]] = 1
    cnt = 0xfffffff
    dfs(*S)
    if cnt!=0xfffffff:
        print('#{} {}'.format(tc, cnt))
    else:
        print('#{} {}'.format(tc, -1))
