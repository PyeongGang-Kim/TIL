import sys
from collections import deque


def dfs(i):
    r = []
    st = [i]
    while st:
        idx = st.pop()
        if not vl[idx]:
            vl[idx] = 1
            r.append(str(idx))
        for v in range(len(nl[idx])-1, -1, -1):
            if not vl[nl[idx][v]]:
                st.append(nl[idx][v])
    print(' '.join(r))


def bfs(i):
    r = []
    q = deque([i])
    while q:
        idx = q.popleft()
        if not vl[idx]:
            vl[idx] = 1
            r.append(str(idx))
        for v in nl[idx]:
            if not vl[v]:
                q.append(v)
    print(' '.join(r))


N, M, V = map(int, sys.stdin.readline().strip().split())
nl = {i: [] for i in range(1, N+1)}
for m in range(M):
    v1, v2 = map(int, sys.stdin.readline().strip().split())
    nl[v1].append(v2)
    nl[v2].append(v1)

for i in range(1, N+1):
    nl[i].sort()
vl = [0 for _ in range(N+1)]
dfs(V)
vl = [0 for _ in range(N+1)]
bfs(V)