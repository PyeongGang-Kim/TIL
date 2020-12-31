import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
inf = 0xfffffff
nl = [[inf for _ in range(n)] for _ in range(n)]
while m:
    m -= 1
    a, b, d = map(int, input().split())
    a -= 1
    b -= 1
    nl[a][b] = min(d, nl[a][b])

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i != j and nl[i][j] > nl[i][k] + nl[k][j]:
                nl[i][j] = nl[i][k] + nl[k][j]

result = []
for j in range(n):
    temp = " ".join([str(nl[j][i]) if nl[j][i] != inf else "0" for i in range(n)])
    result.append(temp)
print("\n".join(result))