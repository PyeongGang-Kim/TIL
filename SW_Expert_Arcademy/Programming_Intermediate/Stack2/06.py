#미완


T=int(input())
rsp=[3,3,1,2]
for t in range(1,T+1):
    N=int(input())
    NL=list(map(int, input().strip().split(' ')))
    w1=0
    w2=0
    win=0
    st1=[NL[0]]
    st2=[NL[(N + 1) // 2]]
    for i in range(1,(N + 1) // 2):
        if NL[i]==NL[0]:
            st1.append(NL[i])
        else:
            if st1[0]==rsp[NL[i]]:
                w1=len(st1)+1
    for i in range((N + 1) // 2,N):
        if NL[i]==NL[0]:
            st2.append(NL[i])
        else:
            if st2[0]==rsp[NL[i]]:
                w1=len(st2)+1

    if NL[w1]==NL[w2] or NL[w1]!=rsp[NL[w2]]:
        win=w1
    else:
        win=w2

    print("#{} {}".format(t, win))


    # for
    #
    # if NL[:(N + 1) // 2] in 1:
    #     if NL[:(N + 1) // 2] in 2:
    #         # 1이 승리
    #         for i, n in enumerate(NL[:(N + 1) // 2]):
    #             if n == 1:
    #                 w1 = i + 1
    #     else:
    #         # 2가 승리
    #         for i, n in enumerate(NL[:(N + 1) // 2]):
    #             if n == 2:
    #                 w1 = i + 1
    # else:
    #     # 3이 승리
    #     for i, n in enumerate(NL[:(N + 1) // 2]):
    #         if n == 3:
    #             w1 = i + 1
    #
    # if NL[:(N + 1) // 2] in 1:
    #     if NL[:(N + 1) // 2] in 2:
    #         # 1이 승리
    #         for i, n in enumerate(NL[:(N + 1) // 2]):
    #             if n == 1:
    #                 w1 = i + 1
    #     else:
    #         # 2가 승리
    #         for i, n in enumerate(NL[:(N + 1) // 2]):
    #             if n == 2:
    #                 w1 = i + 1
    # else:
    #     # 3이 승리
    #     for i, n in enumerate(NL[:(N + 1) // 2]):
    #         if n == 3:
    #             w1 = i + 1


