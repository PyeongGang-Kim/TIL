T = int(input())
for t in range(1, T+1):
    N = int(input())
    nl = [list(map(int, input().split())) for _ in range(N)]
    for j in range(N):
        for i in range(N):
            if not nl[j][i]:
                nl[j][i] = 0xfffffff

    for k in range(N):
        for j in range(N):
            for i in range(N):
                nl[j][i] = min(nl[j][i], nl[j][k] + nl[k][i])

    r = 0
    for j in range(N):
        for i in range(N):
            if i != j:
                r = max(nl[j][i], r)
    print('\n'.join(map(str, nl)))
    print('#{} {}'.format(t, r))