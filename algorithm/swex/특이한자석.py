def rotate(idx, s, ro):
    if (s == 0 or s == 1) and idx > 0:
        if ml[idx][(mil[idx]-2)%8] != ml[idx-1][(mil[idx-1]+2)%8]:
            rotate(idx-1, 1, -ro)
    if (s == 0 or s == 2) and idx < 3:
        if ml[idx][(mil[idx]+2)%8] != ml[idx+1][(mil[idx+1]-2)%8]:
            rotate(idx+1, 2, -ro)
    if ro == 1:
        mil[idx] = (mil[idx]-1)%8
    else:
        mil[idx] = (mil[idx]+1)%8


T = int(input())
for tc in range(1, T+1):
    K = int(input())
    ml = [list(map(int, input().split())) for _ in range(4)]
    mil = [0, 0, 0, 0]
    for _ in range(K):
        idx, ro = map(int, input().split())
        rotate(idx-1, 0, ro)
    r = 0
    for i in range(4):
        r += ml[i][mil[i]]*2**i
    print('#{} {}'.format(tc, r))