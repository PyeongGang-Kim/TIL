import sys
input = sys.stdin.readline

N = int(input())
nl = list(map(int, input().split()))
B, C = map(int, input().split())
r = 0
for i in range(N):
    if nl[i] > B:
        r += 1 + (nl[i]-B)//C
        if (nl[i]-B)%C:
            r += 1
    else:
        r += 1
print(r)