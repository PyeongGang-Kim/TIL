'''
0/1 냅색 문제
'''
N, K = map(int, input().split())
wv = [[0, 0]]
for _ in range(N):
    wv.append(list(map(int, input().split())))
D = [[0 for _ in range(K+1)] for _ in range(N+1)]
for j in range(1, N+1):
    for i in range(1, K+1):
        if i >= wv[j][0]:
            D[j][i] = max(D[j-1][i], D[j-1][i-wv[j][0]] + wv[j][1])
        else:
            D[j][i] = D[j-1][i]
print(D[-1][-1])