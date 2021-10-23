from collections import  deque

# x, y 좌표에서 color에 해당하는 그룹의 크기, 기준블록 좌표를 반환하는 함수 만약 그룹이 아닌경우 빈리스트
# 해당 색깔에서 그룹을 bfs로 탐색하면서 방문을 해 두면 다른 위치에서 중복방문을 막을 수 있다.
# 다른 색깔을 탐색하기 시작할 땐 방문배열 초기화하기.
def find_group(x, y, color):
    Q = deque([[x, y]])
    vl[y][x] = 1
    cnt = 0
    r_cnt = 0
    while Q:
        cx, cy = Q.pop()
        cnt += 1
        for dx, dy in D:
            tx, ty = cx + dx, cy + dy
            # 격자 안이고 방문한적 없고 무지개 혹은 같은색깔
            if 0 <= tx < N and 0 <= ty < N and not vl[ty][tx]:
                if nl[ty][tx] == color:
                    vl[ty][tx] = 1
                    Q.append([tx, ty])
                elif not nl[ty][tx]:
                    vl[ty][tx] = 1
                    Q.append([tx, ty])
                    r_cnt += 1
    return cnt, r_cnt

# 중력을 작용하는 함수
def gravity():
    for i in range(N):
        chk = 1
        sy = N-1
        # 처음 빈칸을 찾아야 한다.
        for j in range(sy, -1, -1):
            if nl[j][i] == -2:
                sy = j
                chk = 0
                break
        if chk:
            continue
        while sy:
            # sy가 맨 위가 아니면 교체할 칸을 찾아야 한다.
            for cy in range(sy-1, -1, -1):
                # 만약 차례로 올라가다 -1을 만났으면 현재칸보다 위에있는 빈칸을 찾는다.
                chk = 0
                if nl[cy][i] == -1:
                    for j in range(cy, -1, -1):
                        if nl[j][i] == -2:
                            sy = j
                            chk = 1
                            break
                    if not chk:
                        chk = 1
                        sy = 0
                if chk:
                    break

                if nl[cy][i] > -1:
                    nl[sy][i] = nl[cy][i]
                    nl[cy][i] = -2
                    sy -= 1
                    break
                if not cy:
                    sy = 0

def init_visit_list():
    for i in range(N):
        for j in range(N):
            vl[j][i] = 0



# 90도 회전 작용하는 함수
def rotate():
    global nl
    # 0, 0 -> 0, N-1
    # 1, 2 -> 2, N-1-1
    # x, y -> y, N-1-x
    tl = [[0 for _ in range(N)] for _ in range(N)]
    for j in range(N):
        for i in range(N):
            tl[N-1-i][j] = nl[j][i]
    nl = tl
    pass

# 그룹 삭제하는 함수
def del_group(x, y):
    global score
    color = nl[y][x]
    Q = deque([[x, y]])
    vl[y][x] = 1
    nl[y][x] = -2
    cnt = 0
    while Q:
        cx, cy = Q.pop()
        cnt += 1
        for dx, dy in D:
            tx, ty = cx + dx, cy + dy
            # 격자 안이고 방문한적 없고 무지개 혹은 같은색깔
            if 0 <= tx < N and 0 <= ty < N and not vl[ty][tx] and (nl[ty][tx] == color or not nl[ty][tx]):
                vl[ty][tx] = 1
                nl[ty][tx] = -2
                Q.append([tx, ty])
    score += cnt * cnt

D = [[-1, 0], [1, 0], [0, 1], [0, -1]]
N, M = map(int, input().split())

nl = [list(map(int, input().split())) for _ in range(N)]

vl = [[0 for _ in range(N)] for _ in range(N)]


# 블록 그룹이 있는동안 반복
chk = 1
score = 0
while chk:
    gx, gy = N, N
    max_size = 0
    max_rainbow_cnt = 0

    # 각 색상별로 블록 그룹 탐색하기
    for color in range(1, M+1):
        init_visit_list()
        for j in range(N):
            for i in range(N):
                # 현재 찾는 색인 경우 그룹 탐색 시작.
                if nl[j][i] == color:
                    size, rainbow_cnt = find_group(i, j, color)
                    if size > 1:
                        # 최대갯수가 갱신되는 경우 초기화
                        if max_size < size:
                            max_size, max_rainbow_cnt, gx, gy = size, rainbow_cnt, i, j
                        # 최대갯수와 동일한 경우
                        elif max_size == size:
                            # 무지개 블록 갯수가 더 많은 경우
                            if rainbow_cnt > max_rainbow_cnt:
                                max_rainbow_cnt, gx, gy = rainbow_cnt, i, j
                            elif rainbow_cnt == max_rainbow_cnt:
                                # 행 번호가 더 큰 경우
                                if j > gy:
                                    gx, gy = i, j
                                elif j == gy:
                                    if i > gx:
                                        gx = i


    # 그룹 있는지 확인 후 그룹 없으면 종료해야함.
    if not max_size:
        break
    init_visit_list()
    del_group(gx, gy)
    gravity()
    rotate()
    gravity()


print(score)
#중력
#90도 회전
#그룹 탐색
