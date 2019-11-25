import sys
input = sys.stdin.readline
D = [0 for _ in range(101)]
D[1] = 1
D[2] = 1
D[3] = 1
N = int(input())
nl = [int(input()) for _ in range(N)]
for i in range(4, max(nl)+1):
    D[i] = D[i-2] + D[i-3]
r = ''
for i in range(N):
    r = r + str(D[nl[i]]) + '\n'
print(r)