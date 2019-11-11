D = {'1': '3', '2': '4', '3': '1', '4': '2', ' ': ' '}

N = int(input())
nl = input().strip()
nl = nl + ' ' + nl
nl2 = ''
for s in nl:
    nl2 = D[s] + nl2

r = []
cnt = 0
K = int(input().strip())
chk = False
chk2 = False
for _ in range(K):
    tmp = input()
    for i in range(0, 2*N, 2):
        chk = False
        for j in range(0, 2*N, 2):
            if nl[i+j] != tmp[j]:
                chk = True
                break
        if not chk:
            break
    if not chk:
        cnt += 1
        r.append(tmp)
    else:
        for i in range(0, 2 * N, 2):
            chk = False
            for j in range(0, 2 * N, 2):
                if nl2[i + j] != tmp[j]:
                    chk = True
                    break
            if not chk:
                break
        if not chk:
            cnt += 1
            r.append(tmp)

print(cnt)
print('\n'.join(r))

