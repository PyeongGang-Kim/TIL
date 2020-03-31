import sys
'''
문제에 명시한 대로 하면 된다.
%%
인풋 받을때 strip 해줄 것.
'''

# 동쪽은
def rote():
    da[1], da[5] = da[5], da[1]
    da[5], da[3] = da[3], da[5]
    da[2], da[3] = da[3], da[2]
# 서쪽은
def rotw():
    da[5], da[3] = da[3], da[5]
    da[1], da[5] = da[5], da[1]
    da[1], da[2] = da[2], da[1]
# 북쪽은
def rotn():
    da[0], da[2] = da[2], da[0]
    da[2], da[4] = da[4], da[2]
    da[4], da[5] = da[5], da[4]
# 남쪽은
def rots():
    da[4], da[5] = da[5], da[4]
    da[2], da[4] = da[4], da[2]
    da[0], da[2] = da[2], da[0]

def rot(o):
    if o == 4:
        rots()
    elif o == 3:
        rotn()
    elif o == 2:
        rotw()
    else:
        rote()


d = [[1, 0], [-1, 0], [0, -1], [0, 1]]

N, M, sy, sx, K = map(int, sys.stdin.readline().split())
nl = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
kl = list(map(int, sys.stdin.readline().strip().split()))
da = [0, 0, 0, 0, 0, 0]
r = []
for o in kl:
    tx, ty = sx + d[o-1][0], sy + d[o-1][1]
    if 0<=tx<M and 0<=ty<N:
        sx, sy = tx, ty
        rot(o)
        if nl[ty][tx]:
            da[5] = nl[ty][tx]
            nl[ty][tx] = 0
        else:
            nl[ty][tx] = da[5]
        r.append(str(da[2]))
print('\n'.join(r))