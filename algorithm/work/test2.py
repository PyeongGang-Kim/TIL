T = int(input())
for t in range(1, T+1):
    N, A, B = map(int, input().split())
    n = 1
    while n**2<N:
        n += 1
    result = B*(N-1)
    for r in range(1, N):
        for c in range(r, N//r+1):
            tmp = A*abs(r-c)+B*(N-r*c)
            if tmp < result:
                result = tmp
    print('#{} {}'.format(t,result))


