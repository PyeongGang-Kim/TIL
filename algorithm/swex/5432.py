T = int(input())
for t in range(1, T+1):
    S = input()
    st = []
    chk = False
    cnt = 0
    for i in range(len(S)):
        if S[i] == '(':
            st.append(i)
            cnt += 1
            chk = False
        elif S[i] == ')':
            if chk:
                st.pop()
            else:
                chk = True
                cnt -= 1
                st.pop()
                cnt += len(st)
    print('#{} {}'.format(t, cnt))