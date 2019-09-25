import sys
sys.stdin = open('등산로조성.txt')


def dfs(i, j, k=1, cnt=1):
    global r
    if r < cnt:
        r = cnt
    vl[j][i] = 1
    for dx, dy in d:
        tx, ty = i+dx, j+dy
        if 0 <= tx < N and 0 <= ty < N and not vl[ty][tx]:
            if nl[j][i] > nl[ty][tx]:
                vl[ty][tx] = 1
                dfs(tx, ty, k, cnt+1)
                vl[ty][tx] = 0
            else:
                if k:
                    if nl[ty][tx] - K < nl[j][i]:
                        tmp = nl[ty][tx]
                        nl[ty][tx] = nl[j][i]-1
                        vl[ty][tx] = 1
                        dfs(tx, ty, 0, cnt+1)
                        nl[ty][tx] = tmp
                        vl[ty][tx] = 0
    vl[j][i] = 0


d = [[0, 1], [0, -1], [1, 0], [-1, 0]]
T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    nl = [list(map(int, input().split())) for _ in range(N)]
    vl = [[0 for _ in range(N)] for _ in range(N)]
    r = 0
    maxn = 0
    maxl = []
    for j in range(N):
        for i in range(N):
            if nl[j][i] > maxn:
                maxn = nl[j][i]
                maxl = [[i, j]]
            elif nl[j][i] == maxn:
                maxl.append([i,j])
    for i, j in maxl:
        dfs(i, j)
    print('#{} {}'.format(t, r))