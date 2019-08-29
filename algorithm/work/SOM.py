import sys
sys.stdin = open('asdf.txt')


def sm(x, ar):
    if x == N-1:
        ar = ar[N//2:]+ar[:N//2]
        return ar
    if x <= N//2-1:
        tmp1 = ar[0:N//2]
        tmp2 = ar[N//2:]
    else:
        x = N - 1 - x
        tmp2 = ar[0:N//2]
        tmp1 = ar[N//2:]
    ar = []
    for j in range(N//2-x):
        ar.append(tmp1.pop(0))
    for xx in range(x):
        ar.append(tmp2.pop(0))
        ar.append(tmp1.pop(0))
    for j in range(N//2-x):
        ar.append(tmp2.pop(0))
    return ar


def bfs(ar, d=0):
    front = 0
    Q = [[ar, d]]
    while front < len(Q):
        ar, d = Q[front]
        front += 1
        if d > 5:
            return 6
        if ck(ar):
            return d
        for i in range(1, N):
            Q.append([sm(i, ar), d+1])


def ck(ar):
    chk = 0
    for i in range(len(ar)-1):
        if ar[i] < ar[i+1]:
            chk = 1
            break
    if not chk:
        return True
    chk = 0
    for i in range(len(ar)-1):
        if ar[i] > ar[i+1]:
            chk = 1
            break
    if not chk:
        return True
    return False


T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    r = bfs(arr[:])
    if r == 6:
        r = -1
    print('#{} {}'.format(t, r))
