'''
음의 사이클이 있더라도
음의 사이클이 있는 곳에서 도착점까지 갈 수가 없으면 Gee가 아니다

'''


import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    Q = deque([E])
    while Q:
        p = Q.popleft()
        for i in range(N):
            if ml3[p][i] and not vl2[i]:
                if vl[i]:
                    return False
                vl2[i] = 1
                Q.append(i)
    return True


inf = 0xfffffffffff
N, S, E, M = map(int, input().split())
ml = []
while M:
    M -= 1
    s, e, t = map(int, input().split())
    ml.append([s, e, t])

ml2 = list(map(int, input().split()))

nl = [inf for _ in range(N)]
nl[S] = 0
n = N
while n:
    n -= 1
    update = False
    for s, e, t in ml:
        if nl[s] != inf:
            if nl[e] > nl[s] + t - ml2[e]:
                nl[e] = nl[s] + t - ml2[e]
                update = True
    if not update:
        break
if nl[E] != inf:
    if update:
        vl = [0] * N
        vl2 = [0] * N
        ml3 = [[0 for _ in range(N)] for _ in range(N)]
        for s, e, t in ml:
            ml3[e][s] = 1
            if nl[s] != inf:
                if nl[e] > nl[s] + t - ml2[e]:
                    nl[e] = nl[s] + t - ml2[e]
                    vl[s], vl[e] = 1, 1
        if bfs():
            print(-nl[E]+ml2[S])
        else:
            print("Gee")
    else:
        print(-nl[E]+ml2[S])
else:
    print("gg")