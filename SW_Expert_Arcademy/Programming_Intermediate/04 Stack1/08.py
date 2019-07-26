def fin(S, chk=0):
    if chk:
        return S, chk
    for i in listE:
        if S == i[0]:
            #갈 곳이 방문한 곳일 경우
            if listV[i[1]-1][1]:
                continue
            #갈 곳이 방문한 곳이 아닐 경우
            else:
                #만약 갈 곳이 도착점인 경우
                if G==i[1]:
                    return S, 1
                #갈 곳이 도착점이 아닌 경우
                else:
                    #스택에 갈 곳 추가
                    st.append(i[1])
                    #시작점을 갈 곳으로 변경
                    S=i[1]
                    #방문리스트에 기록
                    listV[S-1][1]=1
                    #갈 곳을 입력해서 함수 다시 호출
                    trash, chk=fin(S)
                    break

    #종점 못 가고 스택길이가 0이 아닌 경우
    if chk ==0 and len(st)!=0:
        #스택에서 하나 빼낸다
        st.pop(-1)
        #하나 빼낸 후 스택 길이가 0이면 함수 끝낸다.
        if len(st)==0:
            return S, chk
        #스택길이가 0이 아닐 경우 시작점을 스택 맨 끝에 값으로 설정한 후 함수 호출한다.
        else:
            S=st[-1]
        trash, chk=fin(S)

    #종점을 갔거나 스택길이가 0인 경우 함수를 끝낸다.
    else:
        return S, chk
    return S, chk

T=int(input())

for t in range(1,T+1):
    #V개의 노드 E개의 간선
    V, E = map(int, input().strip().split(' '))
    listV=[[i,0] for i in range(1,V+1)]

    listE=[list(map(int, input().strip().split(' '))) for e in range(E)]
    S, G= map(int, input().strip().split(' '))
    st=[S]
    listV[S-1][1]=0
    trash, chk =fin(S)
    print('#{} {}'.format(t,chk))