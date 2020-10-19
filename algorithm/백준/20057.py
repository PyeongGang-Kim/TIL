temp_D = [[1, 1, 0.01], [-1, 1, 0.01], [-2, 0, 0.02], [-1, 0, 0.07], [1, 0, 0.07], [2, 0, 0.02], [-1, -1, 0.1], [1, -1, 0.1], [0, -2, 0.05]]
D = []
for i in range(3):
    D.append([x[:] for x in temp_D])
    for point in temp_D:
        point[1] *= -1
        point[0], point[1] = point[1], point[0]
D.append([x[:] for x in temp_D])
dir = [[0, -1], [1, 0], [0, 1], [-1, 0]]
N = int(input())
mid = N >> 1
nl = [list(map(int, input().split())) for _ in range(N)]

ml = [[5 for _ in range(N)] for _ in range(N)]
ml[0][0] = 3
cx, cy = 0, 0
cdir = 1
cdir2 = 3
while 1:
    tx, ty = cx + dir[cdir][0], cy + dir[cdir][1]
    if 0 <= tx < N and 0 <= ty < N and ml[ty][tx] == 5:
        ml[ty][tx] = cdir2
    else:
        cdir = (cdir + 1) % 4
        cdir2 = (cdir2 + 1) % 4
        tx, ty = cx + dir[cdir][0], cy + dir[cdir][1]
        if 0 <= tx < N and 0 <= ty < N and ml[ty][tx] == 5:
            ml[ty][tx] = cdir2
        else:
            break
    cx, cy = tx, ty
cx, cy = mid, mid
cdir = 3
result = 0
while cx or cy:
    px, py = cx, cy
    cx, cy = cx + dir[cdir][0], cy + dir[cdir][1]
    # 모래를 뿌릴 위치 cx, cy 모래뿌릴 방향 cdir 뿌릴 모래양
    temp_sum = 0
    for wind in D[cdir]:
        # 모래를 뿌릴 위치(cx, cy)에서 각 각의 위치로 모래를 이동시킬 것.
        dx, dy, a = wind
        temp = int(nl[cy][cx] * a)
        tx, ty = cx + dx, cy + dy
        if 0 <= tx < N and 0 <= ty < N:
            nl[ty][tx] += temp
            temp_sum += temp
        else:
            temp_sum += temp
            result += temp
    # 남은 모래는 nl[cy][cx] - temp_sum이다.

    tx, ty = cx + dir[cdir][0], cy + dir[cdir][1]
    if 0 <= tx < N and 0 <= ty < N:
        nl[ty][tx] += nl[cy][cx] - temp_sum
    else:
        result += nl[cy][cx] - temp_sum
    nl[cy][cx] = 0
    cdir = ml[cy][cx]



print(result)

