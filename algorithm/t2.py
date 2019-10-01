T = int(input())
for t in range(1, T+1):
    a = ''.join(sorted(list(input())))
    R = 0
    tmp = []
    for i in range(1, len(a)+1):
        for j in range(len(a)-i+1):
            tmp.append(a[j:j+i])
    for w in tmp:
        chk = True
        for c in range(len(w)//2):
            if w[c] != w[-1-c]:
                chk = False
                break
        if chk:
            R += 1

    print('#{} {}'.format(t, R))