T=int(input())
for t in range(1,T+1):
    try:
        st = []
        tm=input().strip().split(' ')
        for r in tm:
            if r.isdigit():
                st.append(int(r))
            else:
                if r =='+':
                    tmp2=st.pop(-1)
                    tmp1=st.pop(-1)
                    st.append(int(tmp1+tmp2))
                elif r =='*':
                    tmp2=st.pop(-1)
                    tmp1=st.pop(-1)
                    st.append(int(tmp1*tmp2))
                elif r =='-':
                    tmp2=st.pop(-1)
                    tmp1=st.pop(-1)
                    st.append(int(tmp1-tmp2))
                elif r =='/':
                    tmp2=st.pop(-1)
                    tmp1=st.pop(-1)
                    st.append(int(round((tmp1/tmp2))))
                else:
                    result=st.pop()
        print('#{} {}'.format(t,result))
    except:
        print('#{} {}'.format(t,'error'))

