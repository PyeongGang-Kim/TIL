T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nl = [list(map(int, input().split())) for _ in range(N)]
    result = -1
    for j in range(N-2):
        for i in range(1, N-1):
            for l in range(i-1, -1, -1):
                for r in range(i+1, N):
                    ey = j + r - l
                    if ey >= N:
                        break
                    ex = - i + r + l
                    ry = j + r - i
                    ly = j + i - l
                    if (r-i)*(i-l)*2 < result:
                        continue
                    # print(i, j, l, ly, r, ry, ex, ey)
                    tmp = set()
                    chk = False
                    for r1 in range(r-i):
                        if nl[j+r1][i+r1] not in tmp:
                            tmp.add(nl[j+r1][i+r1])
                        else:
                            chk = True
                            break
                        if nl[ey-r1][ex-r1] not in tmp:
                            tmp.add(nl[ey-r1][ex-r1])
                        else:
                            chk = True
                            break
                    for r2 in range(i-l):
                        if nl[ly-r2][l+r2] not in tmp:
                            tmp.add(nl[ly-r2][l+r2])
                        else:
                            chk = True
                            break
                        if nl[ry+r2][r-r2] not in tmp:
                            tmp.add(nl[ry+r2][r-r2])
                        else:
                            chk = True
                            break
                    if not chk:
                        result = max(result, len(tmp))
    print('#{} {}'.format(tc, result))