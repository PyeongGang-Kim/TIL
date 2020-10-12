# 보드 위의 각 좌표에 말들을 기록할 수 있게 한다.
# 각 각의 말들은 좌표를 기록해둔다.
# 말이 이동하게 되면 내 위의 말들을 모두 옮긴다.
# 턴이 1000 초과 시 -1 출력한다.

# 말 이동할 때 4개 이상 쌓이면 게임 종료
D = [[0, -1], [1, 0], [0, 1], [-1, 0]]
CD = [1, 3, 0, 2]
N, K = map(int, input().split())
nl = [list(map(int, input().split())) for _ in range(N)]
sl = [[[] for _ in range(N)] for _ in range(N)]
stone_list = [list(map(int, input().split())) for _ in range(K)]
for idx, stone in enumerate(stone_list):
    stone[0] -= 1
    stone[1] -= 1
    stone[2] -= 1
    stone[2] = CD[stone[2]]
    stone[0], stone[1] = stone[1], stone[0]
    sl[stone[1]][stone[0]].append(idx)

def move_white(cx, cy, nx, ny, idx):
    # 갈 곳의 위치가 흰색 -> 예정대로 이동
    for i in range(idx, len(sl[cy][cx])):
        sl[ny][nx].append(sl[cy][cx][i])
        stone_list[sl[cy][cx][i]][0] = nx
        stone_list[sl[cy][cx][i]][1] = ny
    sl[cy][cx] = sl[cy][cx][:idx]
    if len(sl[ny][nx]) > 3:
        return True
    return False

def move_red(cx, cy, nx, ny, idx):
    global stone_list
    # 갈 곳의 위치가 빨간색 -> 이동하되 순서가 뒤집혀서 쌓임
    for i in range(len(sl[cy][cx])-1, idx-1, -1):
        sl[ny][nx].append(sl[cy][cx][i])
        stone_list[sl[cy][cx][i]][0] = nx
        stone_list[sl[cy][cx][i]][1] = ny
    sl[cy][cx] = sl[cy][cx][:idx]
    if len(sl[ny][nx]) > 3:
        return True
    return False

def game():
    # 매 턴마다 각 말별로 실시한다.
    turn = 1
    while turn < 1001:
        for i in range(K):
            # 현재 위치에서 몇번째 인덱스인지 확인
            cx, cy, dir = stone_list[i]
            for idx, num in enumerate(sl[cy][cx]):
                if num == i:
                    ci = idx
                    break
            # 현재 돌이 존재하는 위치 ci
            # 이동시켜 본다
            tx, ty = cx + D[dir][0], cy + D[dir][1]
            # 벗어났거나 파란색인경우
            if not (0 <= tx < N and 0 <= ty < N) or nl[ty][tx] == 2:
                # 방향전환
                dir = (dir + 2) % 4
                stone_list[i][2] = dir
                tx, ty = cx + D[dir][0], cy + D[dir][1]
                if 0 <= tx < N and 0 <= ty < N:
                    # 흰색 바닥인경우
                    if nl[ty][tx] == 0:
                        if move_white(cx, cy, tx, ty, ci):
                            return turn
                    # 빨간색 바닥인경우
                    elif nl[ty][tx] == 1:
                        if move_red(cx, cy, tx, ty, ci):
                            return turn
            # 흰색
            elif nl[ty][tx] == 0:
                if move_white(cx, cy, tx, ty, ci):
                    return turn
            # 빨간색
            else:
                if move_red(cx, cy, tx, ty, ci):
                    return turn

        turn += 1
    return -1
print(game())