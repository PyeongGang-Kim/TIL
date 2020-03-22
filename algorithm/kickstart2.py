T = int(input())
for tc in range(1, T+1):
    N, K, P = map(int, input().split())
    D = [[0 for _ in range(P+1)] for _ in range(N+1)]
    nl = [list(map(int, input().split())) for _ in range(N)]
    for n in range(1, N+1):
        tmp = 0
        for k in range(1, K+1):
            tmp += nl[n-1][k-1]
            for j in range(k, P+1):
                D[n][j] = max(D[n-1][j-k] + tmp, D[n-1][j], D[n][j])
    print('Case #{}: {}'.format(tc, D[-1][-1]))