h, w = map(int, input().split())
rl = map(int, input().split())
cl = map(int, input().split())
vl = [[0 for i in range(w)] for i in range(h)]
cnt = 0
for i, c in enumerate(cl):
    for k in range(c+1):
        if k == c:
            if k < h:
                vl[k][i] = -1
                cnt += 1
        else:
            vl[k][i] = 1
            cnt += 1

chk = 0
for i, r in enumerate(rl):
    for k in range(r+1):
        if k == r:
            if k < w:
                if vl[i][k] == 1:
                    chk = 1
                    break
                elif vl[i][k] == 0:
                    vl[i][k] = -1
                    cnt += 1
        elif vl[i][k] == 0:
            vl[i][k] = 2
            cnt += 1
        elif vl[i][k] == -1:
            chk = 1
            break
    if chk:
        break
if chk:
    print(0)
else:
    print((2**(w*h-cnt))%1000000007)