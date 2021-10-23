import sys
sys.setrecursionlimit(100000)
D = [[0, 1], [0, -1], [1, 0], [-1, 0]]

# 사각형 크기가 정해지면 그 사각형을 돌려야한다.

def turn(xs, xe, ys, ye):
    if xs >= xe:
        return

    for j in range(ys, ye + 1):
        for i in range(xs, xe+1):
            tl[ys + i - xs][xe + ys - j] = nl[j][i]
    for j in range(ys, ye + 1):
        for i in range(xs, xe+1):
            nl[j][i] = tl[j][i]

def div(inp, val, xs, xe, ys, ye):
    if val == inp:
        turn(xs, xe, ys, ye)
        return
    # 다른 경우면 네개로 쪼갠다.
    xm = (xs + xe) >> 1
    ym = (ys + ye) >> 1
    div(inp, val-1, xs, xm, ys, ym)
    div(inp, val-1, xm+1, xe, ys, ym)
    div(inp, val-1, xs, xm, ym+1, ye)
    div(inp, val-1, xm+1, xe, ym+1, ye)

def melt():
    chk_points = []
    for j in range(1<<N):
        for i in range(1<<N):
            if nl[j][i]:
                cnt = 0
                for dx, dy in D:
                    tx, ty = i + dx, j + dy
                    if 0 <= tx < 1<<N and 0 <= ty < 1<<N:
                        if nl[ty][tx]:
                            cnt += 1
                if cnt < 3:
                    chk_points.append([i, j])
    for chk_point in chk_points:
        nl[chk_point[1]][chk_point[0]] -= 1

def dfs(i, j, dep = 1):
    global cnt

    cnt += nl[j][i]
    res = 0
    for dx, dy in D:
        tx, ty = i + dx, j + dy
        if 0 <= tx < 1 << N and 0 <= ty < 1 << N and not vl[ty][tx] and nl[ty][tx]:
            vl[ty][tx] = 1

            res += dfs(tx, ty, dep + 1)
    return res + 1

N, Q = map(int, input().split())
nl = [list(map(int, input().split())) for _ in range(1<<N)]
tl = [[0 for _ in range(1<<N)] for _ in range(1<<N)]
ml = list(map(int, input().split()))
for size in ml:
    div(size, N, 0, (1<<N) - 1 , 0, (1<<N) - 1)
    melt()

cnt = 0
max_v = 0
vl = [[0 for _ in range(1<<N)] for _ in range(1<<N)]
for j in range(1<<N):
    for i in range(1<<N):
        if not vl[j][i] and nl[j][i]:
            vl[j][i] = 1
            max_v = max(dfs(i, j), max_v)


print(cnt)
print(max_v)