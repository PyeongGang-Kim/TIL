import sys
sys.stdin=open('input.txt', 'r')

T=int(input())
for t in range(1,T+1):
    
    #문제입력 양쪽에서 공백이 있는 경우가 있기 때문에 strip()을 추가하였음.
    N, M = map(int, input().strip().split(" "))
    ai=list(map(int, input().strip().split(" ")))

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