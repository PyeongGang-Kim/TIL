N = int(input())
nl = list(map(int, input().split()))
result = nl[0]
for i in range(1, N):
    if nl[i-1] > 0:
        nl[i] = nl[i-1] + nl[i]
    result = max(result, nl[i])
print(result)