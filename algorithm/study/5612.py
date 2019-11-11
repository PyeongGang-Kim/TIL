T = int(input())
N = int(input())
r = 0
for t in range(T):
    a, b = map(int, input().split())
    N += a - b
    if N < 0:
        r = 0
        break
    r = max(N, r)
print(r)