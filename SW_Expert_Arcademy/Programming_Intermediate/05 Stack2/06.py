def dv(b, c):
    tmp=(b+c)//2
    w1=b
    w2=tmp+1
    if tmp-b>1:
        w1=dv(b, tmp)
    else:
        if b!=tmp:
            if not(NL[b-1]==NL[tmp-1] or NL[b-1]!=rsp[NL[tmp-1]]):
                w1=tmp
    if c-tmp>2:
        w2=dv(tmp+1, c)
    else:
        if (tmp+1)!=c:
            if not(NL[tmp]==NL[c-1] or NL[tmp]!=rsp[NL[c-1]]):
                w2=c


    if NL[w1-1]==NL[w2-1] or NL[w1-1]!=rsp[NL[w2-1]]:
        return w1
    else:
        return w2

T=int(input())
rsp=[0,3,1,2]
for t in range(1,T+1):
    N=int(input())
    NL=list(map(int, input().strip().split(' ')))
    win=dv(1,N)

    print("#{} {}".format(t, win))