import sys

'''
맨 끝 점에서 그 이전 점들의 세로 차 가로 차

맨 끝 좌표 x1, y1
그 위의 임의의 점 x. y
새로운 좌표는 x1 + (y1 - y), y1 - (x1 - x) 이다.
끝 점을 알면 된다.

'''
dr = [[1, 0], [0, -1], [-1, 0], [0, 1]]
dr2 = [[1, 0], [1, 1], [0, 1]]
rset = set()
N = int(sys.stdin.readline())
for n in range(N):
    xs, ys, d, g = map(int, sys.stdin.readline().split())
    xl, yl = xs+dr[d][0], ys+dr[d][1]
    nl = {(xs, ys), (xs+dr[d][0], ys+dr[d][1])}
    for i in range(g):
        tmpset = set()
        for x, y in nl:
            t1, t2 = xl + (yl - y), yl - (xl - x)
            if 0 <= t1 <= 100 and 0 <= t2 <= 100:
                tmpset.add((t1, t2))
        nl = nl.union(tmpset)
        xl, yl = xl + (yl - ys), yl - (xl - xs)

    rset = rset.union(nl)

cnt = 0
for x, y in rset:
    chk = True
    for dx, dy in dr2:
        tx, ty = x + dx, y + dy
        if (tx, ty) not in rset:
            chk = False
            break
    if chk:
        cnt += 1
print(cnt)