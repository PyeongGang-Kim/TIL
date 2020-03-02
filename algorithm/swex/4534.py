def cntf(i, c):
    if not len(ml[i]):
        return 1
    vl[i] = 1
    #내가 흰색인 경우
    if c:
        if nl[i][1]:
            vl[i] = 0
            return nl[i][1]
        tmp = 1
        for idx in ml[i]:
            if not vl[idx]:
                tmp2 = cntf(idx, 1)
                tmp2 %= mo
                tmp2 += cntf(idx, 0)
                tmp2 %= mo
                tmp *= tmp2
                tmp %= mo
        nl[i][1] = tmp
        vl[i] = 0
        return tmp
    #검은색인 경우
    else:
        if nl[i][0]:
            vl[i] = 0
            return nl[i][0]
        tmp = 1
        for idx in ml[i]:
            if not vl[idx]:
                tmp *= cntf(idx, 1)
                tmp %= mo
        nl[i][0] = tmp
        vl[i] = 0
        return tmp

mo = 1000000007
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ml = [[] for _ in range(N+1)]
    nl = [[0, 0] for _ in range(N+1)]
    vl = [0] * (N+1)
    K = N - 1
    while K:
        K -= 1
        a, b = map(int, input().split())
        ml[a].append(b)
        ml[b].append(a)
    r = cntf(1, 0)
    r += cntf(1, 1)
    r %= mo

    print('#{} {}'.format(tc, r))
