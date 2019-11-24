import sys
input = sys.stdin.readline

N, K = map(int, input().split())
nl = [int(input()) for _ in range(N)]
n = 0
cnt = 0
for i in range(N-1, -1, -1):
    if K-n >= nl[i]:
        tmp = (K-n)//nl[i]
        cnt += tmp
        n += tmp*nl[i]
    if K == n:
        break
print(cnt)