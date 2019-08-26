import time
import sys
sys.stdin = open('asdf.txt')


T = int(input())
for t in range(1, T+1):
    A, B = input().split()
    a = len(A)
    b = len(B)
    c = [[0 for _ in range(a+1)] for _ in range(b+1)]
    for j in range(1, b+1):
        for i in range(1, a+1):
            tp = c[j][i-1]
            if B[j-1] == A[i-1]:
                c[j][i] = c[j - 1][i - 1] + 1
            elif tp >= c[j-1][i]:
                c[j][i] = tp
            else:
                c[j][i] = c[j-1][i]
    print('#{} {}'.format(t, c[b][a]))
