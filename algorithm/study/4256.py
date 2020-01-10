def findpos(s, e):
    global idx
    fndnum = nl1[idx]
    idx += 1
    if s == e:
        r.append(str(fndnum))
        return
    for i in range(s, e+1):
        if fndnum == nl2[i]:
            ## 왼쪽
            if i-s:
                findpos(s, i-1)
            ##오른쪽
            if e-i:
                findpos(i+1, e)
            ##현위치
            r.append(str(fndnum))
            break

T = int(input())
while T:
    n = int(input())
    nl1 = list(map(int, input().split()))
    nl2 = list(map(int, input().split()))
    idx = 0
    r = []
    findpos(0, n-1)

    print(' '.join(r))
    T -= 1