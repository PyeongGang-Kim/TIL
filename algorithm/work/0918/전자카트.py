import sys
sys.stdin = open('전자카트.txt')


def perm(k = 0):
    global r
    if k == N-1:
        print(arr)
        tmp = 0
        tmp2 = 0
        for i in arr:
            tmp += ml[tmp2][i-1]
            tmp2 = i-1
        tmp += ml[arr[-1]-1][0]
        if tmp < r:
            r = tmp
        return
    for j in range(k, N-1):
        arr[j], arr[k] = arr[k], arr[j]
        perm(k+1)
        arr[j], arr[k] = arr[k], arr[j]


T = int(input())
for t in range(1, T+1):
    N = int(input())
    ml = [list(map(int, input().split())) for _ in range(N)]
    arr = [i for i in range(2, N+1)]
    r = 0xfffffff
    perm()
    print('#{} {}'.format(t, r))