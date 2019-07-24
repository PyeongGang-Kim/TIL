def fin(p, chk=0):
    if chk:
        return 1
    chk=0
    cnt=0
    if not chk:
        for e in listE:
            if e[0]==st[-1] and listV[e[0]-1][1]!=G:
                if G==e[1]:
                    chk=1
                    break
                cnt+=1
                st.append(e[1])
                chk = fin(listV[e[0]-1][1])
                if chk:
                    break
    if cnt !=0:
        chk=fin(listV[st.pop(-1)-1])
    if chk:
        return 1
    else:
        return 0
T=int(input())


for t in range(1,T+1):
    #V개의 노드 E개의 간선
    V, E = map(int, input().strip().split(' '))
    listV=[[i,0] for i in range(1,V+1)]

    listE=[list(map(int, input().strip().split(' '))) for e in range(E)]
    S, G= map(int, input().strip().split(' '))


    ##set
    st=[S]
    listV[S-1][1]=1
    chk=0
    ##start
    result=fin(S)

    print('#{} {}'.format(t, result))