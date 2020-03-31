import sys
input = sys.stdin.readline
N = int(input())
nl = list(map(int, input().split()))
nl.sort()
r = 0
sum = 0
for i in range(N):
    sum += nl[i]
    r += sum
print(r)