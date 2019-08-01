T=int(input())
for t in range(1,T+1):
    N=int(input())

    a=[[[0,0] for i in range(10)] for i in range(10)]

    for n in range(N):
        tempList=list(map(int, input().strip().split(' ')))
        if tempList[4]==1:
            red1,red2=[tempList[0],tempList[1]], [tempList[2],tempList[3]]
            for i in range(red1[1], red2[1] + 1):
                for j in range(red1[0], red2[0] + 1):
                    a[i][j][0] = 1
        else:
            blue1,blue2=[tempList[0],tempList[1]], [tempList[2],tempList[3]]
            for i in range(blue1[1],blue2[1]+1):
                for j in range(blue1[0],blue2[0]+1):
                    a[i][j][1]=1
    cnt=0
    for i in range(10):
        for j in range(10):
            if a[i][j][0]+a[i][j][1]==2:
                cnt+=1
    print('#{} {}'.format(t,cnt))