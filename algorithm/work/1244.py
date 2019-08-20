def cf(c=0):
    if c >= n:
        chklg(nl)
        return

    for i in range(len(nl)-1):
        for j in range(i+1, len(nl)):
            nl[j], nl[i] = nl[i], nl[j]
            tmp = 0
            for k in range(len(nl)):
                tmp += int(nl[k])*10**(len(nl)-k-1)
            if tmp not in vl[c]:
                vl[c].append(tmp)
                cf(c+1)
            nl[j], nl[i] = nl[i], nl[j]


def chklg(nll):
    global maxnum
    tmp2 = 0
    for i in range(len(nll)):
        tmp2 += int(nll[i])*10**(len(nll)-i-1)
    if tmp2 > maxnum:
        maxnum = tmp2


T = int(input())
vl = []
for t in range(1, T+1):
    numb, n = input().split()
    nl = list(numb)
    n = int(n)
    if len(vl)<n:
        for i in range(len(vl), n):
            vl.append([])
    maxnum = int(numb)
    cf()
    print('#{} {}'.format(t,maxnum))