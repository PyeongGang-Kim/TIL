T = int(input())
for t in range(1, T+1):
    N, M, K, A, B = map(int, input().split())
    al = list(map(int, input().split()))
    bl = list(map(int, input().split()))
    tl = list(map(int, input().split()))
    tlcnt = 0
    ocnt = 0
    tmpl = []
    tmplf = 0
    tmplr = 0
    al2 = [[] for _ in range(N)]
    bl2 = [0 for _ in range(M)]
    raa = range(N)
    rab = range(M)
    r = 0
    time = 0
    while ocnt < K:
        for i in raa:
            if al2[i] and al2[i][0] == time:
                tmpl.append(al2[i])
                tmplr += 1
                al2[i] = []
        for i in raa:
            try:
                if tl[tlcnt] <= time:
                    if not al2[i]:
                        tlcnt += 1
                        if i+1 == A:
                            al2[i] = [time + al[i], tlcnt, True]
                        else:
                            al2[i] = [time + al[i], tlcnt, False]
                else:
                    break
            except:
                break

        for i in rab:
            if bl2[i] == time:
                bl2[i] = 0
        for i in rab:
            if tmplf < tmplr:
                if not bl2[i]:
                    bl2[i] = time + bl[i]
                    ocnt += 1
                    if tmplf < tmplr and i+1 == B and tmpl[tmplf][2]:
                        r += tmpl[tmplf][1]
                    tmplf += 1

            else:
                break
        time += 1
    if not r:
        r = -1
    print('#{} {}'.format(t, r))