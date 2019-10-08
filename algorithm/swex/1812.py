'''
미완성

'''
T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    nl = list(map(int, input().split()))

    m = M**2
    r = 1
    for i in nl:
        m -= (2**i)**2
        if m < 0:
            m += M**2
            r += 1
    print(r)