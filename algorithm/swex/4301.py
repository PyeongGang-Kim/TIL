T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    t1, t2 = divmod(N, 4)
    t3 = 0
    if t2 == 3:
        t3 = 2
    else:
        t3 = t2
    l1 = t1*2 + t3
    if t2 == 3:
        t3 = 1
    else:
        t3 = 0
    l2 = t1*2 + t3


    t1, t2 = divmod(M, 4)

    if t2 <= 2:
        t3 = l1 * t2
    else:
        t3 = l1 * 2 + l2


    r = t1 * (l1 + l2) * 2 + t3
    print('#{} {}'.format(t, r))


