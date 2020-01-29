import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def dfs(x, y):
    if vl[y][x]:
        return vl[y][x]
    else:
        tmp = 0
        for dx, dy in D:
            tx, ty = x + dx, y + dy
            if 0 <= tx < N and 0 <= ty < N and nl[y][x] < nl[ty][tx]:
                tmp = max(tmp, dfs(tx, ty))
        vl[y][x] = tmp + 1
        return vl[y][x]


D = [[0, 1], [0, -1], [-1, 0], [1, 0]]
N = int(input())
nl = [list(map(int, input().split())) for _ in range(N)]
vl = [[0 for _ in range(N)] for _ in range(N)]
r = 0
for j in range(N):
    for i in range(N):
        r = max(r, dfs(i, j))
print(r)