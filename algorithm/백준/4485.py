import heapq
import sys
input = sys.stdin.readline

def bfs():
    nl = [list(map(int, input().split())) for _ in range(N)]
    vl = [[0xfffffff] * N for _ in range(N)]
    vl[0][0] = nl[0][0]
    Q = [[nl[0][0], 0, 0]]
    while Q:
        dis, x, y = heapq.heappop(Q)
        if x == N - 1 and y == N - 1:
            return dis
        if dis > vl[y][x]:
            continue
        for dx, dy in d:
            tx, ty = x + dx, y + dy
            if 0 <= tx < N and 0 <= ty < N:
                ndis = dis + nl[ty][tx]
                if ndis < vl[ty][tx]:
                    vl[ty][tx] = ndis
                    heapq.heappush(Q, [ndis, tx, ty])


d = [[0, 1], [0, -1], [-1, 0], [1, 0]]
r = []
i = 1
N = int(input())
while N:
    r.append('Problem {}: {}'.format(i, str(bfs())))
    i += 1
    N = int(input())
print('\n'.join(r))