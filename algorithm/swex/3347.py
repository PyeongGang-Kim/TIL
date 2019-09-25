for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    al = list(map(int, input().split()))
    bl = list(map(int, input().split()))
    st = [[al[0], 0, 0]]
    for i in range(1, len(al)):
        if al[i] < st[-1][0]:
            st.append([al[i], i, 0])
            if st[-1][0] == 1:
                break
    for n in bl:
        for a in st:
            if a[0] <= n:
                a[2] += 1
                break
    idx = 0
    tmp = 0
    for i in st:
        if i[2] > tmp:
            tmp = i[2]
            idx = i[1]
    print('#{} {}'.format(t, idx+1))
