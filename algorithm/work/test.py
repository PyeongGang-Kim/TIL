T = int(input())
for t in range(1, T+1):
    nl = [list(map(int, input().split())) for _ in range(9)]
    chk = 0
    while not chk:
        for j in range(9):
            tl = [0]*9
            for i in range(9):
                tmp = nl[j][i]
                if tl[tmp-1]:
                    chk = 1
                    break
                else:
                    tl[tmp-1] = 1
            if chk:
                break
        if chk:
            break
        for i in range(9):
            tl = [0]*9
            for j in range(9):
                tmp = nl[j][i]
                if tl[tmp-1]:
                    chk = 1
                    break
                else:
                    tl[tmp-1] = 1
            if chk:
                break
        if chk:
            break

        for k in range(3):
            for l in range(3):
                tl = [0]*9
                for j in range(3):
                    for i in range(3):
                        tmp = nl[j+3*k][i+3*l]
                        if tl[tmp-1]:
                            chk = 1
                            break
                        else:
                            tl[tmp-1] = 1
                if chk:
                    break
            if chk:
                break
        break
    print('#{} {}'.format(t, int(not chk)))