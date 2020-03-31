n = int(input())
nl = list(map(int, input().split()))
D = [[0, 0] for _ in range(n)]
D[0][0] = nl[0]
D[0][1] = min(nl[0], nl[1])

chk = 1
r1 = [str(D[0][0])]
r2 = [str(D[0][1])]
for i in range(1, n):
    if nl[i] > nl[i-1]:
        D[i][0] = D[i-1][0] + nl[i]
        D[i][1] = D[i-1][1] + nl[i-1]
        if chk:
            r1.append(str(nl[i]))
            r2.append(str(min(nl[i], nl[i-1])))
        else:
            r1.append(str(min(nl[i], nl[i-1])))
            r2.append(str(nl[i]))
    else:
        if chk:
            chk = 0
        else:
            chk = 1
        D[i][0] = D[i-1][1] + nl[i]
        D[i][1] = D[i-1][0] + nl[i]

        r1.append(str(nl[i]))
        r2.append(str(nl[i]))

if D[-1][0] > D[-1][1]:
    if chk:
        print(' '.join(r1))
    else:
        print(' '.join(r2))
else:
    if chk:
        print(' '.join(r2))
    else:
        print(' '.join(r1))


print(r1)
print(r2)