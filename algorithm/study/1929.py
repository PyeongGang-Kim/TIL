import math
N, M = map(int, input().split())
D = [True for _ in range(M+1)]
M2 = int(math.sqrt(M))
for i in range(2, M2+1):
    if D[i]:
        tmp = i*2
        while tmp <= M:
            D[tmp] = False
            tmp += i
r = []
for i in range(N, M+1):
    if D[i]:
        r.append(str(i))
print('\n'.join(r))