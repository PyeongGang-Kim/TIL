T = int(input())
for tc in range(1, T+1):
    a, b = map(int, input().split())
    A, B = divmod(a, b)
    res = ''
    if B:
        vl = [0 for i in range(b)]
        vl2 = []
        tmp = -1
        while True:
            t1, t = divmod(10*B, b)
            if t == 0:
                break
            if not vl[B]:
                vl[B] = t
                vl2.append(str(t1))
                B = t

            else:
                tmp = vl2.index(str(t1))
                break
        if tmp != -1:
            r = ['.']
            for i in range(tmp):
                r.append(vl2[i])
            r1 = []
            for i in range(tmp, len(vl2)):
                r1.append(vl2[i])
            res = (str(A) +''.join(r) + '(' +''.join(r1)+')')
        else:
            res = (round(a/b, 1))
    else:
        res = str(A)
    print('#{} {}'.format(tc, res))