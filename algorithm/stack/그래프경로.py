import sys
sys.stdin = open('그래프경로.txt')


def dfs():
    vl[S-1] = 1
    while st:
        tmp = st.pop()
        if tmp == G:
            return 1
        for n in nl:
            if tmp == n[0] and not vl[n[1]-1]:
                vl[n[1]-1] = 1
                st.append(n[1])
    return 0




T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())
    vl = [0 for _ in range(V)]
    nl = []
    for _ in range(E):
        nl.append(list(map(int, input().split())))
    S, G = map(int, input().split())
    st = [S]
    print('#{} {}'.format(t, dfs()))
