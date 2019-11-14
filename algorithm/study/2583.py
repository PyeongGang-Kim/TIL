from collections import deque
import sys
input = sys.stdin.readline

Q = deque()

M, N, K = map(int, input().split())
k = 0
nl = [[False for _ in range(N)] for _ in range(M)]
while k < K:
    k += 1
    lx, ly, rx, ry = map(int, input().split())
    for j in range(ly, ry):
        for i in range(lx, rx):
            nl[j][i] = True
r = []
dr = [[0, 1], [0, -1], [1, 0], [-1, 0]]
for j in range(M):
    for i in range(N):
        if not nl[j][i]:
            Q.append([i, j])
            nl[j][i] = True
            cnt = 1
            while Q:
                x, y = Q.popleft()
                for dx, dy in dr:
                    tx, ty = x + dx, y + dy
                    if 0 <= tx < N and 0 <= ty < M and not nl[ty][tx]:
                        Q.append([tx, ty])
                        nl[ty][tx] = True
                        cnt += 1
            r.append(cnt)
r.sort()
print(len(r))
print(' '.join(map(str, r)))


