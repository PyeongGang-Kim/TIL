import sys
sys.stdin = open('이진탐색.txt')


def bf(l, r, c):
    m = (l+r)//2
    if nl[m] == n:
        return True
    if nl[m] > n:
        if c == -1:
            return False
        return bf(l, m-1, -1)
    else:
        if c == 1:
            return False
        return bf(m+1, r, 1)


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    nl = set(map(int, input().split()))
    ml = set(map(int, input().split())).intersection(nl)
    nl = sorted(list(nl))
    cnt = 0
    for n in ml:
        if bf(0, len(nl)-1, 0):
            cnt += 1
    print('#{} {}'.format(t, cnt))