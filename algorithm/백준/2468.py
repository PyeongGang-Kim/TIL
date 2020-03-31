from collections import deque


def bfs(i, j):
    vl[j][i] = 1
    Q = deque([[i, j]])
    while Q:
        x, y = Q.popleft()
        for dx, dy in D:
            tx, ty = x + dx, y + dy
            if 0 <= tx < N and 0 <= ty < N and not vl[ty][tx] and nl[ty][tx] > k:
                vl[ty][tx] = 1
                Q.append([tx, ty])


D = [[0, 1], [0, -1], [1, 0], [-1, 0]]

N = int(input())
nl = [list(map(int, input().split())) for _ in range(N)]

r = 1
tmp = set()
for i in range(N):
    for j in range(N):
        tmp.add(nl[j][i])

for k in tmp:
    cnt = 0

    vl = [[0 for _ in range(N)] for _ in range(N)]
    for j in range(N):
        for i in range(N):
            if not vl[j][i]:
                if nl[j][i] > k:
                    bfs(i, j)
                    cnt += 1
                else:
                    vl[j][i] = 1
    if cnt > r:
        r = cnt
print(r)