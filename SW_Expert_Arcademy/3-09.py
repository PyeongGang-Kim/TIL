T=int(input())
for t in range(1,T+1):
    N, M = map(int, input().split(" "))
    ai=list(map(int, input().split(" ")))
    result=0
    maxnum, minnum = sum(ai[0:M]), sum(ai[0:M])

    for n in range(N-M):
        tmp=0
        for m in range(1,M+1):
            tmp+=ai[n+m]
        if tmp>maxnum:
            maxnum=tmp
        if tmp<minnum :
            minnum=tmp
    result=maxnum-minnum
    print('#'+str(t), result)