# 승객 bfs로 찾기
# 가장 가까운 우선순위 높은 승객을 찾는다.
# bfs로 도착지로 이동한다. 이동거리 확인
# 남은연료 - 이동거리 0 보다 작으면 종료
# 아닐경우 남은연료 += 이동거리
from _collections import deque
D = [[0, -1], [1, 0], [0, 1], [-1, 0]]

def find_p(x, y):
    _, ex, ey = pl[y][x]
    if pl[y][x][0]:
        pl[y][x][0] = 0
        return x, y, 0
    vl = [[0 for _ in range(N)] for _ in range(N)]
    vl[y][x] = 1
    Q = deque([[x, y, 0]])
    temp_passengers = []
    while Q:
        qlen = len(Q)
        while qlen:
            qlen -= 1
            x, y, dis = Q.popleft()
            for dx, dy in D:
                tx, ty = x + dx, y + dy
                if 0 <= tx < N and 0 <= ty < N and not nl[ty][tx] and not vl[ty][tx]:
                    vl[ty][tx] = 1
                    if pl[ty][tx][0]:
                        temp_passengers.append([tx, ty, dis+1])
                    else:
                        Q.append([tx, ty, dis+1])
        # 승객이 있으면 우선순위에 따라 정렬해서 0번째 찾기
        if temp_passengers:
            temp_passengers.sort(key=lambda x: [x[1], x[0]])
            tx, ty, dis = temp_passengers[0]
            pl[ty][tx][0] = 0
            # 태울 승객까지의 거리, 위치 반환
            return temp_passengers[0]

    # 태울 승객까지의 거리, 태운 승객 반환
    return -1, -1, -1

def find_d(x, y):
    _, ex, ey = pl[y][x]
    if x == ex and y == ey:
        return 0
    vl = [[0 for _ in range(N)] for _ in range(N)]
    Q = deque([[x, y, 0]])
    while Q:
        x, y, dis = Q.popleft()
        for dx, dy in D:
            tx, ty = x + dx, y + dy
            if 0 <= tx < N and 0 <= ty < N and not nl[ty][tx] and not vl[ty][tx]:
                vl[ty][tx] = 1
                if tx == ex and ty == ey:
                    return dis+1
                Q.append([tx, ty, dis+1])
    return -1

N, M, F = map(int, input().split())
nl = [list(map(int, input().split())) for _ in range(N)]
ty, tx = map(int, input().split())
ty -= 1
tx -= 1
passengers = [[x-1 for x in map(int, input().split())] for _ in range(M)]
pl = [[[0, 0, 0] for _ in range(N)] for _ in range(N)]
passenger_count = len(passengers)
for passenger in passengers:
    pl[passenger[0]][passenger[1]] = [1, passenger[3], passenger[2]]


while passenger_count:
    ttx, tty, dis = find_p(tx, ty)
    if dis == -1 or F-dis < 0:
        break
    tx, ty = ttx, tty
    F -= dis

    dis = find_d(tx, ty)
    if dis == -1 or F-dis < 0:
        break
    F += dis
    _, tx, ty = pl[ty][tx]
    passenger_count -= 1

if passenger_count:
    print(-1)
else:
    print(F)
