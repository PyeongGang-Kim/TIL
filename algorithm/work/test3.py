import sys
sys.stdin = open('asdf.txt')


def cal(i):
    global r1, r2
    ori = i
    cnt = 100
    for j in range(99):
        if i >= 1:
            if nl[j][i-1] == 1:
                x = 1
                while i - x >= 0 and nl[j][i-x]:
                    x += 1
                i += - x + 1
                cnt += x - 1
                continue
        if i <= 98:
            if nl[j][i+1] == 1:
                x = 1
                while i + x <= 99 and nl[j][i+x]:
                    x += 1
                i += x - 1
                cnt += x - 1
    if r1 >= cnt:
        r1 = cnt
        r2 = ori



T = 10
for t in range(1, T+1):
    tc = int(input())
    nl = [list(map(int, input().split())) for _ in range(100)]
    r1, r2 = 10000, 0
    for i in range(100):
        if nl[0][i]:
            cal(i)
    print('#{} {}'.format(t, r2))