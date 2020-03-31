def rotate(idx, s, ro):
    if (s == 0 or s == 1) and idx > 0:
        if ml[idx][(mil[idx]-2)%8] != ml[idx-1][(mil[idx-1]+2)%8]:
            rotate(idx-1, 1, -ro)
    if (s == 0 or s == 2) and idx < N-1:
        if ml[idx][(mil[idx]+2)%8] != ml[idx+1][(mil[idx+1]-2)%8]:
            rotate(idx+1, 2, -ro)
    if ro == 1:
        mil[idx] = (mil[idx]-1)%8
    else:
        mil[idx] = (mil[idx]+1)%8


N = int(input())
ml = [list(map(int, list(input()))) for _ in range(N)]
mil = [0 for _ in range(N)]
K = int(input())
for _ in range(K):
    idx, ro = map(int, input().split())
    rotate(idx-1, 0, ro)
r = 0
for i in range(N):
    r += ml[i][mil[i]]
print(r)