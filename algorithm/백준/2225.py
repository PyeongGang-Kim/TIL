'''
12 3은
0, 12 2, 1 11 2 ...  10 2 2 11 1 2   12 0, 2
    13      12          3       2       1
    13*14/2
12 4는
0, 12 3    1, 11 3...   12 0 3
    13*14/2 12*13/2     1*2/2

재귀호출하면서 값을 줄이면 된다.
k값이 1씩 줄어들면서
k가 2가 되면 n+1 값들의 합(n+2)*(n+1)/2
'''
n, k  = map(int, input().split())
n1 = n+1
k1 = k+1
D = [[0 for i in range(n1)] for i in range(k1)]
D[1] = [1 for i in range(n1)]
D[2] = [i+1 for i in range(n1)]
for d in range(3, k1):
    for i in range(n1):
        tmp = 0
        for j in range(i+1):
            tmp = (tmp + D[d-1][j]) % 1000000000
        D[d][i] = tmp


print(D[k][n])


D = [[0 for i in range(n+1)] for i in range(k+1)]
D[1] = [1 for i in range(n+1)]
D[2] = [i+1 for i in range(n+1)]
for d in range(3, k+1):
    for i in range(n+1):
        tmp = 0
        for j in range(i+1):
            tmp = (tmp + D[d-1][j]) % 1000000000
        D[d][i] = tmp


print(D[k][n])