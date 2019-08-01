def subsetlist(N,K,*v):
    b=[[0],[1]]
    for k in range(len(v)-1):
        temp=[]
        for i, c in enumerate(b):
            temp.append(c+[0])
            temp.append(c+[1])
        b=temp
    for i in range(len(b)):
        for j in range(len(b[0])):
            b[i][j]*=v[j]
    chk=0
    for i in b:
        if i.count(0)==12-N:
            sum=0
            for k in i:
                sum+=k
            if sum==K:
                chk+=1
    return chk


T=int(input())
inputtuple=tuple(range(1,13))
for t in range(1,T+1):
    N, K = map(int, input().strip().split(' '))
    print('#{} {}'.format(t,subsetlist(N,K,*inputtuple)))
