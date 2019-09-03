import sys
sys.stdin = open('asdf.txt')


def rm(i, c = 1):
    if i > 1 and not vl[i-1] and ml[i-1][(front[i] - 2) % 8] != ml[i - 2][(front[i-1] + 2) % 8]:
        vl[i-1] = 1
        rm(i-1, -c)
    if i < 4 and not vl[i+1] and ml[i-1][(front[i] + 2) % 8] != ml[i][(front[i+1] - 2) % 8]:
        vl[i+1] = 1
        rm(i+1, -c)

    if c == -1:
        front[i] = (front[i] + 1) % 8
    else:
        front[i] = (front[i] - 1) % 8


T = int(input())
for t in range(1, T+1):
    K = int(input())
    ml = [list(map(int, input().split())) for _ in range(4)]
    ol = [list(map(int, input().split())) for _ in range(K)]
    front = [0, 0, 0, 0, 0]
    for o in ol:
        vl = [0, 0, 0, 0, 0]
        vl[o[0]] = 1
        rm(o[0], o[1])
    r = 0
    for i in range(4):
        if ml[i][front[i+1]]:
            r += 2**(i)

    print('#{} {}'.format(t, r))
