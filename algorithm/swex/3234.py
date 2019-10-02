import itertools

def dfs(l = 0, r = 0, d = 0):
    global cnt
    if r > l:
        return
    if d == N:
        cnt += 1
        return
    dfs(l+dl[d], r, d+1)
    dfs(l, r+dl[d], d+1)


T = int(input())
for t in range(1, T+1):
    N = int(input())
    nl = list(map(int, input().split()))
    vl = [0 for _ in range(N)]
    cnt = 0
    for dl in itertools.permutations(nl):
        dfs()
    print('#{} {}'.format(t, cnt))