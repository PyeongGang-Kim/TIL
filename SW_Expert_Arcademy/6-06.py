def combi(n, k):
    result = 1
    k = min(n-k, k)

    for i in range(1, k+1):
        result*=(n+1-i)/i
    return result

T=int(input())
for t in range(1,T+1):
    num=int(int(input())/10)
    sum=0
    for i in range(int(num/2)+1):
        #float계산을 했으므로 라운드를 해서
        #소수점 아래자리를 버리는 게 아니게 만들어준다.
        #1.99999999를 2로 계산하고싶지만 int에 넣어버리면
        #1을 반환하기 때문.
        sum+=int(round(combi(num-i,i)*2**i))
    print('#{} {}'.format(t,sum))