def cf(c=0):
    if c >= n:
        chklg(nl)
        return

    for i in range(len(nl)-1):
        for j in range(i+1, len(nl)):
            nl[j], nl[i] = nl[i], nl[j]
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
for t in range(1, T+1):
    numb, n = input().split()
    nl = list(numb)
    n = int(n)
    maxnum = int(numb)
    cf()
    print('#{} {}'.format(t,maxnum))