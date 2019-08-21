'''
1
10 10
1 2
3 1
3 2
2 4
5 6
6 9
8 9
6 7
8 7
8 10

'''



def dfs():
    global leng
    tmp = st[-1]
    for num in nl:
        if tmp == num[0] and num[1] not in st:
            st.append(num[1])
            if leng < len(st):
                leng = len(st)
            dfs()
            st.pop()
        if tmp == num[1] and num[0] not in st:
            st.append(num[0])
            if leng < len(st):
                leng = len(st)
            dfs()
            st.pop()



T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    nl = []
    for m in range(M):
        nl.append(list(map(int, input().split())))
    leng = 1
    for i in range(1,N+1):
        st = [i]
        dfs()
    print('#{} {}'.format(t, leng))