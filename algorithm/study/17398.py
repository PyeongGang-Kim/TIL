import sys
input = sys.stdin.readline
sys.setrecursionlimit(200000)

def unionfind(i):
    if not cl.get(i):
        cl[i] = [i, 1]
    if cl[i][0] != i:
        cl[i][0] = unionfind(cl[i][0])
        return cl[i][0]
    else:
        return i


N, M, Q = map(int, input().split())
nl = [list(map(int, input().split())) if _ else [] for _ in range(M+1)]
vl = [False for _ in range(M+1)]
ql = [int(input().strip()) for _ in range(Q)]
for idx in ql:
    vl[idx] = True
cl = dict()
for idx in range(1, M+1):
    if not vl[idx]:
        t1, t2 = unionfind(nl[idx][0]), unionfind(nl[idx][1])
        if t1 != t2:
            cl[t2][0] = t1
            cl[t1][1] += cl[t2][1]

r = 0
for idx in reversed(ql):
    t1, t2 = unionfind(nl[idx][0]), unionfind(nl[idx][1])
    if t1 != t2:
        cl[t2][0] = t1
        r += cl[t1][1] * cl[t2][1]
        cl[t1][1] += cl[t2][1]
print(r)
