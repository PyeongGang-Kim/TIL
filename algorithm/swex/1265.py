T = int(input())
for t in range(1, T+1):
    N, P = map(int, input().split())
    t1, t2 = divmod(N, P)
    nl = [t1 for _ in range(P)]
    i = 0
    t3 = t1*P
    if t2:
        while True:
            nl[i] += 1
            i += 1
            if t3 + i == N:
                break

    r = 1
    for n in nl:
        r *= n
    print('#{} {}'.format(t,r))

