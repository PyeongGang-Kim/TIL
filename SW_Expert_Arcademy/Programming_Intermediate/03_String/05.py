T=int(input())
for t in range(1,T+1):
    a=''.join(list(set(input().strip())))
    b=input().strip()
    maxnum=0
    for aa in a:
        temp=b.count(aa)
        if maxnum<temp:
            maxnum=temp
    print('#{} {}'.format(t,maxnum))