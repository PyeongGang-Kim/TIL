import sys
input = sys.stdin.readline


D = [[0], [1], [2], [0, 1], [0, 2], [1, 2], [0, 1, 2]]
vl = [0] * 7
TC = int(input())
r = []
while TC:
    cnt = 0
    TC -= 1
    nl = list(map(int, input().split()))
    for i in range(3):
        if nl[i]:
            nl[i] -= 1
            cnt += 1
    nl.sort()
    if nl[2] and nl[1]:
        nl[2] -= 1
        nl[1] -= 1
        cnt += 1
    if nl[2] and nl[0]:
        nl[2] -= 1
        nl[0] -= 1
        cnt += 1
    if nl[1] and nl[0]:
        nl[1] -= 1
        nl[0] -= 1
        cnt += 1
    if nl[0] and nl[1] and nl[2]:
        cnt += 1
    r.append(str(cnt))
print('\n'.join(r))