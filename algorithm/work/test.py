import sys
sys.stdin = open('asdf.txt')


def L(i=0, s=0):
    global r
    if s >= B:
        if r > s:
            r = s
        return
    if s == B:
        return
    if i == N:
        return
    L(i+1, s+nl[i])
    L(i+1, s)


for t in range(1, int(input())+1):
    N, B = map(int, input().split())
    r = 10000*N
    nl = list(map(int, input().split()))
    L()
    print('#{} {}'.format(t, r-B))