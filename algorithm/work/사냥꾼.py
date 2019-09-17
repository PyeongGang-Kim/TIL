import sys
sys.stdin = open('사냥꾼.txt')


def hunt(i, j):
    for dx, dy in d:
        for n in range(1, N):
            tx, ty = i + dx*n, j + dy*n
            if not chk(tx, ty):
                break


def chk(i, j):
    global cnt
    if 0 <= i < N and 0 <= j < N:
        if nl[j][i] == 2:
            cnt += 1
        if nl[j][i] == 3:
            return False
        else:
            return True
    else:
        return False


d = [[0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1]]
T = int(input())
for t in range(1, T+1):
    N = int(input())
    nl = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for j in range(N):
        for i in range(N):
            if nl[j][i] == 1:
                hunt(i, j)
    print('#{} {}'.format(t, cnt))