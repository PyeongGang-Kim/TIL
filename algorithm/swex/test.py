drs = [[0, 0], [0, -1], [1, 0], [0, 1], [-1, 0]]
T = int(input())
for t in range(1, T+1):
    M, A = map(int, input().split())
    p1 = list(map(int, input().split()))
    p2 = list(map(int, input().split()))
    al = []
    for _ in range(A):
        al.append(list(map(int, input().split())))
    vl1 = [[] for _ in range(M)]
    vl2 = [[] for _ in range(M)]
    p1x, p1y = 1, 1
    p2x, p2y = 10, 10
    E = 0
    tmpmax1 = 0
    tmpmax2 = 0
    for j in range(A):
        if abs(p1x - al[j][0]) + abs(p1y - al[j][1]) <= al[j][2]:
            tmpmax1 = max(tmpmax1, al[j][3])
        if abs(p2x - al[j][0]) + abs(p2y - al[j][1]) <= al[j][2]:
            tmpmax2 = max(tmpmax2, al[j][3])
    E += tmpmax1 + tmpmax2

    for i in range(M):
        p1x, p1y = p1x + drs[p1[i]][0], p1y + drs[p1[i]][1]
        p2x, p2y = p2x + drs[p2[i]][0], p2y + drs[p2[i]][1]
        tmp1 = []
        tmp2 = []
        for j in range(A):
            if abs(p1x-al[j][0]) + abs(p1y-al[j][1]) <= al[j][2]:
                tmp1.append(j)
            if abs(p2x-al[j][0]) + abs(p2y-al[j][1]) <= al[j][2]:
                tmp2.append(j)
        if tmp1:
            if tmp2:
                #조합 만들면서 더하기
                tmpmax = 0
                for i1 in tmp1:
                    for i2 in tmp2:
                        if i1 != i2:
                            tmpmax = max(tmpmax, al[i2][3] + al[i1][3])
                        else:
                            tmpmax = max(tmpmax, al[i2][3])
                E += tmpmax
            else:
                #tmp1중 최대 골라 더하기
                tmpmax = 0
                for i1 in tmp1:
                    tmpmax = max(tmpmax, al[i1][3])
                E += tmpmax
        else:
            if tmp2:
                #tmp2중 최대 골라 더하기
                tmpmax = 0
                for i2 in tmp2:
                    tmpmax = max(tmpmax, al[i2][3])
                E += tmpmax

    print('#{} {}'.format(t, E))