def caldis(idx):
    if nl[idx][0]:
        nl[idx][0], tmp = caldis(nl[idx][0])
        nl[idx][1] += tmp
        return nl[idx][0], nl[idx][1]
    else:
        return idx, 0


r = []
T = int(input())
while T:
    N = int(input())
    nl = [[0, 0] for _ in range(N+1)]
    a = input()
    while a[0] != 'O':
        if a[0] == 'E':
            o, n = a.split()
            t1, t2 = caldis(int(n))
            r.append(str(t2))
        else:
            o, n1, n2 = a.split()
            n1 = int(n1)
            n2 = int(n2)
            nl[n1][1] = abs(n1-n2)%1000
            nl[n1][0] = int(n2)
        a = input()
    T -= 1
print('\n'.join(r))