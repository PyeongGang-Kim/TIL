

n = int(input())
if n == 1:
    print(1)
else:
    st = [0, 2]
    i = 1
    cnum = 2
    while 1:
        st.append(st[-1] + i)
        if st[-1] >= n:
            print(cnum)
            break
        if cnum == st[i]:
            i += 1
        cnum += 1
