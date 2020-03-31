T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    D = [0] * (B+1)
    nl = list(map(int, input().split()))
    for n in nl:
        for i in range(B, n-1, -1):
            D[i] = max(D[i-n] + 1, D[i])

    print('Case #{}: {}'.format(tc, D[-1]))
