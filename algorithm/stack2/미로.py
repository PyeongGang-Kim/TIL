import sys
sys.stdin = open('미로_input.txt')


def dfs():
    global st
    while st:
        cp = st.pop()
        if nl[cp[1]][cp[0]] == 3:
            return 1
        st = st+ck(cp)
    return 0


def ck(P):
    ts = []
    for k in range(len(d)):
        tp = [P[0]+d[k][0], P[1]+d[k][1]]
        if 0 <= tp[0] < N and 0 <= tp[1] < N:
            if nl[tp[1]][tp[0]] == 3:
                return [tp]
            elif not nl[tp[1]][tp[0]]:
                ts.append(tp)
                nl[tp[1]][tp[0]] = 1
    return ts


results = []
d = [[0, 1], [0, -1], [1, 0], [-1, 0]]
T = int(input())
for t in range(1, T+1):
    st = []
    N = int(input())
    nl = [list(map(int, input())) for _ in range(N)]
    for j in range(N):
        for i in range(N):
            if nl[j][i] == 3:
                G = [i, j]
            elif nl[j][i] == 2:
                S = [i, j]
    st.append(S)
    results.append('#{} {}'.format(t, dfs()))
print('\n'.join(results))
