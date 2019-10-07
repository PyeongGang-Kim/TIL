'''
부분적으로 높은점, 낮은점만 사이에 있는 갯수를 알면
그 한 봉우리에서 나오는 경우의 수를 알 수 있다.
'''

T = int(input())
for t in range(1, T+1):
    N = int(input())
    nl = list(map(int, input().split()))
    idx = 0
    for i in range(len(nl)-1):
        if nl[i] < nl[i+1]:
            idx = i
            break
    r = 0
    if not idx and nl[0] > nl[1]:
        #안한다
        pass
    else:
        #한다
        st = [idx]
        d = True
        for i in range(len(nl)-1):
            if d:
                if nl[i] > nl[i+1]:
                    st.append(i)
                    d = False
            elif nl[i] < nl[i+1]:
                st.append(i)
                d = False
        if nl[-1] < nl[-2]:
            st.append(len(nl)-1)
        for i in range(0, len(st)-1, 2):
            r += (st[i+1]-st[i])*(st[i+2]-st[i+1])
    print('#{} {}'.format(t, r))