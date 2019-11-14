from collections import deque
import sys
input = sys.stdin.readline

Q = deque()
dr = [[0, 1], [0, -1], [-1, 0], [1, 0]]
T = int(input())
r = []
for _ in range(T):
    M, N, K = map(int, input().split())
    nl = [[True for _ in range(M)] for _ in range(N)]
    cnt = 0
    while cnt < K:
        cnt += 1
        x, y = map(int, input().split())
        nl[y][x] = False

    cnt = 0
    for j in range(N):
        for i in range(M):
            if not nl[j][i]:
                cnt += 1
                nl[j][i] = True
                Q.append([i, j])
                while Q:
                    x, y = Q.popleft()
                    for dx, dy in dr:
                        tx, ty = x + dx, y + dy
                        if 0 <= tx < M and 0 <= ty < N and not nl[ty][tx]:
                            nl[ty][tx] = True
                            Q.append([tx, ty])
    r.append(cnt)
print('\n'.join(map(str, r)))