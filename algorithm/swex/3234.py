def dfs(l = 0, r = 0, d = 0):
    global cnt
    if d == N:
        cnt += 1
        return
    for i in range(N):
        if not vl[i]:
            vl[i] = 1
            dfs(l+nl[i], r, d+1)
            if l >= r + nl[i]:
                dfs(l, r+nl[i], d+1)
            vl[i] = 0


T = int(input())
for t in range(1, T+1):
    N = int(input())
    nl = list(map(int, input().split()))
    vl = [0 for _ in range(N)]
    cnt = 0

    dfs()
    print('#{} {}'.format(t, cnt))