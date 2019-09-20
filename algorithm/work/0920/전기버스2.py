import sys
sys.stdin = open('전기버스2.txt')


def dfs():
    global r
    st = [[1, nl[1], 0]]
    while st:
        idx, charge, cnt = st.pop()
        if cnt >= r:
            continue
        for i in range(1, charge+1):
            if idx+i >= nl[0]:
                if r > cnt:
                    r = cnt
                continue
            st.append([idx+i, nl[idx+i], cnt+1])


T = int(input())
for t in range(1, T+1):
    nl = list(map(int, input().split()))
    r = 100
    dfs()
    print('#{} {}'.format(t, r))

