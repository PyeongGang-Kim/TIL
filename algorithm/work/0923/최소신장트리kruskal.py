import sys
sys.stdin = open('최소신장트리.txt')


def unionfind(n):
    if cl[n] != -1:
        cl[n] = unionfind(cl[n])
    else:
        return n
    return cl[n]


def kruskal():
    global r
    for li in nl:
        t1 = unionfind(li[0])
        t2 = unionfind(li[1])
        if t1 != t2:
            cl[t2] = t1
            r += li[2]


for t in range(1, int(input())+1):
    V, E = map(int, input().split())
    nl = []
    r = 0
    nl = [list(map(int, input().split())) for _ in range(E)]
    cl = [-1 for _ in range(V+1)]
    nl.sort(key=lambda x: x[2])
    kruskal()
    print('#{} {}'.format(t, r))