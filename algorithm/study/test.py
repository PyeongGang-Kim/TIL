def check():
    for i in range(1, N + 1):
        nl = [inf] * (N + 1)
        vl = [False] * (N + 1)
        nl[1] = 0
        vl[1] = True
        n = N - 1

        while n:
            for i in range(1, N+1):
                if vl[i]:
                    for j in range(1, N+1):
                        if ml[i][j] + nl[i] < nl[j]:
                            nl[j] = ml[i][j] + nl[i]
                            vl[j] = True
                    vl[i] = False

            n -= 1

        for i in range(1, N+1):
            if nl[i] != inf:
                for j in range(1, N+1):
                    if ml[i][j] + nl[i] < nl[j]:
                        return True
    return False


inf = 0xfffffff
TC = int(input())

while TC:
    TC -= 1

    N, M, W = map(int, input().split())
    ml = [[inf for _ in range(N+1)] for _ in range(N+1)]
    while M:
        M -= 1
        S, E, T = map(int, input().split())
        ml[S][E] = min(ml[S][E], T)
    while W:
        W -= 1
        S, E, T = map(int, input().split())
        ml[S][E] = min(ml[S][E], -T)

    if check():
        print('YES')
    else:
        print('NO')