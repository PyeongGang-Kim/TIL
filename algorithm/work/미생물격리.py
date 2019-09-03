import sys
sys.stdin = open('asdf.txt')


d = [[0, 0], [0, -1], [0, 1], [-1, 0], [1, 0]]
T = int(input())
for t in range(1, T+1):
    N, M, K = map(int, input().split())
    nl = [list(map(int, input().split())) for _ in range(K)]
    for m in range(M):
        st = []
        tl = []
        tmp2 = []
        for i, n in enumerate(nl):
            n[1] += d[n[3]][0]
            n[0] += d[n[3]][1]
            if n[1] == 0 or n[1] == N-1 or n[0] == 0 or n[0] == N-1:
                n[2] //= 2
                if n[2] == 0:
                    tmp2.append(i)
                if n[3] == 1 or n[3] == 3:
                    n[3] += 1
                else:
                    n[3] -= 1

            tmp = [n[1], n[0]]
            if tmp in st:
                if tmp not in tl:
                    tl.append(tmp)
            else:
                st.append(tmp)

        while tmp2:
            ti = tmp2.pop()
            nl[ti], nl[-1] = nl[-1], nl[ti]
            nl.pop()

        while tl:
            tx, ty = tl.pop()
            sm, m, dr = 0, 0, 0
            for i in range(len(nl)-1, -1, -1):
                if nl[i][1] == tx and nl[i][0] == ty:
                    sm += nl[i][2]
                    if nl[i][2] > m:
                        m = nl[i][2]
                        dr = nl[i][3]
                    nl[i], nl[-1] = nl[-1], nl[i]
                    nl.pop()
            nl.append([ty, tx, sm, dr])
    r = 0
    for n in nl:
        r += n[2]
    print('#{} {}'.format(t, r))