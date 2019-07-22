T=int(input())
for t in range(1,T+1):
    N=int(input())
    ai=list(map(int, input().strip().split()))

    sw=1
    for i in range(10):
        if sw:
            sw=0
            tmp=[ai[i],i]
            for j in range(i,len(ai)):
                if tmp[0]<ai[j]:
                    tmp=[ai[j],j]

            ai.pop(tmp[1])
            ai.insert(i,tmp[0])
        else:
            sw=1
            tmp=[ai[i],i]
            for j in range(i,len(ai)):
                if tmp[0]>ai[j]:
                    tmp=[ai[j],j]

            ai.pop(tmp[1])
            ai.insert(i,tmp[0])


    print('#{} {}'.format(t, ' '.join(map(str, ai[:10]))))