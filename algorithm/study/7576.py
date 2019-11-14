from collections import deque


M, N = map(int, input().split())
nl = [list(map(int, input().split())) for _ in range(N)]
ccnt = 0
Q = deque()
chk = False
dr = [[0, 1], [0, -1], [1, 0], [-1, 0]]
for j in range(N):
    for i in range(M):
        if nl[j][i] == 0:
            ccnt += 1
        elif nl[j][i] == 1:
            Q.append([i, j])

tcnt = -1
if ccnt:
    vl = [[False for _ in range(M)] for _ in range(N)]
    while Q:
        tcnt += 1
        f = 0
        r = len(Q)
        while f < r:
            x, y = Q.popleft()
            f += 1
            for dx, dy in dr:
                tx, ty = x + dx, y + dy
                if 0 <= tx < M and 0 <= ty < N and not vl[ty][tx] and nl[ty][tx] != -1:
                    if nl[ty][tx]:
                        Q.append([tx, ty])
                        vl[ty][tx] = True
                    else:
                        Q.append([tx, ty])
                        ccnt -= 1
                        vl[ty][tx] = True
    if ccnt:
        result = -1
    else:
        result = tcnt
else:
    result = 0
print(result)

