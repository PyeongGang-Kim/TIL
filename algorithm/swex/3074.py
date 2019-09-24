def find(l, r):
    m = (l+r)//2
    num = 0
    for i in range(N):
        num += m // nl[i]
    if num < M:
        return find(m, r)
    else:
        m1 = m-1
        num = 0
        for i in range(N):
            num += m1 // nl[i]
        if num < M:
            return m
        else:
            return find(l, m)


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    nl = [0 for _ in range(N)]
    for i in range(N):
        nl[i] = int(input())

    print('#{} {}'.format(t, find(1, nl[0]*M)))