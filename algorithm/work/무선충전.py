
def mkcm(x, y, D, C, j, d=0):
    Q = [[x, y, D, C, j, d]]
    vl[y][x].append(j)
    while Q:
        x, y, D, C, j, d = Q.pop(0)
        for i in range(1, 5):
            tx, ty = x + dr[i][0], y + dr[i][1]
            if d < D and 1 <= tx <= 10 and 1 <= ty <= 10 and j not in vl[ty][tx]:
                vl[ty][tx].append(j)
                Q.append([tx, ty, D, C, j, d+1])


def selC(ap, bp):
    global CS
    re = []
    tmp2 = 0
    if vl[ap[1]][ap[0]]:
        if vl[bp[1]][bp[0]]:
            for a in vl[ap[1]][ap[0]]:
                for b in vl[bp[1]][bp[0]]:
                    tmp = {a, b}
                    tmp2 = 0
                    for t in tmp:
                        tmp2 += cl[t][3]
                    re.append(tmp2)
            CS += max(re)
        else:
            for t in vl[ap[1]][ap[0]]:
                re.append(cl[t][3])
            CS += max(re)
    elif vl[bp[1]][bp[0]]:
        for t in vl[bp[1]][bp[0]]:
            re.append(cl[t][3])
        CS += max(re)


dr = [[0, 0], [0, -1], [1, 0], [0, 1], [-1, 0]]
T = int(input())
for t in range(1, T+1):
    M, A = map(int, input().split())
    pd = []
    vl = [[[] for _ in range(11)] for _ in range(11)]
    for _ in range(2):
        pd.append(list(map(int, input().split())))
    ap = [1, 1]
    bp = [10, 10]
    cl = []
    CS = 0
    for a in range(A):
        cl.append(list(map(int, input().split())))
    for i, clt in enumerate(cl):
        mkcm(*clt, i)

    selC(ap, bp)
    for i in range(M):
        ap = [ap[0] + dr[pd[0][i]][0], ap[1] + dr[pd[0][i]][1]]
        bp = [bp[0] + dr[pd[1][i]][0], bp[1] + dr[pd[1][i]][1]]
        selC(ap, bp)

    print('#{} {}'.format(t, CS))