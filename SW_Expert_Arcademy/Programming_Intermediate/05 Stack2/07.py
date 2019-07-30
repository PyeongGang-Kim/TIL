def findstart(chk, ls):
    tmp=ls[0]
    tmpst=[0]
    for k in range(1, len(ls)):
        if not chk[k] and tmp>ls[k]:
            tmp=ls[k]
            tmpst.append(k)
    chk[tmpst.pop()]=1
    return chk, tmp

def findminsum(chk, tempst=[],i=0):
    tmp=sum(tempst)
    if i >= N:
        st.append(sum(tempst))
        return

    if minsum<tmp:
        return

    for x in range(N):
        if not chk[x]:
            chk[x] = 1
            tempst.append(nl[i][x])
            i += 1
            findminsum(chk, tempst, i)
            chk[x] = 0
            i -= 1
            tempst.pop()

T=int(input())
for t in range(1,T+1):
    N = int(input())
    nl = [list(map(int, input().strip().split())) for n in range(N)]
    chk=[0 for x in range(N)]
    st=[]
    minsum=0
    for i in range(N):
        chk, tmp = findstart(chk,nl[i])
        minsum+=tmp
    chk=[0 for x in range(N)]
    findminsum(chk)
    result=min(st)
    print('#{} {}'.format(t, result))