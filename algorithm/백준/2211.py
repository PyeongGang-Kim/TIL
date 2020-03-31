import sys
import heapq
input = sys.stdin.readline


N, M = map(int, input().split())
ml = [[] for _ in range(N+1)]
vl = [0] * (N+1)
while M:
    M -= 1
    a, b, c = map(int, input().split())
    ml[a].append([c, a, b])
    ml[b].append([c, b, a])

vl[1] = 1
Q = ml[1][:]
heapq.heapify(Q)
r = []
while Q:
    dis, idx1, idx2 = heapq.heappop(Q)
    if not vl[idx2]:
        vl[idx2] = 1
        r.append('{} {}'.format(idx1, idx2))
        for tdis, tidx1, tidx2 in ml[idx2]:
            if not vl[tidx2]:
                heapq.heappush(Q, [dis + tdis, idx2, tidx2])
print(len(r))
print('\n'.join(r))