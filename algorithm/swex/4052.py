for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    nl = [[x for x in map(int, input().split())] for _ in range(N)]
    nl.sort(key=lambda x: (-x[1], -x[0]))
    D = [0] * (M+2)
    for a, b, c in nl:
        if D[a] < D[b+1] + c:
            tmp = D[b+1] + c
            while a and D[a] < tmp:
                D[a] = tmp
                a -= 1
    print('#{} {}'.format(tc, D[1]))
