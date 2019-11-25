D = [0 for _ in range(50)]
D[0] = 0
D[1] = 1
D[2] = 1
N = int(input())
for i in range(3, N+1):
    D[i] = D[i-1] + D[i-2]
print(D[N])
