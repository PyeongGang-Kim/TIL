D = [[0 for _ in range(15)] for _ in range(15)]
for i in range(15):
    D[0][i] = i
for j in range(1, 15):
    for i in range(1, 15):
        D[j][i] = D[j][i-1] + D[j-1][i]
tc = int(input())
r = []
while tc:
    tc -= 1
    a, b = int(input()), int(input())
    r.append(str(D[a][b]))
print('\n'.join(r))