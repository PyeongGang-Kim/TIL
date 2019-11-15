T = int(input())
for t in range(1, T+1):
    al = []
    N = int(input())
    for _ in range(N):
        x, y, d, k = map(int, input().split())
        al.append([2*x, 2*y, d, k, 0])

    cl = []
    for i in range(len(al)-1):
        for j in range(i+1, len(al)):
            if al[i][0] == al[j][0]:
                if al[i][2] == 0 and al[j][2] == 1 and al[i][1] < al[j][1]:
                    cl.append([al[j][1] - al[i][1], i, j])
                elif al[i][2] == 1 and al[j][2] == 0 and al[i][1] > al[j][1]:
                    cl.append([al[i][1] - al[j][1], i, j])
            elif al[i][1] == al[j][1]:
                if al[i][2] == 2 and al[j][2] == 3 and al[i][0] > al[j][0]:
                    cl.append([al[i][0] - al[j][0], i, j])
                elif al[i][2] == 3 and al[j][2] == 2 and al[i][0] < al[j][0]:
                    cl.append([al[j][0] - al[i][0], i, j])
            else:
                tmp1 = al[j][0] - al[i][0]
                tmp2 = al[j][1] - al[i][1]
                if abs(tmp1) == abs(tmp2):
                    if tmp1 < 0:
                        if tmp2 < 0:
                            if (al[i][2] == 1 and al[j][2] == 3) or (al[i][2] == 2 and al[j][2] == 0):
                                cl.append([-tmp1*2, i, j])
                        else:
                            if (al[i][2] == 2 and al[j][2] == 1) or (al[i][2] == 0 and al[j][2] == 3):
                                cl.append([tmp2*2, i, j])
                    else:
                        if tmp2 < 0:
                            if (al[i][2] == 3 and al[j][2] == 0) or (al[i][2] == 1 and al[j][2] == 2):
                                cl.append([tmp1*2, i, j])
                        else:
                            if (al[i][2] == 3 and al[j][2] == 1) or (al[i][2] == 0 and al[j][2] == 2):
                                cl.append([tmp1*2, i, j])
    cl.sort()
    E = 0
    for crush in cl:
        if al[crush[1]][4]:
            if not al[crush[2]][4] and crush[0] == al[crush[1]][4]:
                al[crush[2]][4] = crush[0]
                E += al[crush[2]][3]
        else:
            if al[crush[2]][4]:
                if crush[0] == al[crush[2]][4]:
                    al[crush[1]][4] = crush[0]
                    E += al[crush[1]][3]
            else:
                E += al[crush[1]][3] + al[crush[2]][3]
                al[crush[1]][4] = crush[0]
                al[crush[2]][4] = crush[0]
    print('#{} {}'.format(t, E))