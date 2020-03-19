import sys
import heapq
input = sys.stdin.readline
def bfs():
    if N == 1 and M == 1:
        return 0
    while Q:
        dis, x, y = heapq.heappop(Q)
        for dx, dy in d:
            tx, ty = x + dx, y + dy
            if tx == M-1 and ty == N-1:
                return dis

            if 0 <= tx < M and 0 <= ty < N:

                ndis = dis
                if nl[ty][tx] == '1':
                    ndis += 1

                if ndis < vl[ty][tx]:
                    vl[ty][tx] = ndis
                    heapq.heappush(Q, [ndis, tx, ty])


M, N = map(int, input().split())
nl = [input() for _ in range(N)]
vl = [[0xfffffff]*M for _ in range(N)]
vl[0][0] = 0
Q = [[0, 0, 0]]
d = [[0, 1], [0, -1], [1, 0], [-1, 0]]

print(bfs())