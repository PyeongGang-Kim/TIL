def move(x, y, tx, ty, c):
    global cnt
    for idx in nl[y][x][1]:
        dl[idx][0], dl[idx][1] = tx, ty
    if c == 1:
        nl[y][x][1].reverse()
    nl[ty][tx][1] = nl[ty][tx][1] + nl[y][x][1]
    cnt = max(cnt, len(nl[ty][tx][1]))
    nl[y][x][1] = []


D = [[1, 0], [-1, 0], [0, -1], [0, 1]]
DX = {0: 1, 1: 0, 2: 3, 3: 2}
N, K = map(int, input().split())
nl = [[[i, []] for i in map(int, input().split())] for _ in range(N)]
dl = []
for k in range(K):
    y, x, d = map(int, input().split())
    dl.append([x-1, y-1, d-1])
    nl[y-1][x-1][1].append(k)

tim = 0
cnt = 1
if len(dl) < 4:
    tim = 1001

while tim < 1001:
    tim += 1
    # 드론들 순번대로 이동한다
    for i in range(len(dl)):
        # 움직일 수 있는 드론
        if nl[dl[i][1]][dl[i][0]][1] and nl[dl[i][1]][dl[i][0]][1][0] == i:
            x, y, d = dl[i]
            tx, ty = x + D[d][0], y + D[d][1]
            if 0 <= tx < N and 0 <= ty < N:
                # 빨간색
                if nl[ty][tx][0] == 1:
                    move(x, y, tx, ty, 1)
                # 파란색
                elif nl[ty][tx][0] == 2:
                    dl[i][2] = DX[dl[i][2]]
                    tx, ty = x - D[d][0], y - D[d][1]
                    if 0 <= tx < N and 0 <= ty < N:
                        # 파란색 빨간색
                        if nl[ty][tx][0] == 1:
                            move(x, y, tx, ty, 1)
                        # 파란색 파란색
                        elif nl[ty][tx][0] == 2:
                            dl[i][2] = DX[dl[i][2]]
                        # 파란색 흰색
                        else:
                            move(x, y, tx, ty, 0)
                    # 파란색 파란색
                    else:
                        dl[i][2] = DX[dl[i][2]]
                # 흰색
                else:
                    move(x, y, tx, ty, 0)
            # 파란색
            else:
                dl[i][2] = DX[dl[i][2]]
                tx, ty = x - D[d][0], y - D[d][1]
                if 0 <= tx < N and 0 <= ty < N:
                    # 파란색 빨간색
                    if nl[ty][tx][0] == 1:
                        move(x, y, tx, ty, 1)
                    # 파란색 파란색
                    elif nl[ty][tx][0] == 2:
                        dl[i][2] = DX[dl[i][2]]
                    # 파란색 흰색
                    else:
                        move(x, y, tx, ty, 0)
                # 파란색 파란색
                else:
                    dl[i][2] = DX[dl[i][2]]
    # cnt 확인
    if cnt >= 4:
        break
if tim == 1001:
    print(-1)
else:
    print(tim)

