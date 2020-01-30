import sys
input = sys.stdin.readline

n, k = map(int, input().split())
tmp = int(input())
D = [0] * (k+1)
i = 0
while i <= k:
    D[i] = 1
    i += tmp
for i in range(1, n):
    tmp = int(input())
    for j in range(tmp, k+1):
        D[j] += D[j-tmp]
r = 0
print(D[-1])