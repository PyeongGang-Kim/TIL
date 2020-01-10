from collections import deque
def bfs(x, y):
    global result
    vl2 = [[False for _ in range(C)] for _ in range(R)]
    vl2[y][x] = True
    Q = deque([[x, y]])
    while Q:
        x, y = Q.popleft()
        for dx, dy in D:
            tx, ty = x + dx, y + dy
            if 0 <= tx < C and 0 <= ty < R and nl[ty][tx] == '.' and not vl2[ty][tx]:
                vl2[ty][tx] = True
                Q.append([tx, ty])

    Q.append([x, y, 0])
    while Q:
        x, y, dis = Q.popleft()
        for dx, dy in D:
            tx, ty = x + dx, y + dy
            if 0 <= tx < C and 0 <= ty < R and nl[ty][tx] == '.' and not vl[ty][tx]:
                vl[ty][tx] = True
                Q.append([tx, ty, dis + 1])

    result = max(dis, result)


D = [[0, 1], [0, -1], [-1, 0], [1, 0]]
T = int(input())
for t in range(T):
    result = 0
    C, R = map(int, input().split())
    nl = [input() for _ in range(R)]
    vl = [[False for _ in range(C)] for _ in range(R)]
    for i in range(C):
        for j in range(R):
            cnt = 0
            for dx, dy in D:
                tx, ty = i + dx, j + dy
                if 0 <= tx < C and 0 <= ty < R and not vl[j][i] and nl[j][i] == '.' and nl[ty][tx] == '.':
                    cnt += 1
            if cnt == 1 or cnt == 2:
                bfs(i, j)
    print('Maximum rope length is {}.'.format(result))