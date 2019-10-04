'''
부분적으로 높은점, 낮은점만 사이에 있는 갯수를 알면
그 한 봉우리에서 나오는 경우의 수를 알 수 있다.
'''

T = int(input())
for t in range(1, T+1):
    N = int(input())
    nl = list(map(int, input().split()))
    low = nl[0]
    chkd = True
    cnt = 0
    st = []
    for i in range(len(nl)-1):
        #올라가는 경우
        if chkd:
            if nl[i] < nl[i+1]:
                cnt += 1
            else:
                st.append(cnt)
                cnt = 0
                chkd = False

        #내려가는 경우
        else:
            if nl[i] > nl[i+1]:
                cnt += 1
            else:
                st.append(cnt)
                cnt = 0
                chkd = True
    #맨 마지막 하나가 남는다.