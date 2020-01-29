def cleaning(x, y, d):
    cnt = 1
    nl[y][x] = 2
    while 1:
        cd = (d - 1) % 4
        chk = False
        for _ in range(4):
            tx, ty = x + D[cd][0], y + D[cd][1]
            if 0 <= tx < M and 0 <= ty < N and not nl[ty][tx]:
                chk = True
                x, y, d = tx, ty, cd
                nl[y][x] = 2
                cnt += 1
                break
            cd = (cd - 1) % 4
        if not chk:
            cd = (d + 2) % 4
            tx, ty = x + D[cd][0], y + D[cd][1]
            if 0 <= tx < M and 0 <= ty < N and nl[ty][tx] != 1:
                x, y = tx, ty
                continue
            return cnt


D = [[0, -1], [1, 0], [0, 1], [-1, 0]]
N, M = map(int, input().split())
r, c, d = map(int, input().split())
nl = [list(map(int, input().split())) for _ in range(N)]
print(cleaning(c, r, d))