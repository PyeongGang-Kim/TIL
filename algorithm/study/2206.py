'''
bfs 중단할 시점을 잘 골라야 한다.
비짓 리스트를 벽돌을 부술수 있을 때와 벽돌을 부수지 못할 때로 나눠야 한다.
'''

from collections import deque
def bfs():
    d = [[0, 1], [0, -1], [-1, 0], [1, 0]]
    Q = deque([[0, 0, 1, 1]])
    chk = False
    vl = [[[False, False] for _ in range(M)] for _ in range(N)]
    while Q:
        x, y, dis, o = Q.popleft()
        vl[y][x][o] = True
        for dx, dy in d:
            tx, ty = x + dx, y + dy
            if tx == M-1 and ty == N-1:
                dis += 1
                chk = True
                return dis
            if 0 <= tx < M and 0 <= ty < N and not vl[ty][tx][o]:
                if nl[ty][tx] == '1' and o:
                    Q.append([tx, ty, dis+1, 0])
                    vl[ty][tx][0] = True
                elif nl[ty][tx] == '0':
                    Q.append([tx, ty, dis+1, o])
                    vl[ty][tx][o] = True
    return False


N, M = map(int, input().split())

nl = [input() for _ in range(N)]
if N == 1 and M == 1:
    print(1)
else:
    dis = bfs()
    if dis:

        print(dis)
    else:

        print(-1)