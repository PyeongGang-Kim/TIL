import sys
sys.stdin = open('asdf.txt')


def c(d = 0, s = 1):
    global r
    if d == N:
        if s > r:
            r = s
        return
    if s <= r:

        return
    for i in range(N):
        if not vl[i]:
            vl[i] = 1
            c(d+1, s*nl[d][i])
            vl[i] = 0


T = int(input())
for t in range(1, T+1):
    N = int(input())
    nl = [[0.01*i for i in list(map(int, input().split()))] for _ in range(N)]
    vl = [0]*N
    r = 0
    arr = [0] * N
    c()
    print('#{} {:6f}'.format(t, r*100))