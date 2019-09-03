import sys
sys.stdin = open('asdf.txt')

def dfs(i, j, d, cnt=3):
    if nl[j][i] < 3:
        tx, ty = i + dr[d][0], j + dr[d][1]
        if mov(tx, ty, i, j, d, cnt):
            vl[ty][tx] = 1
            dfs(tx, ty, d, cnt + 1)
            vl[ty][tx] = 0
    else:
        td = (d + 1) % 4
        tx, ty = i + dr[td][0], j + dr[td][1]
        if mov(tx, ty, i, j, td, cnt):
            vl[ty][tx] = 1
            dfs(tx, ty, td, cnt + 1)
            vl[ty][tx] = 0

        td = (d - 1) % 4
        tx, ty = i + dr[td][0], j + dr[td][1]
        if mov(tx, ty, i, j, td, cnt):
            vl[ty][tx] = 1
            dfs(tx, ty, td, cnt + 1)
            vl[ty][tx] = 0


def mov(tx, ty, i, j, d, cnt):
    global result
    if 0 <= tx < N and 0 <= ty < N and nl[ty][tx] and not vl[ty][tx]:
        if [tx, ty] == [0, 0]:
            if [i, j] == S and sd == d:
                if result > cnt:
                    result = cnt
        else:
            return True
    return False


dr = [[0, -1], [1, 0], [0, 1], [-1, 0]]  # 시계방향 상우하좌
T = int(input())
for t in range(1, T + 1):
    N = int(input())
    nl = [list(map(int, input().split())) for _ in range(N)]
    cl = [[[[], [], [], []] for _ in range(N)] for _ in range(N)]
    vl = [[0 for _ in range(N)] for _ in range(N)]
    if nl[0][0] == 1 or nl[0][0] == 2:
        S = [1, 0]
        sd = 3
    else:
        S = [0, 1]
        sd = 0
    if nl[N - 1][N - 1] == 1 or nl[N - 1][N - 1] == 2:
        G = [N - 2, N - 1]
        gd = 3
    else:
        G = [N - 1, N - 2]
        gd = 0
    result = N ** 2
    chk = 0
    vl[G[1]][G[0]] = 1
    dfs(G[0], G[1], gd)
    vl[G[1]][G[0]] = 0

    print('#', end='')
    print(t, result)