import sys
M, N = map(int,sys.stdin.readline().split())
n = 0
nl = [[1 for _ in range(M)] for _ in range(M)]
dl = [[0 for _ in range(M)] for _ in range(M)]
ml = [0 for _ in range(M-1)]
ml2 = [0 for _ in range(M)]
il = [0 for _ in range(2*M-1)]
while n < N:
    a, b, c = map(int, sys.stdin.readline().split())
    i = 0
    while i < a:
        il[i] = 0
        i += 1
    b += a
    while i < b:
        il[i] = 1
        i += 1
    c += b
    while i < c:
        il[i] = 2
        i += 1
    for i in range(M-1):
        ml[i] += il[i+M]
    for i in range(M):
        ml2[i] += il[i]

    n += 1

for j in range(M):
    for i in range(1, M):
        nl[j][i] += ml[i-1]
for j in range(M):
    nl[j][0] += ml2[M-1-j]
for m in range(M):
    print(' '.join(map(str, nl[m])))