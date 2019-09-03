import sys
sys.stdin = open('asdf.txt')
'''
총 인원이 0명인 경우
결과는 0이다

총 인원이 1명 이상일 때
M<=1이면 1이다

M>1일 경우
K = 2부터 K^2 + (K-1)^2 <= M*총인원을 만족하는 최대 K까지
각 각의 좌표들에서 해당 K까지 더하면서 중복된 값들 최대값 찾는다
K^2 + (K-1)^2 <= M*최대값을 만족하면
결과에 최대값을 저장한다.

K의 최대값은 2*N보다 작아야한다.
'''


def f(x, y, k):
    for i in range(k-1):
        if 0<=x+i<N and 0<=y-k+1+i:
            vl[y-k+1+i][x+i] += 1
        if 0<=x+k-1-i<N and 0<=y+i<N:
            vl[y+i][x+k-1-i] += 1
        if 0<=x-i<N and 0<=y+k-1-i<N:
            vl[y+k-1-i][x-i] += 1
        if 0<=x-k+1+i<N and 0<=y-i<N:
            vl[y-i][x-k+1+i] += 1


def ck(k):
    global result
    tmp = 0
    for j in range(N):
        for i in range(N):
            if vl[j][i] >= tmp:
                tmp = vl[j][i]
    if k**2 + (k-1)**2 <= M * tmp:
        result = tmp


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    nl = [list(map(int, input().split())) for _ in range(N)]
    vl = [[0 for _ in range(N)] for _ in range(N)]
    np = 0
    hl = []
    result = 0
    for j in range(N):
        for i in range(N):
            if nl[j][i]:
                vl[j][i] = 1
                np += 1
                hl.append([i, j])
    if np == 0:
        pass
    elif M<1:
        pass
    else:
        result = 1
        K = 3
        while K^2 + (K-1)^2 <= M*np:
            K += 1
        if K > 2*N:
            K = 2*N
        for k in range(2, K):
            for h in hl:
                f(h[0], h[1], k)
            ck(k)
    print('#{} {}'.format(t, result))