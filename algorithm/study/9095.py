import sys
input = sys.stdin.readline

def cnt(s = 0):
    global ncnt
    if s == N:
        ncnt += 1
        return
    elif s > N:
        return
    for i in range(1, 4):
        cnt(s+i)


r = []
T = int(input())
for t in range(T):
    ncnt = 0
    N = int(input())
    cnt()
    r.append(str(ncnt))
print('\n'.join(r))