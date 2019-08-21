import sys
sys.stdin = open('test2_input.txt')


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    nl = []
    for m in range(M):
        nl.append(list(map(int, input().split())))
    print(nl)
    for n in range(1, N+1):
        st = [n]
        while 1:
            for v in nl:
                if v[0] == st[-1]:
                    st.append(v[0])
                    break
                elif v[1] == st[-1]:
                    st.append(v[1])
                    break
