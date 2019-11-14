import sys
from collections import deque

dr =  [[1, -2], [2, -1], [2, 1], [1, 2], [-1, 2], [-2, 1], [-2, -1], [-1, -2]]
dr2 = [[0, 1], [0, -1], [1, 0], [-1, 0]]
Q = deque()
K = int(input())
M, N = map(int, input().split())
nl = [list(map(int, input().split())) for _ in range(N)]
vl = [[0 for _ in range(M)] for _ in range(N)]
EX = M-1
EY = N-1
r = 0xffffffff
Q.append([0, 0, K+1, 0])
vl[0][0] = K+1
while Q:
    x, y, k, d = Q.popleft()
    if x == EX and y == EY:
        r = min(r, d)
        break
    for dx, dy in dr2:
        tx, ty = x + dx, y + dy
        if 0 <= tx < M and 0 <= ty < N and not nl[ty][tx] and vl[ty][tx] < k:
            Q.append([tx, ty, k, d+1])
            vl[ty][tx] = k
    if k > 1:
        k -= 1
        for dx, dy in dr:
            tx, ty = x + dx, y + dy
            if 0 <= tx < M and 0 <= ty < N and not nl[ty][tx] and vl[ty][tx] < k:
                Q.append([tx, ty, k, d+1])
                vl[ty][tx] = k
if r == 0xffffffff:
    r = -1
print(r)