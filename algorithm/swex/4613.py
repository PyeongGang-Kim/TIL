'''
각 줄을 W, R, B로 칠할 때 몇번씩 칠해야하는지 저장을 해 놓는다.
0부터 i까지, i+1부터 j까지 j+1부터 N 까지 각각 색칠한다고 생각하고
포문을 통해 접근한다.

'''

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    nl = [input() for _ in range(N)]
    W, R, B = [0 for _ in range(N)], [0 for _ in range(N)], [0 for _ in range(N)]
    for j in range(N):
        for i in range(M):
            if nl[j][i] == 'W':
                R[j] += 1
                B[j] += 1
            elif nl[j][i] == 'R':
                W[j] += 1
                B[j] += 1
            else:
                W[j] += 1
                R[j] += 1
    r = N * M
    for i in range(N-2):
        for j in range(i+1, N-1):
            tmp = 0
            for tm in range(i+1):
                tmp += W[tm]
            for tm in range(i+1, j+1):
                tmp += B[tm]
            for tm in range(j+1, N):
                tmp += R[tm]
            r = min(r, tmp)
    print('#{} {}'.format(t, r))