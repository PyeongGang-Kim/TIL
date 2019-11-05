def dfs(x, y, d):

    for dx, dy, td in D[d]:
        tx, ty = x + dx, y + dy
        if 0 <= tx < C and 0 <= ty < R and nl[ty][tx] == '.' and not vl[ty][tx][td]:
            if i == tx and j == ty:
                return True
            vl[ty][tx][td] = True
            tmp = dfs(tx, ty, td)
            vl[ty][tx][td] = False
            if tmp:
                return True
    return False


dr = [[1, 0, 0], [0, 1, 1], [-1, 0, 2], [0, -1, 3]]
D = {
    0: [dr[3], dr[0], dr[1]],
    1: [dr[0], dr[1], dr[2]],
    2: [dr[1], dr[2], dr[3]],
    3: [dr[2], dr[3], dr[0]],
}


R, C = map(int, input().split())
nl = [input().strip() for _ in range(R)]

chk = False
vl = [[[False for _ in range(4)] for _ in range(C)] for _ in range(R)]
for j in range(R):
    for i in range(C):
        if nl[j][i] == '.':
            for k in range(4):
                if not dfs(i, j, k):
                    chk = True
                    break
            if chk:
                break
    if chk:
        break
if chk:
    print(1)
else:
    print(0)