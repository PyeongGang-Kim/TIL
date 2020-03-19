import heapq
import sys
input = sys.stdin.readline

def bfs(s, e):
    vl = [0xfffffff] * (N+1)
    Q = [[0, s]]
    while Q:
        dis, pos = heapq.heappop(Q)
        if vl[pos] < dis:
            continue
        if pos == e:
            return dis
        for npos in range(1, N+1):
            if nl[pos][npos]:
                ndis = dis + nl[pos][npos]
                if ndis < vl[npos]:
                    vl[npos] = ndis
                    heapq.heappush(Q, [ndis, npos])
    return 0xfffffff


N, E = map(int, input().split())
nl = [[0]*(N+1) for _ in range(N+1)]
while E:
    E -= 1
    a, b, c = map(int, input().split())
    if nl[a][b]:
        nl[a][b] = min(nl[a][b], c)
    else:
        nl[a][b] = c
    if nl[b][a]:
        nl[b][a] = min(nl[b][a], c)
    else:
        nl[b][a] = c
p1, p2 = map(int, input().split())

r1 = bfs(1, p1) + bfs(p1, p2) + bfs(p2, N)
r2 = bfs(1, p2) + bfs(p2, p1) + bfs(p1, N)
if r1 <= r2:
    if r1 < 0xfffffff:
        print(r1)
    else:
        print(-1)
else:
    if r2 < 0xfffffff:
        print(r2)
    else:
        print(-1)