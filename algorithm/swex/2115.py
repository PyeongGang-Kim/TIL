


T = int(input())
for t in range(1, T+1):
    N, M, C = map(int, input().split())
    nl = [list(map(int, input().split())) for _ in range(N)]
    nl2 = [[0 for _ in range(N)] for _ in range(N)]
    for j in range(N):
        for i in range(N):
            nl2[j][i] = nl[j][i] ** 2

    ml = []

    for j in range(N):
        for i in range(N-M+1):
            tmpr = 0
            for k in range(1, 1<<M):
                tmps = 0
                chk = True
                for l in range(M):
                    if k & (1 << l):
                        tmps += nl[j][i+l]
                        if tmps > C:
                            chk = False
                            break
                tmps = 0
                if chk:
                    for l in range(M):
                        if k & (1 << l):
                            tmps += nl2[j][i+l]
                tmpr = max(tmpr, tmps)
            ml.append(tmpr)
        for m in range(M-1):
            ml.append(0)
    r = 0
    for i in range(N**2-M+1):
        for j in range(i+M, N**2):
            r = max(r, ml[i] + ml[j])
    print('#{} {}'.format(t, r))