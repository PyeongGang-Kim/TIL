for t in range(1, int(input())+1):
    W, H, N = map(int, input().split())
    r = 0
    if N == 1:
        input()
    else:
        nl = []
        for i in range(N):
            nl.append(list(map(int, input().split())))
        for i in range(N-1):
            t1, t2 = nl[i+1][0] - nl[i][0], nl[i+1][1] - nl[i][1]
            if t1 >= 0 and t2 >= 0:
                r += max(t1, t2)
            elif t1 < 0 and t2 < 0:
                r -= min(t1, t2)
            else:
                r += abs(t1) + abs(t2)
    print('#{} {}'.format(t, r))