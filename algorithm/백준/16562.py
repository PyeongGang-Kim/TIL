import sys
input = sys.stdin.readline

def findset(i):
    if cl[i]:
        cl[i] = findset(cl[i])
    else:
        return i
    return cl[i]


N, M, k = map(int, input().split())
ml = [0]+list(map(int, input().split()))
cl = [0 for _ in range(N+1)]
while M:
    a, b = map(int, input().split())
    tmp1, tmp2 = findset(a), findset(b)
    if tmp1 != tmp2:
        cl[tmp2] = tmp1
    M -= 1
D = dict()
for i in range(1, N+1):
    idx = findset(i)
    if not D.get(idx):
        D[idx] = 10001
    D[idx] = min(D[idx], ml[i])
tmp = k
for i, v in D.items():
    tmp -= v
    if tmp < 0:
        print('Oh no')
        break
if tmp >= 0:
    print(k-tmp)

