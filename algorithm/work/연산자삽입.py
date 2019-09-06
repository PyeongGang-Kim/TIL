import sys
sys.stdin = open('asdf.txt')


def fnd(i, j, d):
    while 1:
        vl[j][i] = 1
        for k in range(3):
            tx, ty = i + dr[(d+k)%4][0], j + dr[(d+k)%4][1]
            if 0 <= tx < M and 0 <= ty < N and not nl[ty][tx] and not vl[ty][tx]:
                d = (d+k)%4
                i = tx
                j = ty
                continue

        tx = i - dr[d][0]
        ty = j - dr[d][1]
        if 





dr = [[0, -1], [1, 0],[0, 1], [-1, 0]]
vl = [[0 for _ in range(M)] for _ in range(N)]