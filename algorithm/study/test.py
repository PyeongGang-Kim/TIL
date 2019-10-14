from collections import deque
import sys
sys.stdin = open(
    'asdf.txt'
)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def check():

    for y in range(6):
        for x in range(11, -1, -1):
            if nxm[x][y] == '.':
                for z in range(x-1, -1, -1):
                    if nxm[z][y] != '.':
                        nxm[x][y] = nxm[z][y]
                        nxm[z][y] = '.'
                        break


def bfs(x, y, alpa, cnt):
    Q = deque()
    Q.append((x, y))
    visited[x][y] = 1
    cc[0] += 1
    while Q:
        x, y = Q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < 12 and 0 <= ny < 6:
                if nxm[nx][ny] == alpa and visited[nx][ny] == 0:
                    cc[0] += 1
                    visited[nx][ny] = 1
                    Q.append((nx, ny))


nxm = [list(input())for _ in range(12)]
ans = [[0 for _ in range(6)]for _ in range(12)]
answer = [0 for _ in range(20)]
depth = 0
while 1:
    depth += 1

    for x in range(12):
        for y in range(6):
            visited = [[0 for _ in range(6)] for _ in range(12)]
            if nxm[x][y] != '.' and visited[x][y] == 0:
                cc = [0]
                bfs(x, y, nxm[x][y], 1)

                if cc[0] >= 4:
                    answer[depth] += 1
                    for i in range(12):
                        for j in range(6):
                            if visited[i][j] == 1:
                                ans[i][j] = 1

    for x in range(12):
        for y in range(6):
            if ans[x][y] == 1:
                nxm[x][y] = '.'
                ans[x][y] = 0

    check()
    if answer[depth] == 0:
        break

print(depth-1)