def perm(s, idx):
    if idx == N:
        global rmax, rmin
        rmax = max(rmax, s)
        rmin = min(rmin, s)
        return
    for i in range(4):
        if ol[i]:
            ol[i] -= 1
            if i == 0:
                perm(s+nl[idx], idx+1)
            elif i == 1:
                perm(s-nl[idx], idx+1)
            elif i == 2:
                perm(s*nl[idx], idx+1)
            else:
                perm(int(s/nl[idx]), idx+1)
            ol[i] += 1


T = int(input())
for t in range(1, T+1):
    N = int(input())
    ol = list(map(int, input().split()))
    nl = list(map(int, input().split()))
    rmax = -100000000
    rmin = 100000000
    perm(nl[0], 1)
    print('#{} {}'.format(t, rmax-rmin))