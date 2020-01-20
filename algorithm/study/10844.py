N = int(input())
if N == 1:
    print(9)
else:
    D = [[0]*10 for _ in range(N)]
    for i in range(1, 10):
        D[0][i] = 1

    for j in range(1, N):
        D[j][1] = D[j-1][0]
        D[j][8] = D[j-1][9]
        for i in range(1, 9):
            D[j][i-1] = (D[j][i-1] + D[j-1][i]) % 1000000000
            D[j][i+1] = (D[j][i+1] + D[j-1][i]) % 1000000000
    print(sum(D[-1])%1000000000)

