import sys
sys.stdin = open('그룹나누기.txt')


def unionfind(x):
    if cl[x] == -1:
        return x
    else:
        tmp = unionfind(cl[x])
        cl[x] = tmp
        return tmp


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    nl = list(map(int, input().split()))
    cl = [-1 for _ in range(N+1)]
    cnt = N
    for i in range(M):
        t1 = unionfind(nl[i*2])
        t2 = unionfind(nl[i*2+1])
        if t1 != t2:
            cl[t2] = t1
            cnt -= 1
    print('#{} {}'.format(t, cnt))
