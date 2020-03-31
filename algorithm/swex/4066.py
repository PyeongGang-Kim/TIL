inf = 0xfffffff
for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    nl = [[inf for _ in range(N+1)] for _ in range(N+1) ]
    for i in range(1, N+1):
        nl[i][i] = 0
    while M:
        M -= 1
        a, b, c = map(int, input().split())
        nl[a][b] = min(nl[a][b], c)
    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                nl[i][j] = min(nl[i][j], nl[i][k]+nl[k][j])
    r = []
    for j in range(1, N+1):
        for i in range(1, N+1):
            if nl[j][i] == inf:
                r.append('-1')
            else:
                r.append(str(nl[j][i]))

    print('#{} {}'.format(tc, ' '.join(r)))