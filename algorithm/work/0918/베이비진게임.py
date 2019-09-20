import sys
sys.stdin = open('베이비진게임.txt')


def chk(i):
    for k in range(10):
        if c[i][k] == 3:
            return True
    for k in range(8):
        if c[i][k] and c[i][k+1] and c[i][k+2]:
            return True


T = int(input())
for t in range(1, T+1):
    nl = list(map(int, input().split()))
    a = [0]*10
    b = [0]*10
    c = [a, b]
    win = 0

    for i in range(6):
        a[nl[i*2]] += 1
        b[nl[i*2+1]] += 1
        if chk(0):
            win = 1
            break
        if chk(1):
            win = 2
            break
    print('#{} {}'.format(t, win))