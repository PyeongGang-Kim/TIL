
D = {'A': 3, 'B': 2, 'C': 1, 'D': 0}
for t in range(1, int(input())+1):
    n = input()
    nl = [0 for i in range(len(n))]
    tl = [[] for i in range(len(n))]
    if n[0] == 'A':
        for j in range(1, 16):
            if j & 1 << 3:
                tl[0].append([j, 1])
    else:
        for j in range(1, 16):
            if j & 1 << 3 and j & 1 << D[n[0]]:
                tl[0].append([j, 1])

    for i in range(1, len(n)):
        tmp2 = []
        for j in range(1, 16):
            if j & 1 << D[n[i]]:
                tmp2.append([j, 0])

        cnt = 0
        for n1 in tl[i - 1]:
            for n2 in tmp2:
                if n1[0] & n2[0]:
                    n2[1] = (n2[1] + n1[1])%1000000007
        tl[i] = tmp2
    r = 0
    for i in (tl[-1]):
        r = (r + i[1]) % 1000000007
    print('#{} {}'.format(t, r))