import sys
input = sys.stdin.readline

def findset(nameStr):
    if D[nameStr][0] != nameStr:
        D[nameStr][0] = findset(D[nameStr][0])
    else:
        return nameStr
    return D[nameStr][0]

r = []
T = int(input())
for _ in range(T):
    D = dict()
    F = int(input())
    for _ in range(F):
        A, B = input().split()
        if not D.get(A):
            D[A] = [A, 1]
        if not D.get(B):
            D[B] = [B, 1]
        tmp1, tmp2 = findset(A), findset(B)
        if tmp1 != tmp2:
            D[tmp2][0] = tmp1
            D[tmp1][1] += D[tmp2][1]
        r.append(str(D[tmp1][1]))
print('\n'.join(r))