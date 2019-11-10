import sys
sys.stdin = open('asdf.txt')

def bfs(x, y):
    global check, cnt, result
    q = []
    visited[x][y] += 1
    q.append((x, y))
    while len(q) != 0:
        x, y = q.pop(0)
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            elif visited[nx][ny] != 0:
                continue
            elif visited[nx][ny] == 0 and data[nx][ny] == 0:
                visited[x][y] += 1
                continue
            elif visited[nx][ny] == 0 and data[nx][ny] != 0:
                visited[nx][ny] += 1
                q.append((nx, ny))

    cnt += 1

    c1 = 0
    c2 = 0
    for n in range(N):
        for m in range(M):
            if data[n][m]:
                c1 += 1
            if visited[n][m]:
                c2 += 1

    if c1 != c2:
        result = cnt
        check = 0

    for n in range(N):
        for m in range(M):
            if data[n][m] > 0:
                data[n][m] -= visited[n][m] - 1
                if data[n][m] <= 0:
                    data[n][m] = 0
                    c1 -= 1

    if c1 == 0:
        result = 0

N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
cnt = 0
flag = 0
check = 1
x = 0
y = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


while check:
    for i in range(N):
        if flag == 1:
            flag = 0
            break
        for j in range(M):
            if data[i][j] != 0:
                x = i
                y = j
                flag = 1
                break
    visited = [[0] * M for _ in range(N)]
    bfs(x, y)




print(result)