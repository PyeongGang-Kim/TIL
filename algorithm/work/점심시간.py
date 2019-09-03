import sys
sys.stdin = open('asdf.txt')


def comb(d=0):
    global r
    if d == numh:
        return calt()
    arr.append(0)
    tmp = comb(d+1)
    if tmp < r:
        r = tmp
    arr.pop()
    arr.append(1)
    tmp = comb(d+1)
    if tmp < r:
        r = tmp
    arr.pop()
    return r


def calt():
    sl2 = [[], []]
    li = [[], []]
    for i in range(numh):
        tmp = arr[i]
        sl2[tmp].append([abs(sl[tmp][0]-hl[i][0]) + abs(sl[tmp][1] - hl[i][1]) + 1, i])
    sl2[0].sort(key=lambda x: x[0])
    sl2[1].sort(key=lambda x: x[0])

    for j in range(2):
        for i in range(len(sl2[j])):
            if len(li[j])<3:
                li[j].append(sl2[j][i][0])
            else:
                tmp2 = max(sl2[j][i][0], li[j][-3] + sl[j][2])
                li[j].append(tmp2)
    if li[0] and li[1]:
        return max(li[0][-1]+sl[0][2], li[1][-1]+sl[1][2])
    elif li[0]:
        return li[0][-1]+sl[0][2]
    else:
        return li[1][-1]+sl[1][2]




T = int(input())
for t in range(1, T+1):
    N = int(input())
    nl = [list(map(int, input().split())) for _ in range(N)]
    hl = []
    sl = []
    for j in range(N):
        for i in range(N):
            if nl[j][i]:
                if nl[j][i] == 1:
                    hl.append([i, j])
                else:
                    sl.append([i, j, nl[j][i]])
    numh = len(hl)
    arr = [0 for _ in range(numh)]
    r = calt()
    arr = []
    comb()
    print('#{} {}'.format(t, r))
