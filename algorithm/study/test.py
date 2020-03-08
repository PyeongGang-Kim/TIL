
n = int(input())

nl = [0] * (n+1)


for i in range(n):
    k = str(i)
    tmp = i
    for s in k:
        tmp += int(s)

    if tmp <= n:
        if not nl[tmp]:
            nl[tmp] = i

print(nl[n] if nl[n] else 0)