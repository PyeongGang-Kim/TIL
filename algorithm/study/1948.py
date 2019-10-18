import sys
from collections import deque
'''
시작점과 도착점 찾는 방법
간선 입력 받을 때 도착, 시작 비짓체크를 한다.
시작점부터 최대값 갱신하면서 bfs

도착점부터 최대값인지 확인하면서 bfs
최대값일때만 큐에 넣고 카운팅한다.

'''
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
ran = range(N+1)
nl = [0 for _ in ran]
sl = [[] for _ in ran]
el = [[] for _ in ran]
for m in range(M):
    s, e, d = map(int, sys.stdin.readline().split())
    sl[s].append([e, d])
    el[e].append([s, d])
S, E = map(int, sys.stdin.readline().split())
Q = deque([S])
while Q:
    s = Q.popleft()
    for v in sl[s]:
        tmp = nl[s] + v[1]
        if nl[v[0]] < tmp:
            Q.append(v[0])
            nl[v[0]] = tmp
r = 0
vl = [False for _ in ran]
Q.append(E)
while Q:
    e = Q.popleft()
    for v in el[e]:
        if nl[v[0]] + v[1] == nl[e]:
            if not vl[v[0]]:
                vl[v[0]] = True
                Q.append(v[0])
            r += 1
print(nl[E])
print(r)