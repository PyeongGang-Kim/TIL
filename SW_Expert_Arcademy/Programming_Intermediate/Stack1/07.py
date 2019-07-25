T=int(input())
for t in range(1,T+1):
    a=input()

    chk=0
    st=[]
    for c in a:
        if c=='{' or c=='(':
            st.append(c)

        if c=='}':
            if len(st):
                if st[-1]=='{':
                    st.pop(-1)
                else:
                    chk=1
                    break
            else:
                chk=1
        if c == ')':
            if len(st):
                if st[-1]=='(':
                    st.pop(-1)
                else:
                    chk=1
                    break
            else:
                chk=1

    if chk==1 or len(st)>0:
        result=0
    else:
        result=1

    print('#{} {}'.format(t, result))
