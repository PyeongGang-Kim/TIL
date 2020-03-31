def dfs(i):
    tmp = 1
    for idx in range(1, N+1):
        if ml[i][idx] and not vl[idx]:
            vl[idx] = True
            tmp += dfs(idx)
    return tmp


def dfs2(i):
    tmp = 1
    for idx in range(1, N+1):
        if ml[idx][i] and not vl[idx]:
            vl[idx] = True
            tmp += dfs2(idx)
    return tmp


N, M = map(int, input().split())
ml = [[False for _ in range(N+1)] for _ in range(N+1)]
cl = [False for i in range(N+1)]
while M:
    M -= 1
    a, b = map(int, input().split())
    ml[a][b] = True
tmp = N // 2 + 1
cnt = 0
for i in range(1, N+1):
    vl = [False for _ in range(N+1)]
    vl[i] = True
    if dfs(i) > tmp or dfs2(i) > tmp:
        cnt += 1
print(cnt)