import sys
import heapq
input = sys.stdin.readline

inf = 2500
D = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def bfs(x, y):
    global M
    Q = [[0, x, y]]
    while Q:
        dis, x, y = heapq.heappop(Q)
        for dx, dy in D:
            tx, ty = x + dx, y + dy
            if 0 <= tx < N and 0 <= ty < N and dis + 1 < vl[ty][tx] and ml[ty][tx] != '1':
                if ml[ty][tx] == 'K':
                    if vl[ty][tx] == inf:
                        vl[ty][tx] = dis + 1
                        heapq.heappush(Q, [0, tx, ty])
                else:
                    vl[ty][tx] = dis + 1
                    heapq.heappush(Q, [dis+1, tx, ty])
    s = 0
    for j in range(N):
        for i in range(N):
            if ml[j][i] == 'K':
                if vl[j][i] == inf:
                    print(-1)
                    return
                s += vl[j][i]
    print(s)


def init():
    for j in range(N):
        for i in range(N):
            if ml[j][i] == 'S':
                bfs(i, j)
                return


N, M = map(int, input().split())
ml = [input() for _ in range(N)]
vl = [[inf for _ in range(N)] for _ in range(N)]
init()
