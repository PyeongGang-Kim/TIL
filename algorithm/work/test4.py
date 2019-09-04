import sys
sys.stdin = open('asdf.txt')


T = int(input())
for t in range(1, T+1):
    N = 5
    sl = [list(input()) for _ in range(N)]
    r = []
    mxl = 0
    for s in sl:
        if len(s) > mxl:
            mxl = len(s)
    for i in range(mxl):
        for j in range(N):
            if len(sl[j]) > i:
                r.append(sl[j][i])
    print('#{} {}'.format(t, ''.join(r)))