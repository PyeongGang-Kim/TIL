from collections import deque

N, M, H = map(int, input().split())
nl = [[[H, [0, 0, 0, 0]] for _ in range(M)] for _ in range(N)]
tmp = list(map(int, input().split()))
chks = set()
for m in range(M):
    nl[0][m][1][0] = tmp[m]
    if tmp[m] != -1:
        chks.add((m, 0))
        nl[0][m][0] = min(nl[0][m][0], tmp[m])
for n in range(1, N):
    tmp = list(map(int, input().split()))
    for m in range(M):
        nl[n-1][m][1][2] = tmp[m]
        nl[n][m][1][0] = tmp[m]
tmp = list(map(int, input().split()))
for m in range(M):
    nl[-1][m][1][2] = tmp[m]
    if tmp[m] != -1:
        chks.add((m, N-1))
        nl[-1][m][0] = min(nl[-1][m][0], tmp[m])

for n in range(N):
    tmp = list(map(int, input().split()))
    nl[n][0][1][3] = tmp[0]
    if tmp[0] != -1:
        chks.add((0, n))
        nl[n][0][0] = min(nl[n][0][0], tmp[0])

    for m in range(1, M):
        nl[n][m-1][1][1] = tmp[m]
        nl[n][m][1][3] = tmp[m]
    nl[n][-1][1][1] = tmp[-1]
    if tmp[-1] != -1:
        chks.add((M-1, n))
        nl[n][-1][0] = min(nl[n][-1][0], tmp[-1])


dr = [[0, -1], [1, 0], [0, 1], [-1, 0]]
for x, y in chks:
    Q = deque([[x, y, nl[y][x][0]]])
    while Q:
        x, y, h = Q.popleft()
        if nl[y][x][0] < h:
            continue
        for idx, height in enumerate(nl[y][x][1]):
            if height != -1:
                tx, ty = x + dr[idx][0], y + dr[idx][1]
                if 0 <= tx < M and 0 <= ty < N and nl[ty][tx][0] > height and (h <= height or nl[ty][tx][0] > h):
                    tmp = max(height, h)
                    nl[ty][tx][0] = tmp
                    Q.append([tx, ty, tmp])
r = 0
for j in range(N):
    for i in range(M):
        r += nl[j][i][0]
print(r)