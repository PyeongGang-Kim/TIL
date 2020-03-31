def dfs(i, visited, dep=1):
    global r
    r = max(dep, r)
    for idx in ml[i]:
        if not visited&(1<<idx):
            dfs(idx, visited | (1 << idx), dep+1)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    ml = [[] for _ in range(N+1)]
    vl = [0] * (N+1)
    r = 0
    while M:
        M -= 1
        a, b = map(int, input().split())
        ml[a].append(b)
        ml[b].append(a)
    for i in range(1, N+1):
        dfs(i, 1<<i)
    print('#{} {}'.format(tc, r))