from collections import deque
def bfs():
    Q = deque([[0, 0, 1]])
    while Q:
        x, y, cnt = Q.popleft()
        if x == gx and y == gy:
            return cnt
        for dx, dy in dr:
            tx, ty = x + dx, y + dy
            if 0 <= tx < M and 0 <= ty < N and nl[ty][tx] == '1' and not vl[ty][tx]:
                Q.append([tx, ty, cnt+1])
                vl[ty][tx] = 1


dr = [[0, 1], [0, -1], [1, 0], [-1, 0]]
N, M = map(int, input().split())
nl = [input() for _ in range(N)]
vl = [[0 for _ in range(M)] for _ in range(N)]
gx, gy = M-1, N-1
print(bfs())