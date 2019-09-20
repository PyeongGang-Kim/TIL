import sys
sys.stdin = open('최소생산비용.txt')


def sel(k=0, s = 0):
    global r
    if k == N:
        if r > s:
            r = s
    elif s >= r:
        return
    for i in range(k, N):
        arr[i], arr[k] = arr[k], arr[i]
        sel(k+1, s+nl[k][arr[k]])
        arr[i], arr[k] = arr[k], arr[i]


T = int(input())
for t in range(1, T+1):
    N = int(input())
    nl = [list(map(int, input().split())) for _ in range(N)]
    arr = [i for i in range(N)]
    r = 99*15
    sel()
    print('#{} {}'.format(t, r))