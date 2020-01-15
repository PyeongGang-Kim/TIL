def chk(idx):
    global bcnt, vcnt, r
    tmp = 0
    st = []
    for i in range(1, N):
        if nl[idx][i]:
            if not vl[i]:
                return
            st.append(i)
    for i in st:
        if not vl2[i]:
            vcnt += 1
            vl2[i] = 1
    bcnt += 1
    r.append(str(idx))
    if not vl2[idx]:
        vcnt += 1
        vl2[idx] = 1
    return


N, M = map(int, input().split())
N += 1
nl = [[0]*(N+1) for _ in range(N)]
while M:
    M -= 1
    a, b = map(int, input().split())
    nl[a][b] = 1
    nl[b][a] = 1

K = int(input())
ol = list(map(int, input().split()))
vl = [0] * N
vl2 = [0] * N
for idx in ol:
    vl[idx] = 1
bcnt = 0
vcnt = 0
r = []
for idx in ol:
    if vl[idx]:
        chk(idx)
if vcnt == K:
    print(bcnt)
    print(' '.join(r))
else:
    print('-1')