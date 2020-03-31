N = int(input())
ml = [[] for _ in range(N)]
ul = [[[] for _ in range(N)] for _ in range(N)]

for j in range(N):
    tmp = list(map(int, input().split()))
    for i in range(N):
        ml[j].append([tmp[i<<1]-1, tmp[(i<<1)+1]-1])
print(ml)